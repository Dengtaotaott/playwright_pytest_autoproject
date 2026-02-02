"""
浏览器管理工具类
"""
from playwright.sync_api import Playwright, Browser
from loguru import logger
from typing import Optional


class BrowserManager:
    """浏览器管理器"""
    
    def __init__(self, playwright: Playwright):
        self.playwright = playwright
        self._browser: Optional[Browser] = None
    
    def launch_browser(
        self,
        browser_type: str = "chromium",
        headless: bool = True,
        slow_mo: int = 0,
        timeout: int = 30000,
        **kwargs
    ) -> Browser:
        """
        启动浏览器
        
        Args:
            browser_type: 浏览器类型 (chromium, firefox, webkit)
            headless: 是否无头模式
            slow_mo: 操作延迟（毫秒）
            timeout: 超时时间（毫秒）
            **kwargs: 其他浏览器启动参数
            
        Returns:
            Browser实例
        """
        browser_map = {
            "chromium": self.playwright.chromium,
            "firefox": self.playwright.firefox,
            "webkit": self.playwright.webkit,
        }
        
        if browser_type not in browser_map:
            raise ValueError(f"不支持的浏览器类型: {browser_type}")
        
        #获取浏览器引擎
        browser_launcher = browser_map[browser_type]
        
        launch_options = {
            "headless": headless,
            "slow_mo": slow_mo,
            "timeout": timeout,
            **kwargs
        }
        
        logger.info(f"启动浏览器: {browser_type}, 参数: {launch_options}")
        self._browser = browser_launcher.launch(**launch_options)
        
        return self._browser
    
    def close_browser(self):
        """关闭浏览器"""
        if self._browser:
            self._browser.close()
            self._browser = None
            logger.info("浏览器已关闭")

