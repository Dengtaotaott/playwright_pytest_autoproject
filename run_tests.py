"""
测试运行脚本
"""
import subprocess
import sys
import os
from pathlib import Path


def find_project_root():
    """
    查找项目根目录（包含 pytest.ini 的目录）
    
    Returns:
        Path: 项目根目录路径
    """
    current = Path(__file__).resolve().parent
    
    # 向上查找包含 pytest.ini 的目录
    for parent in [current] + list(current.parents):
        if (parent / "pytest.ini").exists():
            return parent
    
    # 如果找不到，返回脚本所在目录
    return current


def run_tests(marker=None, file=None, parallel=False, html_report=True):
    """
    运行测试
    
    Args:
        marker: 测试标记（如：smoke, login等）
        file: 测试文件路径
        parallel: 是否并行运行
        html_report: 是否生成HTML报告
    """
    # 确保在项目根目录运行
    project_root = find_project_root()
    os.chdir(project_root)
    
    # 使用当前 Python 解释器调用 pytest，避免 Windows 下找不到可执行文件
    cmd = [sys.executable, "-m", "pytest", "-v"]
    
    if marker:
        cmd.extend(["-m", marker])
    
    if file:
        # 如果提供的是相对路径，确保相对于项目根目录
        file_path = Path(file)
        if not file_path.is_absolute():
            # 如果文件路径不包含 tests/，自动添加
            if not str(file_path).startswith("tests"):
                file_path = project_root / "tests" / file_path
            else:
                file_path = project_root / file_path
        cmd.append(str(file_path))
    
    if parallel:
        cmd.extend(["-n", "auto"])
    
    if html_report:
        cmd.extend(["--html=reports/report.html", "--self-contained-html"])
    
    # 子进程不继承 PWDEBUG，避免通过 run_tests.py 运行时误开 Playwright Inspector
    env = os.environ.copy()
    env.pop("PWDEBUG", None)

    print(f"执行命令: {' '.join(cmd)}")
    print(f"工作目录: {project_root}")
    result = subprocess.run(cmd, cwd=project_root, env=env)
    sys.exit(result.returncode)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="运行自动化测试")
    parser.add_argument("-m", "--marker", help="测试标记（如：smoke, login）")
    parser.add_argument("-f", "--file", help="测试文件路径")
    parser.add_argument("-p", "--parallel", action="store_true", help="并行运行测试")
    parser.add_argument("--no-html", action="store_true", help="不生成HTML报告")
    
    args = parser.parse_args()
    
    run_tests(
        marker=args.marker,
        file=args.file,
        parallel=args.parallel,
        html_report=not args.no_html
    )

