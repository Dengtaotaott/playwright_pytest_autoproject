# Playwright 定位器使用指南

本项目已集成 Playwright 官方推荐的定位器方法，提供更稳定、更易维护的元素定位方式。

## 🎯 为什么使用 Playwright 定位器？

### 优势

1. **自动等待和重试**：Playwright 定位器内置自动等待机制，无需手动添加等待
2. **更稳定**：基于语义化属性定位，不依赖易变的 CSS 选择器
3. **更易维护**：代码更易读，更接近用户视角
4. **更好的错误信息**：定位失败时提供更清晰的错误提示

## 📚 可用的定位器方法

### 1. `get_by_role()` - 根据角色定位（最推荐）

根据元素的 ARIA 角色和可访问名称定位。

```python
# 点击按钮
self.click(self.get_by_role("button", name="Submit"))

# 填充输入框
self.fill(self.get_by_role("textbox", name="Username"), "admin")

# 点击链接
self.click(self.get_by_role("link", name="Home"))

# 勾选复选框
self.check(self.get_by_role("checkbox", name="Remember me"))

# 选择单选按钮
self.click(self.get_by_role("radio", name="Option 1"))
```

**常用角色**：
- `button` - 按钮
- `textbox` - 文本输入框
- `link` - 链接
- `heading` - 标题 (h1-h6)
- `checkbox` - 复选框
- `radio` - 单选按钮
- `combobox` - 下拉框
- `listbox` - 列表
- `option` - 选项

### 2. `get_by_text()` - 根据文本定位

根据元素的可见文本内容定位。

```python
# 点击包含特定文本的元素
self.click(self.get_by_text("Click me"))

# 精确匹配文本
self.click(self.get_by_text("Submit", exact=True))

# 获取文本内容
text = self.get_text(self.get_by_text("Welcome"))
```

### 3. `get_by_label()` - 根据标签定位

根据表单控件的关联标签文本定位（最推荐用于表单元素）。

```python
# 填充输入框（通过标签）
self.fill(self.get_by_label("Username"), "admin")
self.fill(self.get_by_label("Password"), "password123")
self.fill(self.get_by_label("Email Address"), "test@example.com")
```

### 4. `get_by_placeholder()` - 根据占位符定位

根据输入框的占位符文本定位。

```python
# 通过占位符填充输入框
self.fill(self.get_by_placeholder("Enter your email"), "test@example.com")
self.fill(self.get_by_placeholder("Search..."), "keyword")
```

### 5. `get_by_alt_text()` - 根据 alt 文本定位

根据图片的 alt 属性定位（主要用于图片）。

```python
# 点击图片
self.click(self.get_by_alt_text("Company logo"))

# 检查图片是否存在
if self.is_visible(self.get_by_alt_text("Success icon")):
    print("Success icon is visible")
```

### 6. `get_by_title()` - 根据 title 属性定位

根据元素的 title 属性定位。

```python
# 点击带 title 属性的元素
self.click(self.get_by_title("Close dialog"))
self.click(self.get_by_title("Tooltip text"))
```

### 7. `get_by_test_id()` - 根据测试 ID 定位（推荐用于测试）

根据 `data-testid` 属性定位（最稳定，推荐在测试中使用）。

```python
# 点击带 test-id 的元素
self.click(self.get_by_test_id("submit-button"))
self.click(self.get_by_test_id("login-form"))

# 在 HTML 中需要添加 data-testid 属性
# <button data-testid="submit-button">Submit</button>
```

## 💡 使用示例

### 示例 1：登录表单

```python
class LoginPage(BasePage):
    def login(self, username: str, password: str):
        """使用 Playwright 定位器登录"""
        # 使用 get_by_label 定位表单字段（推荐）
        self.fill(self.get_by_label("Username"), username)
        self.fill(self.get_by_label("Password"), password)
        
        # 使用 get_by_role 定位按钮（推荐）
        self.click(self.get_by_role("button", name="Sign in"))
```

### 示例 2：导航菜单

```python
class NavigationPage(BasePage):
    def click_home_link(self):
        """点击首页链接"""
        # 使用 get_by_role 定位链接
        self.click(self.get_by_role("link", name="Home"))
    
    def click_about_link(self):
        """点击关于链接"""
        # 使用 get_by_text 定位链接
        self.click(self.get_by_text("About"))
```

### 示例 3：复杂表单

```python
class RegistrationPage(BasePage):
    def fill_registration_form(self, data: dict):
        """填写注册表单"""
        # 使用 get_by_label 定位所有表单字段
        self.fill(self.get_by_label("First Name"), data["first_name"])
        self.fill(self.get_by_label("Last Name"), data["last_name"])
        self.fill(self.get_by_label("Email"), data["email"])
        self.fill(self.get_by_placeholder("Password"), data["password"])
        
        # 使用 get_by_role 定位复选框
        self.check(self.get_by_role("checkbox", name="I agree to terms"))
        
        # 使用 get_by_role 定位提交按钮
        self.click(self.get_by_role("button", name="Register"))
```

### 示例 4：链式操作

```python
# Playwright 定位器支持链式操作
def test_complex_interaction(self, page):
    index_page = IndexPage(page)
    index_page.openUrl()
    
    # 获取定位器后可以链式调用
    locator = index_page.get_big_page_link_locator()
    locator.scroll_into_view_if_needed()
    locator.click()
    
    # 或者直接使用
    index_page.get_by_text("Big page with many elements").click()
```

## 🔄 从传统选择器迁移

### 旧方式（不推荐）

```python
# 使用 CSS 选择器
self.click("#submit-button")
self.fill("input[name='username']", "admin")
self.click("a[href='/home']")
```

### 新方式（推荐）

```python
# 使用 Playwright 定位器
self.click(self.get_by_test_id("submit-button"))
self.fill(self.get_by_label("Username"), "admin")
self.click(self.get_by_role("link", name="Home"))
```

## 📋 定位器优先级建议

1. **首选**：`get_by_test_id()` - 最稳定，专为测试设计
2. **次选**：`get_by_role()` - 语义化，稳定可靠
3. **表单元素**：`get_by_label()` - 最符合用户视角
4. **文本链接**：`get_by_text()` 或 `get_by_role("link")`
5. **最后选择**：传统 CSS/XPath 选择器（仅在必要时使用）

## ⚠️ 注意事项

1. **向后兼容**：项目仍支持传统选择器字符串，可以逐步迁移
2. **自动等待**：Playwright 定位器已内置自动等待，无需额外等待
3. **错误信息**：定位失败时，Playwright 会提供更详细的错误信息
4. **性能**：Playwright 定位器性能更好，因为使用了优化的查询机制

## 🔗 相关资源

- [Playwright 定位器官方文档](https://playwright.dev/python/docs/locators)
- [最佳实践指南](https://playwright.dev/python/docs/locators#best-practices)

