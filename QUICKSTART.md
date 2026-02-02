# 快速开始指南

## 🚀 5分钟快速上手

### 第一步：安装依赖

```bash
# 1. 安装Python依赖包
pip install -r requirements.txt

# 2. 安装Playwright浏览器
playwright install
```

### 第二步：配置项目

1. 复制环境变量示例文件（可选）：
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

2. 编辑 `.env` 文件或直接修改 `config/settings.py`，设置你的测试环境URL：
```python
BASE_URL = "https://your-test-site.com"
```

### 第三步：运行测试

```bash
# 方式1：使用pytest直接运行
pytest

# 方式2：使用运行脚本
python run_tests.py

# 方式3：运行指定测试
pytest tests/test_login.py

# 方式4：运行带标记的测试
pytest -m smoke
```

## 📋 常用命令

### 运行测试

```bash
# 运行所有测试
pytest

# 运行指定测试文件
pytest tests/test_login.py

# 运行指定测试类
pytest tests/test_login.py::TestLogin

# 运行指定测试方法
pytest tests/test_login.py::TestLogin::test_successful_login

# 运行带标记的测试
pytest -m smoke          # 冒烟测试
pytest -m login          # 登录相关测试
pytest -m regression     # 回归测试

# 并行运行测试（需要pytest-xdist）
pytest -n auto

# 失败重试
pytest --reruns 2 --reruns-delay 1
```

### 生成报告

```bash
# 生成HTML报告
pytest --html=reports/report.html --self-contained-html

# 生成Allure报告（需要安装allure-pytest）
pytest --alluredir=allure-results
allure serve allure-results
```

### 调试模式

```bash
# 显示详细输出
pytest -v -s

# 显示打印语句
pytest -s

# 只运行失败的测试
pytest --lf

# 运行上次失败的测试，然后运行剩余的
pytest --ff
```

## 📝 编写你的第一个测试

### 1. 创建页面对象

在 `pages/` 目录创建 `my_page.py`：

```python
from pages.base_page import BasePage
from playwright.sync_api import Page

class MyPage(BasePage):
    URL = "https://example.com/my-page"
    
    # 定义页面元素
    BUTTON = "#my-button"
    INPUT = "#my-input"
    TITLE = "h1"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def click_button(self):
        """点击按钮"""
        self.click(self.BUTTON)
    
    def fill_input(self, text: str):
        """填充输入框"""
        self.fill(self.INPUT, text)
    
    def get_title_text(self) -> str:
        """获取标题文本"""
        return self.get_text(self.TITLE)
```

### 2. 创建测试用例

在 `tests/` 目录创建 `test_my_feature.py`：

```python
import pytest
from pages.my_page import MyPage

@pytest.mark.smoke
class TestMyFeature:
    """我的功能测试"""
    
    def test_my_feature(self, page):
        """测试我的功能"""
        my_page = MyPage(page)
        my_page.navigate()
        
        # 执行操作
        my_page.fill_input("测试文本")
        my_page.click_button()
        
        # 断言
        title = my_page.get_title_text()
        assert "成功" in title
```

### 3. 添加测试数据（可选）

在 `data/test_data.yaml` 中添加：

```yaml
test_my_feature:
  input_text: "测试文本"
  expected_title: "成功"
```

在测试中使用：

```python
from utils.data_loader import DataLoader

def test_my_feature(self, page):
    test_data = DataLoader.get_test_data("test_my_feature")
    input_text = test_data.get("input_text")
    expected_title = test_data.get("expected_title")
    
    my_page = MyPage(page)
    my_page.navigate()
    my_page.fill_input(input_text)
    # ...
```

## 🎯 测试标记使用

项目预定义了以下标记：

- `@pytest.mark.smoke` - 冒烟测试
- `@pytest.mark.regression` - 回归测试
- `@pytest.mark.login` - 登录相关
- `@pytest.mark.api` - API测试
- `@pytest.mark.ui` - UI测试
- `@pytest.mark.slow` - 慢速测试

使用示例：

```python
@pytest.mark.smoke
def test_quick_check(page):
    """快速检查测试"""
    pass

@pytest.mark.regression
@pytest.mark.slow
def test_comprehensive(page):
    """全面回归测试"""
    pass
```

## 🔧 配置说明

### 浏览器配置

在 `config/settings.py` 或 `.env` 文件中：

```python
BROWSER = "chromium"  # chromium, firefox, webkit
HEADLESS = False      # True为无头模式
VIEWPORT_WIDTH = 1920
VIEWPORT_HEIGHT = 1080
```

### 超时配置

```python
BROWSER_TIMEOUT = 30      # 浏览器超时（秒）
IMPLICIT_WAIT = 10        # 隐式等待（秒）
EXPLICIT_WAIT = 30        # 显式等待（秒）
```

## 📊 查看结果

### 测试报告

- HTML报告：`reports/report.html`
- 打开报告查看详细测试结果

### 日志文件

- 日志位置：`logs/test_YYYYMMDD.log`
- 包含详细的执行日志和错误信息

### 失败截图

- 截图位置：`screenshots/`
- 测试失败时自动截图

## ❓ 常见问题

### Q: 如何切换浏览器？

A: 修改 `config/settings.py` 中的 `BROWSER` 配置，或设置环境变量 `BROWSER=firefox`

### Q: 如何运行特定环境的测试？

A: 使用不同的 `.env` 文件，或修改 `config/settings.py` 中的 `BASE_URL`

### Q: 测试失败时如何调试？

A: 
1. 查看 `logs/` 目录下的日志文件
2. 查看 `screenshots/` 目录下的失败截图
3. 使用 `pytest -v -s` 查看详细输出
4. 在代码中添加 `page.pause()` 进行交互式调试

### Q: 如何添加新的测试标记？

A: 在 `pytest.ini` 文件的 `markers` 部分添加新标记

## 📚 下一步

- 查看 [README.md](README.md) 了解完整文档
- 查看 [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) 了解项目结构
- 参考示例测试用例学习最佳实践

