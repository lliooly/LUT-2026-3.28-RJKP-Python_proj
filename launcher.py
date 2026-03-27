from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parent


def get_available_tasks():
    tasks = []
    for path in PROJECT_ROOT.iterdir():
        if path.is_dir() and path.name.isdigit() and (path / "main.py").exists():
            tasks.append(int(path.name))
    return sorted(tasks)


def print_task_list(tasks):
    print("可运行的题号：")
    print(" ".join(str(task) for task in tasks))


def prompt_for_task(tasks):
    valid_tasks = {str(task) for task in tasks}
    while True:
        choice = input("请输入要运行的题号（输入 q 退出）：").strip()
        if choice.lower() in {"q", "quit", "exit"}:
            return None
        if choice in valid_tasks:
            return int(choice)
        print("题号无效，请重新输入。")


def run_task(task_number):
    task_dir = PROJECT_ROOT / str(task_number)
    script_path = task_dir / "main.py"

    if not script_path.exists():
        print(f"第 {task_number} 题不存在。")
        return 1

    print(f"正在运行第 {task_number} 题：{script_path.relative_to(PROJECT_ROOT)}", flush=True)
    completed = subprocess.run([sys.executable, script_path.name], cwd=task_dir)
    return completed.returncode


def print_help(tasks):
    print("用法：")
    print("  uv run python launcher.py")
    print("  uv run python launcher.py <题号>")
    print("  uv run python launcher.py --list")
    print()
    print_task_list(tasks)


def main():
    tasks = get_available_tasks()
    if not tasks:
        print("未找到可运行的题目。")
        return 1

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in {"-h", "--help"}:
            print_help(tasks)
            return 0
        if arg in {"-l", "--list"}:
            print_task_list(tasks)
            return 0
        if not arg.isdigit():
            print("请输入有效的题号。")
            print_help(tasks)
            return 1

        task_number = int(arg)
        if task_number not in tasks:
            print(f"题号 {task_number} 不存在。")
            print_task_list(tasks)
            return 1
        return run_task(task_number)

    print("Python 练习题启动器")
    print_task_list(tasks)
    task_number = prompt_for_task(tasks)
    if task_number is None:
        print("已退出启动器。")
        return 0
    return run_task(task_number)


if __name__ == "__main__":
    raise SystemExit(main())
