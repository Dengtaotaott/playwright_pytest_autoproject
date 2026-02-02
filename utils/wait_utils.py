"""
等待工具类
"""
from playwright.sync_api import Page, Locator
from loguru import logger
from typing import Callable, Optional


class WaitUtils:
    """等待工具类"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def wait_for_element(
        self,
        selector: str,
        timeout: int = 30000,
        state: str = "visible"
    ) -> Locator:
        """
        等待元素出现
        
        Args:
            selector: 元素选择器
            timeout: 超时时间（毫秒）
            state: 等待状态 (visible, hidden, attached, detached)
            
        Returns:
            Locator对象
        """
        logger.debug(f"等待元素: {selector}, 状态: {state}, 超时: {timeout}ms")
        locator = self.page.locator(selector)
        locator.wait_for(state=state, timeout=timeout)
        return locator
    
    def wait_for_url(
        self,
        url_pattern: str,
        timeout: int = 30000
    ):
        """
        等待URL匹配
        
        Args:
            url_pattern: URL模式（支持通配符）
            timeout: 超时时间（毫秒）
        """
        logger.debug(f"等待URL: {url_pattern}, 超时: {timeout}ms")
        self.page.wait_for_url(url_pattern, timeout=timeout)
    
    def wait_for_load_state(
        self,
        state: str = "load",
        timeout: int = 30000
    ):
        """
        等待页面加载状态
        
        Args:
            state: 加载状态 (load, domcontentloaded, networkidle)
            timeout: 超时时间（毫秒）
        """
        logger.debug(f"等待页面加载状态: {state}, 超时: {timeout}ms")
        self.page.wait_for_load_state(state, timeout=timeout)
    
    def wait_for_function(
        self,
        expression: str,
        timeout: int = 30000
    ):
        """
        等待JavaScript函数返回true
        
        Args:
            expression: JavaScript表达式
            timeout: 超时时间（毫秒）
        """
        logger.debug(f"等待函数: {expression}, 超时: {timeout}ms")
        self.page.wait_for_function(expression, timeout=timeout)
    
    def wait_for_condition(
        self,
        condition: Callable[[], bool],
        timeout: int = 30000,
        interval: int = 500
    ) -> bool:
        """
        等待自定义条件
        
        Args:
            condition: 条件函数
            timeout: 超时时间（毫秒）
            interval: 检查间隔（毫秒）
            
        Returns:
            是否满足条件
        """
        import time
        start_time = time.time()
        
        while (time.time() - start_time) * 1000 < timeout:
            if condition():
                logger.debug(f"条件满足，耗时: {(time.time() - start_time) * 1000:.0f}ms")
                return True
            time.sleep(interval / 1000)
        
        logger.warning(f"等待条件超时: {timeout}ms")
        return False

