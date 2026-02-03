"""
基础页面类 - 所有页面对象的基类
使用 Playwright 推荐的定位器方法
"""
from playwright.sync_api import Page, Locator
from loguru import logger
from typing import Optional, Union

from utils.assert_utils import AssertUtils
from utils.wait_utils import WaitUtils
from config.settings import Settings


class BasePage:
    """基础页面类 - 使用 Playwright 推荐的定位器方法"""
    
    def __init__(self, page: Page):
        self.page = page
        self.settings = Settings()
        self.assert_utils = AssertUtils(page)
        self.wait_utils = WaitUtils(page)
    
    # ==================== Playwright 推荐定位器方法 ====================
    
    def get_by_role(self, role: str, name: Optional[str] = None, **kwargs) -> Locator:
        """
        根据角色定位元素（推荐使用）
        
        Args:
            role: 角色名称 (button, textbox, link, heading, checkbox, radio, etc.)
            name: 可访问名称（可选）
            **kwargs: 其他选项 (checked, disabled, exact, expanded, included, level, pressed, selected)
            
        Returns:
            Locator对象
            
        Example:
            self.get_by_role("button", name="Sign in").click()
            self.get_by_role("textbox", name="Username").fill("admin")
        """
        return self.page.get_by_role(role, name=name, **kwargs)
    
    def get_by_text(self, text: str, exact: bool = False) -> Locator:
        """
        根据文本内容定位元素（推荐使用）
        
        Args:
            text: 文本内容
            exact: 是否精确匹配
            
        Returns:
            Locator对象
            
        Example:
            self.get_by_text("Welcome").click()
            self.get_by_text("Submit", exact=True).click()
        """
        return self.page.get_by_text(text, exact=exact)
    
    def get_by_label(self, text: str, exact: bool = False) -> Locator:
        """
        根据标签文本定位表单控件（推荐使用）
        
        Args:
            text: 标签文本
            exact: 是否精确匹配
            
        Returns:
            Locator对象
            
        Example:
            self.get_by_label("Username").fill("admin")
            self.get_by_label("Password").fill("password")
        """
        return self.page.get_by_label(text, exact=exact)
    
    def get_by_placeholder(self, text: str, exact: bool = False) -> Locator:
        """
        根据占位符定位输入框（推荐使用）
        
        Args:
            text: 占位符文本
            exact: 是否精确匹配
            
        Returns:
            Locator对象
            
        Example:
            self.get_by_placeholder("Enter your email").fill("test@example.com")
        """
        return self.page.get_by_placeholder(text, exact=exact)
    
    def get_by_alt_text(self, text: str, exact: bool = False) -> Locator:
        """
        根据 alt 文本定位元素（通常是图片）（推荐使用）
        
        Args:
            text: alt 文本
            exact: 是否精确匹配
            
        Returns:
            Locator对象
            
        Example:
            self.get_by_alt_text("Company logo").click()
        """
        return self.page.get_by_alt_text(text, exact=exact)
    
    def get_by_title(self, text: str, exact: bool = False) -> Locator:
        """
        根据 title 属性定位元素（推荐使用）
        
        Args:
            text: title 文本
            exact: 是否精确匹配
            
        Returns:
            Locator对象
            
        Example:
            self.get_by_title("Close dialog").click()
        """
        return self.page.get_by_title(text, exact=exact)
    
    def get_by_test_id(self, test_id: str) -> Locator:
        """
        根据 test-id 属性定位元素（推荐使用）
        默认使用 data-testid 属性，可在 playwright.config 中配置
        
        Args:
            test_id: test-id 值
            
        Returns:
            Locator对象
            
        Example:
            self.get_by_test_id("submit-button").click()
        """
        return self.page.get_by_test_id(test_id)
    
    def navigate(self, url: Optional[str] = None):
        """
        导航到指定URL
        
        Args:
            url: 目标URL，如果为None则使用页面的默认URL
        """
        if url is None:
            url = self.URL if hasattr(self, "URL") else self.settings.BASE_URL
        
        logger.info(f"导航到: {url}")
        # 使用 load 避免 networkidle 在资源多的页面等待过久（常超过 1 分钟）
        self.page.goto(url, wait_until="load")
    
    def get_title(self) -> str:
        """获取页面标题"""
        return self.page.title()
    
    def get_url(self) -> str:
        """获取当前URL"""
        return self.page.url
    
    def click(self, locator: Union[str, Locator], timeout: int = 30000):
        """
        点击元素
        
        Args:
            locator: 定位器（可以是字符串选择器或 Locator 对象）
            timeout: 超时时间（毫秒）
            
        Example:
            # 使用 Playwright 定位器（推荐）
            self.click(self.get_by_role("button", name="Submit"))
            self.click(self.get_by_text("Click me"))
            
            # 使用传统选择器（兼容旧代码）
            self.click("#submit-button")
        """
        if isinstance(locator, str):
            logger.debug(f"点击元素: {locator}")
            self.wait_utils.wait_for_element(locator, timeout=timeout)
            self.page.locator(locator).click(timeout=timeout)
        else:
            logger.debug(f"点击元素: {locator}")
            locator.click(timeout=timeout)
    
    def fill(self, locator: Union[str, Locator], value: str, timeout: int = 30000):
        """
        填充输入框
        
        Args:
            locator: 定位器（可以是字符串选择器或 Locator 对象）
            value: 输入值
            timeout: 超时时间（毫秒）
            
        Example:
            # 使用 Playwright 定位器（推荐）
            self.fill(self.get_by_label("Username"), "admin")
            self.fill(self.get_by_placeholder("Email"), "test@example.com")
            
            # 使用传统选择器
            self.fill("#username", "admin")
        """
        if isinstance(locator, str):
            logger.debug(f"填充输入框: {locator} = '{value}'")
            self.wait_utils.wait_for_element(locator, timeout=timeout)
            self.page.locator(locator).fill(value, timeout=timeout)
        else:
            logger.debug(f"填充输入框: {locator} = '{value}'")
            locator.fill(value, timeout=timeout)
    
    def type_text(self, locator: Union[str, Locator], text: str, delay: int = 100, timeout: int = 30000):
        """
        输入文本（带延迟，模拟真实输入）
        
        Args:
            locator: 定位器（可以是字符串选择器或 Locator 对象）
            text: 输入文本
            delay: 每个字符的延迟（毫秒）
            timeout: 超时时间（毫秒）
            
        Example:
            # 使用 Playwright 定位器（推荐）
            self.type_text(self.get_by_label("Password"), "secret123")
        """
        if isinstance(locator, str):
            logger.debug(f"输入文本: {locator} = '{text}'")
            self.wait_utils.wait_for_element(locator, timeout=timeout)
            self.page.locator(locator).type(text, delay=delay, timeout=timeout)
        else:
            logger.debug(f"输入文本: {locator} = '{text}'")
            locator.type(text, delay=delay, timeout=timeout)
    
    def get_text(self, locator: Union[str, Locator], timeout: int = 30000) -> str:
        """
        获取元素文本
        
        Args:
            locator: 定位器（可以是字符串选择器或 Locator 对象）
            timeout: 超时时间（毫秒）
            
        Returns:
            元素文本
            
        Example:
            # 使用 Playwright 定位器（推荐）
            text = self.get_text(self.get_by_text("Welcome"))
        """
        if isinstance(locator, str):
            self.wait_utils.wait_for_element(locator, timeout=timeout)
            text = self.page.locator(locator).inner_text(timeout=timeout)
            logger.debug(f"获取文本: {locator} = '{text}'")
        else:
            text = locator.inner_text(timeout=timeout)
            logger.debug(f"获取文本: {locator} = '{text}'")
        return text
    
    def get_value(self, selector: str, timeout: int = 30000) -> str:
        """
        获取元素值
        
        Args:
            selector: 元素选择器
            timeout: 超时时间（毫秒）
            
        Returns:
            元素值
        """
        self.wait_utils.wait_for_element(selector, timeout=timeout)
        value = self.page.locator(selector).input_value(timeout=timeout)
        logger.debug(f"获取值: {selector} = '{value}'")
        return value
    
    def is_visible(self, locator: Union[str, Locator], timeout: int = 5000) -> bool:
        """
        检查元素是否可见
        
        Args:
            locator: 定位器（可以是字符串选择器或 Locator 对象）
            timeout: 超时时间（毫秒）
            
        Returns:
            是否可见
            
        Example:
            # 使用 Playwright 定位器（推荐）
            if self.is_visible(self.get_by_role("button", name="Submit")):
                self.click(self.get_by_role("button", name="Submit"))
        """
        try:
            if isinstance(locator, str):
                self.page.locator(locator).wait_for(state="visible", timeout=timeout)
            else:
                locator.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False
    
    def is_enabled(self, selector: str, timeout: int = 5000) -> bool:
        """
        检查元素是否启用
        
        Args:
            selector: 元素选择器
            timeout: 超时时间（毫秒）
            
        Returns:
            是否启用
        """
        try:
            locator = self.page.locator(selector)
            return locator.is_enabled(timeout=timeout)
        except:
            return False
    
    def select_option(self, selector: str, value: str, timeout: int = 30000):
        """
        选择下拉框选项
        
        Args:
            selector: 下拉框选择器
            value: 选项值
            timeout: 超时时间（毫秒）
        """
        logger.debug(f"选择选项: {selector} = '{value}'")
        self.wait_utils.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).select_option(value, timeout=timeout)
    
    def check(self, selector: str, timeout: int = 30000):
        """
        勾选复选框
        
        Args:
            selector: 复选框选择器
            timeout: 超时时间（毫秒）
        """
        logger.debug(f"勾选复选框: {selector}")
        self.wait_utils.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).check(timeout=timeout)
    
    def uncheck(self, selector: str, timeout: int = 30000):
        """
        取消勾选复选框
        
        Args:
            selector: 复选框选择器
            timeout: 超时时间（毫秒）
        """
        logger.debug(f"取消勾选复选框: {selector}")
        self.wait_utils.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).uncheck(timeout=timeout)
    
    def hover(self, selector: str, timeout: int = 30000):
        """
        鼠标悬停
        
        Args:
            selector: 元素选择器
            timeout: 超时时间（毫秒）
        """
        logger.debug(f"鼠标悬停: {selector}")
        self.wait_utils.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).hover(timeout=timeout)
    
    def screenshot(self, path: str, full_page: bool = True):
        """
        截图
        
        Args:
            path: 截图保存路径
            full_page: 是否截取整个页面
        """
        logger.debug(f"截图保存到: {path}")
        self.page.screenshot(path=path, full_page=full_page)
    
    def wait_for_selector(self, selector: str, timeout: int = 30000) -> Locator:
        """
        等待选择器出现
        
        Args:
            selector: 元素选择器
            timeout: 超时时间（毫秒）
            
        Returns:
            Locator对象
        """
        return self.wait_utils.wait_for_element(selector, timeout=timeout)
    
    def scroll_to_element(self, selector: str, timeout: int = 30000):
        """
        滚动到元素
        
        Args:
            selector: 元素选择器
            timeout: 超时时间（毫秒）
        """
        logger.debug(f"滚动到元素: {selector}")
        self.wait_utils.wait_for_element(selector, timeout=timeout)
        self.page.locator(selector).scroll_into_view_if_needed(timeout=timeout)
    
    def reload(self, wait_until: str = "networkidle"):
        """
        重新加载页面
        
        Args:
            wait_until: 等待条件 (load, domcontentloaded, networkidle)
        """
        logger.debug("重新加载页面")
        self.page.reload(wait_until=wait_until)
    
    def go_back(self):
        """返回上一页"""
        logger.debug("返回上一页")
        self.page.go_back()
    
    def go_forward(self):
        """前进下一页"""
        logger.debug("前进下一页")
        self.page.go_forward()

