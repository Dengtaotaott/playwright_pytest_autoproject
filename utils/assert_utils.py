"""
断言工具类
"""
from playwright.sync_api import Page, expect
from loguru import logger
from typing import Any


class AssertUtils:
    """断言工具类"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def assert_url_contains(self, expected_text: str, timeout: int = 5000):
        """断言URL包含指定文本"""
        expect(self.page).to_have_url(f"*{expected_text}*", timeout=timeout)
        logger.debug(f"URL断言通过: 包含 '{expected_text}'")
    
    def assert_title_contains(self, expected_text: str, timeout: int = 5000):
        """断言标题包含指定文本"""
        expect(self.page).to_have_title(f"*{expected_text}*", timeout=timeout)
        logger.debug(f"标题断言通过: 包含 '{expected_text}'")
    
    def assert_element_visible(self, selector: str, timeout: int = 5000):
        """断言元素可见"""
        expect(self.page.locator(selector)).to_be_visible(timeout=timeout)
        logger.debug(f"元素可见断言通过: {selector}")
    
    def assert_element_text(self, selector: str, expected_text: str, timeout: int = 5000):
        """断言元素文本"""
        expect(self.page.locator(selector)).to_have_text(expected_text, timeout=timeout)
        logger.debug(f"元素文本断言通过: {selector} = '{expected_text}'")
    
    def assert_element_contains_text(self, selector: str, expected_text: str, timeout: int = 5000):
        """断言元素包含指定文本"""
        expect(self.page.locator(selector)).to_contain_text(expected_text, timeout=timeout)
        logger.debug(f"元素文本包含断言通过: {selector} 包含 '{expected_text}'")
    
    def assert_element_count(self, selector: str, expected_count: int, timeout: int = 5000):
        """断言元素数量"""
        expect(self.page.locator(selector)).to_have_count(expected_count, timeout=timeout)
        logger.debug(f"元素数量断言通过: {selector} = {expected_count}")
    
    def assert_element_enabled(self, selector: str, timeout: int = 5000):
        """断言元素可启用"""
        expect(self.page.locator(selector)).to_be_enabled(timeout=timeout)
        logger.debug(f"元素可启用断言通过: {selector}")
    
    def assert_element_disabled(self, selector: str, timeout: int = 5000):
        """断言元素禁用"""
        expect(self.page.locator(selector)).to_be_disabled(timeout=timeout)
        logger.debug(f"元素禁用断言通过: {selector}")
    
    def assert_value(self, selector: str, expected_value: Any, timeout: int = 5000):
        """断言元素值"""
        expect(self.page.locator(selector)).to_have_value(str(expected_value), timeout=timeout)
        logger.debug(f"元素值断言通过: {selector} = '{expected_value}'")

