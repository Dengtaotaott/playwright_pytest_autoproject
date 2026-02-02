"""
日志配置工具
"""
import sys
from pathlib import Path
from loguru import logger
from datetime import datetime


def setup_logger():
    """配置日志系统"""
    # 移除默认处理器
    logger.remove()
    
    # 控制台输出 - 彩色格式
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO",
        colorize=True,
    )
    
    # 文件输出 - 详细格式
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    log_file = log_dir / f"test_{datetime.now().strftime('%Y%m%d')}.log"
    logger.add(
        log_file,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="DEBUG",
        rotation="00:00",  # 每天午夜轮转
        retention="30 days",  # 保留30天
        compression="zip",  # 压缩旧日志
        encoding="utf-8",
    )
    
    logger.info("日志系统初始化完成")

