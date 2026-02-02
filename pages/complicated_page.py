"""
complicated-page页面对象
"""

from playwright.sync_api import Page, Locator
from loguru import logger
from pages.base_page import BasePage


class Complicated(BasePage):
    # 该页面上“Button”一组按钮（均为<a>，role=link，name=Button）
    BUTTON_NAME = "Button"

    def __init__(self,page):
        super().__init__(page)

    def get_buttons(self) -> Locator:
        """返回所有名为 Button 的按钮定位器列表（Locator）"""
        return self.page.get_by_role("link", name=self.BUTTON_NAME)

    def click_button(self, index: int = 0):
        """
        点击指定序号的 Button（默认第一个）

        Args:
            index: 第几个按钮（0-based）
        """
        buttons = self.get_buttons()
        target = buttons.nth(index)
        logger.info(f"点击第 {index} 个 Button")
        target.click()

    def scroll_by(self, delta_y):
        """
        按像素滚动页面
        
        Args:
            delta_y: 向下为正，向上为负（像素）
        """
        logger.info(f"滚动页面: delta_y={delta_y}")
        self.page.mouse.wheel(0, delta_y)

    def scroll_to_text(self, text: str):
        """滚动到包含指定文本的元素"""
        locator = self.page.get_by_text(text)
        locator.scroll_into_view_if_needed()