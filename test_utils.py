from pathlib import Path
import importlib.util
import os
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
PYTHON = sys.executable


def run_task(task_no, input_data=""):
    task_dir = PROJECT_ROOT / str(task_no)
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.run(
        [PYTHON, "main.py"],
        input=input_data,
        text=True,
        capture_output=True,
        cwd=task_dir,
        env=env,
    )


def assert_success(testcase, result):
    testcase.assertEqual(
        result.returncode,
        0,
        msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}",
    )


def has_module(name):
    return importlib.util.find_spec(name) is not None
