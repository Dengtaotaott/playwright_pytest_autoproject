"""
项目配置文件
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 项目根目录
BASE_DIR = Path(__file__).parent.parent


class Settings:
    """项目配置类"""
    
    # 基础URL
    BASE_URL = os.getenv("BASE_URL", "https://ultimateqa.com/automation")
    # BASE_URL = os.getenv("BASE_URL", "http://xn--6frwj470ei1s2kl.com/demo")
    
    # 浏览器配置
    BROWSER = os.getenv("BROWSER", "chromium")  # chromium, firefox, webkit
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    SLOW_MO = int(os.getenv("SLOW_MO", "0"))  # 操作延迟（毫秒）
    BROWSER_TIMEOUT = int(os.getenv("BROWSER_TIMEOUT", "20"))  # 浏览器超时（秒）
    
    # 区域和时区
    LOCALE = os.getenv("LOCALE", "zh-CN")
    TIMEZONE = os.getenv("TIMEZONE", "Asia/Shanghai")
    
    # HTTPS配置
    IGNORE_HTTPS_ERRORS = os.getenv("IGNORE_HTTPS_ERRORS", "False").lower() == "true"
    
    # 权限配置
    PERMISSIONS = os.getenv("PERMISSIONS", "").split(",") if os.getenv("PERMISSIONS") else []
    
    # 测试数据路径
    DATA_DIR = BASE_DIR / "data"
    TEST_DATA_FILE = DATA_DIR / "test_data.yaml"
    
    # 报告路径
    REPORTS_DIR = BASE_DIR / "reports"
    LOGS_DIR = BASE_DIR / "logs"
    SCREENSHOTS_DIR = BASE_DIR / "screenshots"
    
    # API配置
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.example.com")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))
    
    # 数据库配置（如需要）
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "3306"))
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "test_db")
    
    # 等待时间配置
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "20"))  # 隐式等待（秒）
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "30"))  # 显式等待（秒）
    
    @classmethod
    def create_directories(cls):
        """创建必要的目录"""
        directories = [
            cls.DATA_DIR,
            cls.REPORTS_DIR,
            cls.LOGS_DIR,
            cls.SCREENSHOTS_DIR,
        ]
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)


# 初始化时创建目录
Settings.create_directories()

