# 项目结构说明

## 📁 目录结构详解

```
playwright_pytest_autoproject/
│
├── config/                          # 配置模块
│   ├── __init__.py                 # 模块初始化文件
│   └── settings.py                 # 项目配置文件（环境变量、URL、浏览器配置等）
│
├── data/                            # 测试数据目录
│   └── test_data.yaml              # YAML格式测试数据（支持JSON、Excel）
│
├── logs/                            # 日志文件目录（自动生成）
│   └── test_YYYYMMDD.log           # 按日期生成的日志文件
│
├── pages/                           # 页面对象模型（POM）目录
│   ├── __init__.py
│   ├── base_page.py                # 基础页面类（所有页面对象的父类）
│   ├── login_page.py               # 登录页面对象示例
│   └── home_page.py                # 首页页面对象示例
│
├── reports/                         # 测试报告目录（自动生成）
│   └── report.html                 # HTML测试报告
│
├── screenshots/                     # 截图目录（自动生成）
│   └── test_name_YYYYMMDD_HHMMSS.png  # 测试失败时的截图
│
├── tests/                           # 测试用例目录
│   ├── __init__.py
│   ├── test_login.py               # 登录功能测试用例
│   └── test_home.py                # 首页功能测试用例
│
├── utils/                           # 工具类目录
│   ├── __init__.py
│   ├── browser_manager.py          # 浏览器管理工具
│   ├── logger_config.py            # 日志配置工具
│   ├── data_loader.py              # 数据加载工具（YAML/JSON/Excel）
│   ├── assert_utils.py             # 断言工具类
│   └── wait_utils.py               # 等待工具类
│
├── conftest.py                      # Pytest全局配置文件（fixture定义）
├── pytest.ini                       # Pytest配置文件
├── requirements.txt                 # Python依赖包列表
├── .gitignore                       # Git忽略文件配置
├── .env.example                     # 环境变量示例文件
├── run_tests.py                     # 测试运行脚本
├── README.md                        # 项目说明文档
└── PROJECT_STRUCTURE.md             # 项目结构说明文档（本文件）
```

## 📝 各模块说明

### config/ - 配置模块
- **settings.py**: 集中管理所有配置项，支持环境变量覆盖
  - 基础URL配置
  - 浏览器配置（类型、无头模式、超时等）
  - 视口配置
  - 数据库配置（如需要）
  - API配置

### pages/ - 页面对象模型
- **base_page.py**: 提供所有页面对象的通用方法
  - 元素操作（点击、输入、获取文本等）
  - 页面导航
  - 等待和断言工具集成
  
- **具体页面对象**: 继承BasePage，封装特定页面的元素和操作
  - 元素选择器定义为类属性
  - 页面操作方法封装为类方法

### tests/ - 测试用例
- 使用Pytest框架编写测试用例
- 使用标记（markers）对测试进行分类
- 支持参数化测试
- 使用fixture进行测试前置和后置处理

### utils/ - 工具类
- **browser_manager.py**: 浏览器生命周期管理
- **logger_config.py**: 日志系统配置（控制台+文件）
- **data_loader.py**: 测试数据加载（支持YAML/JSON/Excel）
- **assert_utils.py**: 丰富的断言方法
- **wait_utils.py**: 各种等待策略

### data/ - 测试数据
- 测试数据与测试代码分离
- 支持YAML、JSON、Excel格式
- 通过DataLoader工具类加载

## 🔄 工作流程

1. **配置加载**: `config/settings.py` 加载配置，支持环境变量
2. **浏览器启动**: `conftest.py` 中的fixture启动浏览器
3. **页面对象**: 测试用例使用页面对象进行操作
4. **数据驱动**: 从`data/`目录加载测试数据
5. **日志记录**: 所有操作记录到`logs/`目录
6. **报告生成**: 测试结果生成到`reports/`目录
7. **失败截图**: 测试失败时自动截图到`screenshots/`目录

## 📦 扩展建议

### 添加新页面对象
1. 在`pages/`目录创建新的页面对象文件
2. 继承`BasePage`类
3. 定义页面元素选择器
4. 封装页面操作方法

### 添加新测试用例
1. 在`tests/`目录创建新的测试文件
2. 使用页面对象进行操作
3. 使用DataLoader加载测试数据
4. 添加适当的测试标记

### 添加新工具类
1. 在`utils/`目录创建新的工具文件
2. 实现通用功能
3. 在需要的地方导入使用

## 🎯 最佳实践

1. **页面对象模式**: 每个页面一个类，元素和操作封装在类中
2. **数据驱动**: 测试数据与代码分离，便于维护
3. **标记管理**: 使用标记对测试进行分类和筛选
4. **等待策略**: 使用显式等待，避免硬编码sleep
5. **日志记录**: 关键操作记录日志，便于调试
6. **错误处理**: 测试失败时自动截图和记录日志
7. **代码复用**: 通用功能封装为工具类或基类方法

