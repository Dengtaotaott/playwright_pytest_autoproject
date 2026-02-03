"""
Pytest配置文件 - 全局fixture和钩子函数
"""
import pytest
from playwright.sync_api import Playwright, Browser, BrowserContext, Page
from loguru import logger
import os
from datetime import datetime

from utils.browser_manager import BrowserManager
from utils.logger_config import setup_logger
from config.settings import Settings


# 配置日志
setup_logger()

"""
跳过测试文件的配置                                                           
# ==================== 用例收集配置 ====================
# 在用例收集阶段跳过指定的文件和目录
# pytest会自动识别conftest.py中的collect_ignore_glob变量
# 使用glob模式匹配，支持通配符
collect_ignore_glob = [
    "**/logs/**",           # 跳过logs目录及其所有内容
    "**/reports/**",        # 跳过reports目录及其所有内容
    "**/__pycache__/**",    # 跳过__pycache__目录
    "**/*.pyc",             # 跳过所有.pyc文件
    "**/.pytest_cache/**",  # 跳过pytest缓存目录
    "**/unit/**",           # 跳过unit目录（单元测试，如需运行可删除此行）
    "**/screenshots/**",    # 跳过screenshots目录
    "tests/test_complicated-page.py",    # 跳过complicated-page.py文件
]
"""

@pytest.fixture(scope="session")
def settings():
    """全局配置fixture"""
    return Settings()


@pytest.fixture(scope="session")
def playwright():
    """Playwright实例"""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser_type_launch_args(settings):
    """浏览器启动参数"""
    launch_args = {
        "headless": settings.HEADLESS,
        "slow_mo": settings.SLOW_MO,
        "timeout": settings.BROWSER_TIMEOUT * 1000,
        "args": ["--start-maximized"],
    }
    return launch_args


@pytest.fixture(scope="session")
def browser(playwright, browser_type_launch_args, settings):
    """浏览器实例 - session级别"""
    browser_manager = BrowserManager(playwright)
    browser = browser_manager.launch_browser(
        browser_type=settings.BROWSER,
        **browser_type_launch_args
    )
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser, settings, request):
    """浏览器上下文 - 每个测试函数一个。终端设置 TRACE=1 再运行 pytest 时会录制 Trace 到 test-results/。"""
    # 按参考示例使用 no_viewport=True 以占用最大可用尺寸
    context = browser.new_context(
        no_viewport=True,
        locale=settings.LOCALE,
        timezone_id=settings.TIMEZONE,
        ignore_https_errors=settings.IGNORE_HTTPS_ERRORS,
    )
    
    # 设置权限
    if settings.PERMISSIONS:
        context.grant_permissions(settings.PERMISSIONS)
    
    # 仅当环境变量 TRACE=1（或 true/yes）时录制 Trace，便于终端调试
    trace_on = os.environ.get("TRACE", "").strip().lower() in ("1", "true", "yes")
    if trace_on:
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    yield context
    
    if trace_on:
        trace_dir = "test-results"
        os.makedirs(trace_dir, exist_ok=True)
        trace_path = os.path.join(trace_dir, f"trace-{request.node.name}.zip")
        context.tracing.stop(path=trace_path)
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """页面实例 - 每个测试函数一个"""
    page = context.new_page()
    
    # 设置默认超时
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(30000)
    
    yield page
    page.close()


@pytest.fixture(scope="function", autouse=True)
def setup_test(page, request):
    """测试前置和后置处理"""
    test_name = request.node.name
    logger.info(f"开始执行测试: {test_name}")
    
    yield
    
    # 测试失败时截图
    if request.node.rep_call.failed:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"{screenshot_dir}/{test_name}_{timestamp}.png"
        page.screenshot(path=screenshot_path, full_page=True)
        logger.error(f"测试失败，截图已保存: {screenshot_path}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """获取测试结果"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
