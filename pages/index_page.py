"""
首页页面对象
"""

from playwright.sync_api import Page
from loguru import logger
from pages.base_page import BasePage
from config.settings import Settings

class IndexPage(BasePage):
    LINK_TEXT = "Big page with many elements"
    URL = Settings.BASE_URL

    def __init__(self, page):
        super().__init__(page)

    def openUrl(self):
        """打开首页"""
        self.navigate()
    
    def click_big_page_link(self):
        """
        点击 'Big page with many elements' 链接
        使用 Playwright 推荐的 get_by_text() 定位器方法
        """
        logger.info("点击 'Big page with many elements' 链接")
        # 使用 Playwright 推荐的定位器方法
        self.click(self.get_by_text(self.LINK_TEXT))
        self.page.wait_for_url("**/complicated-page")
        self.wait_utils.wait_for_load_state("networkidle")
    
    def get_big_page_link_locator(self):
        """
        获取 'Big page with many elements' 链接的定位器
        返回 Locator 对象，可以用于链式操作
        
        Returns:
            Locator对象
        """
        return self.get_by_text("Big page with many elements")