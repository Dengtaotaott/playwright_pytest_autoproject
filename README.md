# Playwright + Pytest + POM 自动化测试项目

这是一个基于 Playwright、Pytest 和 Page Object Model (POM) 设计模式的大型自动化测试项目。

## 📋 项目结构

```
playwright_pytest_autoproject/
├── config/                 # 配置文件目录
│   ├── __init__.py
│   └── settings.py        # 项目配置
├── data/                  # 测试数据目录
│   └── test_data.yaml     # 测试数据文件
├── logs/                  # 日志文件目录（自动生成）
├── pages/                 # 页面对象目录
│   ├── __init__.py
│   ├── base_page.py       # 基础页面类
│   ├── login_page.py      # 登录页面对象
│   └── home_page.py       # 首页页面对象
├── reports/               # 测试报告目录（自动生成）
├── screenshots/           # 截图目录（自动生成）
├── tests/                 # 测试用例目录
│   ├── __init__.py
│   ├── test_login.py      # 登录测试用例
│   └── test_home.py       # 首页测试用例
├── utils/                 # 工具类目录
│   ├── __init__.py
│   ├── browser_manager.py # 浏览器管理
│   ├── logger_config.py   # 日志配置
│   ├── data_loader.py     # 数据加载
│   ├── assert_utils.py    # 断言工具
│   └── wait_utils.py      # 等待工具
├── conftest.py            # Pytest配置文件
├── pytest.ini             # Pytest配置
├── requirements.txt       # Python依赖
├── .gitignore            # Git忽略文件
└── README.md             # 项目说明文档
```

## 🚀 快速开始

### 1. 环境要求

- Python 3.8+
- pip

### 2. 安装依赖

```bash
# 安装Python依赖
pip install -r requirements.txt

# 安装Playwright浏览器
playwright install
```

### 3. 配置环境变量

创建 `.env` 文件（可选，或直接修改 `config/settings.py`）：

```env
BASE_URL=https://example.com
BROWSER=chromium
HEADLESS=False
VIEWPORT_WIDTH=1920
VIEWPORT_HEIGHT=1080
```

### 4. 运行测试

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
pytest -m smoke
pytest -m login

# 并行运行测试
pytest -n auto

# 生成HTML报告
pytest --html=reports/report.html --self-contained-html
```

## 📝 使用说明

### 页面对象模型 (POM)

所有页面对象继承自 `BasePage` 类，提供通用的页面操作方法。

**示例：创建新页面对象**

```python
from pages.base_page import BasePage
from playwright.sync_api import Page

class MyPage(BasePage):
    URL = "https://example.com/my-page"
    
    # 页面元素选择器
    BUTTON = "#my-button"
    INPUT = "#my-input"
    
    def __init__(self, page: Page):
        super().__init__(page)
    
    def click_my_button(self):
        """点击按钮"""
        self.click(self.BUTTON)
```

### 测试用例编写

**示例：编写测试用例**

```python
import pytest
from pages.my_page import MyPage

@pytest.mark.smoke
class TestMyFeature:
    def test_my_feature(self, page):
        my_page = MyPage(page)
        my_page.navigate()
        my_page.click_my_button()
        # 添加断言
```

### 测试数据管理

测试数据存储在 `data/test_data.yaml` 文件中，使用 `DataLoader` 工具类加载：

```python
from utils.data_loader import DataLoader

test_data = DataLoader.get_test_data("test_name")
```

### 标记 (Markers)

项目定义了以下测试标记：

- `@pytest.mark.smoke` - 冒烟测试
- `@pytest.mark.regression` - 回归测试
- `@pytest.mark.login` - 登录相关测试
- `@pytest.mark.api` - API测试
- `@pytest.mark.ui` - UI测试
- `@pytest.mark.slow` - 慢速测试

## 🔧 配置说明

### pytest.ini

主要配置项：
- `testpaths`: 测试文件目录
- `addopts`: 默认命令行选项
- `markers`: 测试标记定义
- `timeout`: 测试超时时间

### config/settings.py

项目配置项：
- `BASE_URL`: 基础URL
- `BROWSER`: 浏览器类型（chromium/firefox/webkit）
- `HEADLESS`: 是否无头模式
- `VIEWPORT_WIDTH/HEIGHT`: 视口大小

## 📊 报告和日志

### 测试报告

- HTML报告：`reports/report.html`
- 测试失败时自动截图：`screenshots/`

### 日志

- 日志文件：`logs/test_YYYYMMDD.log`
- 控制台输出：实时显示测试进度

## 🛠️ 工具类说明

### BrowserManager

浏览器管理工具，负责浏览器的启动和关闭。

### DataLoader

数据加载工具，支持 YAML、JSON、Excel 格式的测试数据。

### AssertUtils

断言工具类，提供丰富的断言方法。

### WaitUtils

等待工具类，提供各种等待策略。

## 📚 最佳实践

1. **页面对象模式**：每个页面创建一个页面对象类
2. **数据驱动**：测试数据与测试代码分离
3. **标记管理**：合理使用测试标记进行分类
4. **等待策略**：使用显式等待，避免硬编码等待
5. **日志记录**：关键操作记录日志
6. **错误处理**：测试失败时自动截图

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 📄 许可证

MIT License

## 📞 联系方式

如有问题，请提交 Issue。

