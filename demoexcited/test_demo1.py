import pytest
from playwright.sync_api import Page,expect
import re

def test_url(page:Page):
    page.goto("https://ultimateqa.com/automation")
    expect(page).to_have_title(re.compile("Automation Practice"))

if __name__ == "__main__":
    pytest.main(["-v","test_demo1.py"])