from __future__ import annotations

from pathlib import Path
import os
import sys
import warnings

BASE_DIR = Path(__file__).resolve().parent
os.environ.setdefault("MPLCONFIGDIR", str(BASE_DIR / ".matplotlib"))

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from sklearn.datasets import load_digits
    from sklearn.exceptions import ConvergenceWarning
    from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report
    from sklearn.model_selection import train_test_split
    from sklearn.neural_network import MLPClassifier
    from sklearn.preprocessing import MinMaxScaler
except ModuleNotFoundError:
    print("请先启用 full 可选依赖，例如：uv sync --extra full")
    sys.exit(0)

OUTPUT_DIR = BASE_DIR / "output"
METRICS_FILE = OUTPUT_DIR / "metrics_summary.txt"
TRAINING_CURVES_FILE = OUTPUT_DIR / "training_curves.png"
CONFUSION_MATRIX_FILE = OUTPUT_DIR / "confusion_matrix.png"
PREDICTION_SAMPLES_FILE = OUTPUT_DIR / "prediction_samples.png"


def configure_matplotlib() -> None:
    plt.rcParams["font.sans-serif"] = ["PingFang SC", "Hiragino Sans GB", "Arial Unicode MS", "SimHei"]
    plt.rcParams["axes.unicode_minus"] = False


def prepare_data():
    digits = load_digits()
    x_train, x_test, y_train, y_test = train_test_split(
        digits.data,
        digits.target,
        test_size=0.2,
        random_state=42,
        stratify=digits.target,
    )
    scaler = MinMaxScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)
    return digits, x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled


def train_model(x_train_scaled, y_train):
    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    warnings.filterwarnings("ignore", category=RuntimeWarning, module=r"sklearn\.utils\.extmath")
    model = MLPClassifier(
        hidden_layer_sizes=(64, 32),
        activation="relu",
        solver="adam",
        batch_size=64,
        learning_rate_init=0.001,
        max_iter=300,
        early_stopping=True,
        n_iter_no_change=20,
        random_state=42,
    )
    model.fit(x_train_scaled, y_train)
    return model


def plot_training_curves(model) -> None:
    figure, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    axes[0].plot(range(1, len(model.loss_curve_) + 1), model.loss_curve_, color="#2563EB", linewidth=2)
    axes[0].set_title("训练损失曲线")
    axes[0].set_ylabel("Loss")
    axes[0].grid(linestyle="--", alpha=0.3)

    validation_scores = getattr(model, "validation_scores_", [])
    if validation_scores:
        axes[1].plot(range(1, len(validation_scores) + 1), validation_scores, color="#059669", linewidth=2)
        axes[1].set_title("验证集准确率曲线")
        axes[1].set_ylabel("Accuracy")
        axes[1].set_xlabel("Epoch")
        axes[1].grid(linestyle="--", alpha=0.3)
    else:
        axes[1].text(0.5, 0.5, "未启用 early stopping，暂无验证曲线。", ha="center", va="center")
        axes[1].set_axis_off()

    figure.tight_layout()
    figure.savefig(TRAINING_CURVES_FILE, dpi=150, bbox_inches="tight")
    plt.close(figure)


def plot_confusion_matrix(model, x_test_scaled, y_test) -> None:
    figure, axis = plt.subplots(figsize=(8, 7))
    ConfusionMatrixDisplay.from_estimator(model, x_test_scaled, y_test, cmap="Blues", ax=axis, colorbar=False)
    axis.set_title("手写数字识别混淆矩阵")
    figure.tight_layout()
    figure.savefig(CONFUSION_MATRIX_FILE, dpi=150, bbox_inches="tight")
    plt.close(figure)


def plot_prediction_samples(x_test, y_test, y_pred) -> None:
    figure, axes = plt.subplots(3, 4, figsize=(10, 8))
    figure.suptitle("测试集预测样例")

    for axis, sample, actual_label, predicted_label in zip(axes.flat, x_test[:12], y_test[:12], y_pred[:12]):
        axis.imshow(sample.reshape(8, 8), cmap="binary")
        axis.set_title(f"预测 {predicted_label} / 真实 {actual_label}")
        axis.axis("off")

    figure.tight_layout()
    figure.savefig(PREDICTION_SAMPLES_FILE, dpi=150, bbox_inches="tight")
    plt.close(figure)


def build_summary(model, x_train_scaled, y_train, y_test, y_pred) -> str:
    train_accuracy = accuracy_score(y_train, model.predict(x_train_scaled))
    test_accuracy = accuracy_score(y_test, y_pred)
    report_dict = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
    worst_digit, worst_digit_info = min(
        ((digit, report_dict[str(digit)]) for digit in range(10)),
        key=lambda item: item[1]["recall"],
    )
    validation_score = getattr(model, "best_validation_score_", None)

    lines = [
        "数据集：sklearn digits 手写数字数据集，共 1797 条样本，10 个类别。",
        "预处理：训练集 / 测试集按 8:2 划分，并使用 MinMaxScaler 将像素缩放到 0-1。",
        "模型结构：输入层 64 维，隐藏层 (64, 32)，输出层 10 类，激活函数 ReLU，优化器 Adam。",
        f"训练集准确率：{train_accuracy:.4f}",
        f"测试集准确率：{test_accuracy:.4f}",
    ]

    if validation_score is not None:
        lines.append(f"最佳验证集准确率：{validation_score:.4f}")

    lines.extend(
        [
            (
                "结果分析：训练集与测试集准确率差距较小，说明当前模型在该数据集上的泛化能力较稳定，"
                "未出现明显过拟合。"
            ),
            (
                f"结果分析：召回率最低的类别是数字 {worst_digit}，其召回率为 "
                f"{worst_digit_info['recall']:.4f}，说明该类在部分笔迹下仍存在混淆。"
            ),
            "",
            "分类报告：",
            classification_report(y_test, y_pred, digits=4, zero_division=0),
        ]
    )
    return "\n".join(lines)


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    configure_matplotlib()

    digits, x_train, x_test, y_train, y_test, x_train_scaled, x_test_scaled = prepare_data()
    model = train_model(x_train_scaled, y_train)
    y_pred = model.predict(x_test_scaled)

    summary_text = build_summary(model, x_train_scaled, y_train, y_test, y_pred)
    METRICS_FILE.write_text(summary_text, encoding="utf-8")
    plot_training_curves(model)
    plot_confusion_matrix(model, x_test_scaled, y_test)
    plot_prediction_samples(x_test, y_test, y_pred)

    test_accuracy = accuracy_score(y_test, y_pred)
    print(f"样本总数：{len(digits.data)}")
    print("模型结构：64 -> 64 -> 32 -> 10")
    print(f"测试集准确率：{test_accuracy:.4f}")
    print(f"训练摘要已保存：{METRICS_FILE.name}")
    print(f"训练曲线已保存：{TRAINING_CURVES_FILE.name}")
    print(f"混淆矩阵已保存：{CONFUSION_MATRIX_FILE.name}")
    print(f"预测样例图已保存：{PREDICTION_SAMPLES_FILE.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
