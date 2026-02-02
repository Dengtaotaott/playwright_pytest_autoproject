"""
首页功能测试用例
"""
import time

import pytest
from playwright.sync_api import Page
from loguru import logger
from pages.index_page import IndexPage
from config.settings import Settings


@pytest.mark.ui
@pytest.mark.smoke
class TestIndex:
    """首页测试类"""
    
    def test_navigate_directly(self, page: Page):
        """测试直接使用navigate方法打开首页"""
        index_page = IndexPage(page)
        # 打开首页
        # 直接调用navigate，会自动使用IndexPage.URL（即Settings.BASE_URL）
        index_page.navigate()
        
        # 验证URL
        assert Settings.BASE_URL in index_page.get_url()
        logger.info("直接使用navigate方法打开首页成功")
    
    @pytest.mark.skip(reason="跳过测试")
    def test_click_big_page_link(self, page: Page):
        """测试点击 'Big page with many elements' 链接（使用 Playwright 定位器）"""
        index_page = IndexPage(page)
        
        # 打开首页
        index_page.openUrl()
        
        # 验证链接存在（使用 Playwright 定位器）
        big_page_locator = index_page.get_big_page_link_locator()
        assert index_page.is_visible(big_page_locator), "链接应该可见"
        
        # 点击链接（内部使用 get_by_text() 定位器）
        index_page.click_big_page_link()
        
        # 验证已跳转到新页面
        current_url = index_page.get_url()
        logger.info(f"点击链接后的URL: {current_url}")
        assert "complicated-page" in current_url.lower(), "应该跳转到 complicated-page 页面"

