from playwright.sync_api import Page
from loguru import logger

from pages.index_page import IndexPage
from pages.complicated_page import Complicated
from config.settings import Settings
from pages.index_page import IndexPage
import time
import pytest

class TestComplicatedPage:
    @pytest.mark.skip(reason="跳过测试")
    def test_click_button_from_home(self, page: Page):
        """
        流程：
        1) 打开首页（BASE_URL）
        2) 点击 'Big page with many elements' 链接跳转到 complicated-page
        3) 在目标页点击第一个 Button
        """
        # 1) 打开首页
        index_page = IndexPage(page)
        index_page.openUrl()

        # 2) 跳转到 complicated-page
        index_page.click_big_page_link()
        dest_url = index_page.get_url()
        logger.info(f"跳转后的URL: {dest_url}")
        assert "complicated-page" in dest_url.lower(), "应跳转到 complicated-page 页面"

        # 3) 点击目标页的第一个 Button
        complicated_page = Complicated(page)
        complicated_page.click_button(0)
        page.pause()

        # 可选校验：点击后仍留在当前页（无跳转预期时可不判断）
        current_url = complicated_page.get_url()
        logger.info(f"点击按钮后URL: {current_url}")
        assert "complicated-page" in current_url.lower(), "点击后不应离开 complicated-page 页面"

    # @pytest.mark.skip(reason="跳过测试")
    def test_scroll_fill(self,page):
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
        complicated_page_test=Complicated(page)
        complicated_page_test.scroll_by(1000)
        time.sleep(5)