# Playwright 元素定位方法指南

## 一、推荐的定位方法（Playwright 官方推荐）

### 1. `get_by_role()` - 根据角色定位（最推荐）

*   根据元素的 ARIA 角色和可访问名称定位
*   参数：
    *   `role`: 角色名称（见下方完整角色列表）
    *   `name`: 可访问名称（可选，用于精确匹配）
    *   `checked`: 是否选中（用于 checkbox, radio, switch）
    *   `disabled`: 是否禁用
    *   `expanded`: 是否展开（用于 combobox, menubar 等）
    *   `level`: 标题级别（1-6，用于 heading）
    *   `pressed`: 是否按下（用于 button）
    *   `selected`: 是否选中（用于 option, tab）
    *   `value`: 当前值（用于 range 类型）

#### 完整角色列表（按类别）

**1.1 按钮类角色**

```python
# button - 按钮（最常用）
page.get_by_role("button", name="Submit")
page.get_by_role("button", name="Sign in")
page.get_by_role("button", pressed=True)  # 切换按钮

# switch - 开关按钮
page.get_by_role("switch", name="Enable notifications")
page.get_by_role("switch", checked=True)
```

**1.2 表单控件角色**

```python
# textbox - 文本输入框
page.get_by_role("textbox", name="Username")
page.get_by_role("textbox", name="Email")
page.get_by_role("textbox", name="Message")

# checkbox - 复选框
page.get_by_role("checkbox", name="Remember me")
page.get_by_role("checkbox", checked=True)
page.get_by_role("checkbox", checked=False)

# radio - 单选按钮
page.get_by_role("radio", name="Option 1")
page.get_by_role("radio", name="Male", checked=True)

# combobox - 下拉框/组合框
page.get_by_role("combobox", name="Country")
page.get_by_role("combobox", name="Select option", expanded=True)

# searchbox - 搜索框
page.get_by_role("searchbox", name="Search")

# spinbutton - 数字输入框（带增减按钮）
page.get_by_role("spinbutton", name="Quantity")

# slider - 滑块
page.get_by_role("slider", name="Volume")
page.get_by_role("slider", value="50")

# option - 选项（下拉框中的选项）
page.get_by_role("option", name="China")

# menuitem - 菜单项
page.get_by_role("menuitem", name="Save")
page.get_by_role("menuitem", name="Delete")

# menuitemcheckbox - 菜单复选框项
page.get_by_role("menuitemcheckbox", name="Show grid")

# menuitemradio - 菜单单选项
page.get_by_role("menuitemradio", name="View mode")
```

**1.3 链接和导航角色**

```python
# link - 链接（最常用）
page.get_by_role("link", name="Home")
page.get_by_role("link", name="About")
page.get_by_role("link", name="Contact Us")

# navigation - 导航区域
page.get_by_role("navigation", name="Main menu")

# menubar - 菜单栏
page.get_by_role("menubar", name="File menu")

# menu - 菜单
page.get_by_role("menu", name="Context menu")

# tab - 标签页
page.get_by_role("tab", name="Settings")
page.get_by_role("tab", selected=True)

# tablist - 标签页列表
page.get_by_role("tablist", name="Tabs")

# tabpanel - 标签页面板
page.get_by_role("tabpanel", name="General")
```

**1.4 标题和文本角色**

```python
# heading - 标题（h1-h6）
page.get_by_role("heading", name="Welcome", level=1)
page.get_by_role("heading", name="Introduction", level=2)
page.get_by_role("heading", name="Details", level=3)

# paragraph - 段落
page.get_by_role("paragraph", name="Description text")

# article - 文章
page.get_by_role("article", name="Blog post")

# note - 注释/提示
page.get_by_role("note", name="Help text")
```

**1.5 列表角色**

```python
# list - 列表
page.get_by_role("list", name="Items")

# listitem - 列表项
page.get_by_role("listitem", name="Item 1")

# listbox - 列表框
page.get_by_role("listbox", name="Options")
```

**1.6 表格角色**

```python
# table - 表格
page.get_by_role("table", name="User data")

# row - 表格行
page.get_by_role("row", name="User 1")

# rowheader - 行标题
page.get_by_role("rowheader", name="Name")

# columnheader - 列标题
page.get_by_role("columnheader", name="Email")

# cell - 表格单元格
page.get_by_role("cell", name="John Doe")

# gridcell - 网格单元格
page.get_by_role("gridcell", name="Value")
```

**1.7 区域和容器角色**

```python
# banner - 横幅/页眉
page.get_by_role("banner", name="Site header")

# complementary - 补充内容（侧边栏）
page.get_by_role("complementary", name="Sidebar")

# contentinfo - 内容信息（页脚）
page.get_by_role("contentinfo", name="Footer")

# main - 主要内容区域
page.get_by_role("main", name="Main content")

# region - 区域
page.get_by_role("region", name="Content area")

# search - 搜索区域
page.get_by_role("search", name="Search section")

# form - 表单
page.get_by_role("form", name="Login form")

# group - 分组
page.get_by_role("group", name="Form fields")

# dialog - 对话框
page.get_by_role("dialog", name="Confirm")

# alertdialog - 警告对话框
page.get_by_role("alertdialog", name="Warning")

# alert - 警告提示
page.get_by_role("alert", name="Error message")

# status - 状态栏
page.get_by_role("status", name="Loading status")

# timer - 计时器
page.get_by_role("timer", name="Countdown")

# log - 日志
page.get_by_role("log", name="Activity log")

# marquee - 滚动文本
page.get_by_role("marquee", name="News ticker")
```

**1.8 图片和媒体角色**

```python
# img - 图片
page.get_by_role("img", name="Company logo")

# figure - 图形/图表
page.get_by_role("figure", name="Chart")
```

**1.9 其他角色**

```python
# application - 应用程序
page.get_by_role("application", name="App")

# document - 文档
page.get_by_role("document", name="PDF viewer")

# feed - 信息流
page.get_by_role("feed", name="News feed")

# math - 数学公式
page.get_by_role("math", name="Equation")

# presentation - 演示内容
page.get_by_role("presentation", name="Diagram")

# separator - 分隔符
page.get_by_role("separator", name="Divider")

# scrollbar - 滚动条
page.get_by_role("scrollbar", name="Vertical scrollbar")

# tooltip - 工具提示
page.get_by_role("tooltip", name="Help text")

# tree - 树形结构
page.get_by_role("tree", name="File tree")

# treeitem - 树形项
page.get_by_role("treeitem", name="Folder")

# grid - 网格
page.get_by_role("grid", name="Data grid")

# rowgroup - 行组
page.get_by_role("rowgroup", name="Table body")

# columnheader - 列标题
page.get_by_role("columnheader", name="Name column")

# definition - 定义
page.get_by_role("definition", name="Term definition")

# term - 术语
page.get_by_role("term", name="Technical term")
```

#### 常用角色快速参考

```python
# 最常用的角色（按使用频率排序）
page.get_by_role("button", name="Submit")        # 按钮
page.get_by_role("link", name="Home")           # 链接
page.get_by_role("textbox", name="Username")    # 输入框
page.get_by_role("checkbox", name="Remember")   # 复选框
page.get_by_role("radio", name="Option")        # 单选按钮
page.get_by_role("heading", name="Title")       # 标题
page.get_by_role("combobox", name="Country")    # 下拉框
page.get_by_role("dialog", name="Confirm")      # 对话框
page.get_by_role("tab", name="Settings")        # 标签页
page.get_by_role("menuitem", name="Save")       # 菜单项
```

### 2. `get_by_text()` - 根据文本内容定位

*   根据元素的可见文本内容定位
*   参数：
    *   `text`: 文本内容（字符串或正则表达式）
    *   `exact`: 是否精确匹配（默认 False）

```python
# 模糊匹配
page.get_by_text("Click me")
page.get_by_text("Welcome")

# 精确匹配
page.get_by_text("Submit", exact=True)

# 正则表达式匹配
page.get_by_text(re.compile(r"Welcome, \w+"))
```

### 3. `get_by_label()` - 根据标签定位（表单元素推荐）

*   根据表单控件的关联标签文本定位
*   参数：
    *   `text`: 标签文本
    *   `exact`: 是否精确匹配

```python
page.get_by_label("Username")
page.get_by_label("Password")
page.get_by_label("Email Address")
page.get_by_label("Remember me", exact=True)
```

### 4. `get_by_placeholder()` - 根据占位符定位

*   根据输入框的占位符文本定位
*   参数：
    *   `text`: 占位符文本
    *   `exact`: 是否精确匹配

```python
page.get_by_placeholder("Enter your email")
page.get_by_placeholder("Search...")
page.get_by_placeholder("Password", exact=True)
```

### 5. `get_by_alt_text()` - 根据 alt 文本定位

*   根据图片的 alt 属性定位（主要用于图片）
*   参数：
    *   `text`: alt 文本
    *   `exact`: 是否精确匹配

```python
page.get_by_alt_text("Company logo")
page.get_by_alt_text("User avatar")
page.get_by_alt_text("Success icon", exact=True)
```

### 6. `get_by_title()` - 根据 title 属性定位

*   根据元素的 title 属性定位
*   参数：
    *   `text`: title 文本
    *   `exact`: 是否精确匹配

```python
page.get_by_title("Close dialog")
page.get_by_title("Tooltip text")
page.get_by_title("Help", exact=True)
```

### 7. `get_by_test_id()` - 根据测试 ID 定位（最稳定）

*   根据 `data-testid` 属性定位（最稳定，推荐用于测试）
*   参数：
    *   `test_id`: test-id 值
*   注意：需要在 HTML 中添加 `data-testid` 属性

```python
# HTML: <button data-testid="submit-button">Submit</button>
page.get_by_test_id("submit-button")

# HTML: <input data-testid="username-input" />
page.get_by_test_id("username-input")
```

## 二、传统定位方法（通过属性定位）

### 8. 通过 ID 定位

*   使用 CSS 选择器通过 ID 定位
*   语法：`#id_name`

```python
# HTML: <button id="submit-btn">Submit</button>
page.locator("#submit-btn")
page.locator("#username")
page.locator("#password-input")
```

### 9. 通过 name 属性定位

*   使用 CSS 选择器通过 name 属性定位
*   语法：`[name="name_value"]`

```python
# HTML: <input name="username" />
page.locator("[name='username']")
page.locator("input[name='username']")  # 更具体
page.locator("[name='email']")
```

### 10. 通过 class 定位

*   使用 CSS 选择器通过 class 定位
*   语法：`.class_name`

```python
# HTML: <button class="btn btn-primary">Submit</button>
page.locator(".btn")
page.locator(".btn-primary")
page.locator(".btn.btn-primary")  # 多个class
```

### 11. 通过标签名定位

*   直接使用 HTML 标签名定位

```python
page.locator("button")
page.locator("input")
page.locator("a")
page.locator("div")
```

### 12. 通过属性定位（通用方法）

*   使用 CSS 属性选择器定位
*   语法：`[attribute="value"]`

```python
# 通过 type 属性
page.locator("[type='submit']")
page.locator("input[type='text']")

# 通过 value 属性
page.locator("[value='Submit']")

# 通过 href 属性
page.locator("[href='/home']")
page.locator("a[href*='complicated']")  # 包含特定文本

# 通过 data 属性
page.locator("[data-id='123']")
page.locator("[data-action='submit']")

# 通过 aria-label 属性
page.locator("[aria-label='Close']")

# 通过 title 属性
page.locator("[title='Tooltip']")
```

### 13. 组合选择器定位

*   组合多个选择器进行精确定位

```python
# 标签 + ID
page.locator("button#submit-btn")

# 标签 + class
page.locator("button.btn-primary")

# 标签 + 属性
page.locator("input[type='text'][name='username']")

# 父子关系
page.locator("div.container button")
page.locator("form > input")

# 后代关系
page.locator("div.container .btn")
```

## 三、XPath 定位方法

### 14. 基本 XPath 定位

*   使用 XPath 表达式定位元素

```python
# 通过标签和属性
page.locator("//button[@id='submit-btn']")
page.locator("//input[@name='username']")
page.locator("//a[@href='/home']")

# 通过文本内容
page.locator("//button[text()='Submit']")
page.locator("//a[contains(text(), 'Click')]")

# 通过部分属性值
page.locator("//a[contains(@href, 'complicated')]")
page.locator("//input[starts-with(@name, 'user')]")
```

### 15. XPath 高级定位

*   使用 XPath 轴和函数进行复杂定位

```python
# 父元素
page.locator("//input[@name='username']/..")

# 兄弟元素
page.locator("//button[@id='btn1']/following-sibling::button")

# 祖先元素
page.locator("//span[text()='Text']/ancestor::div[@class='container']")

# 使用位置
page.locator("//button[1]")  # 第一个button
page.locator("//button[last()]")  # 最后一个button
page.locator("//div[@class='item'][2]")  # 第二个item
```

## 四、如何获取元素的属性值

### 16. `get_attribute()` - 获取属性值

*   获取元素的指定属性值
*   参数：
    *   `name`: 属性名称
    *   `timeout`: 超时时间
*   返回：属性值字符串或 `None`

```python
# 获取 ID
element_id = page.locator("button").get_attribute("id")
print(f"元素ID: {element_id}")

# 获取 name
element_name = page.locator("input").get_attribute("name")
print(f"元素name: {element_name}")

# 获取 class
element_class = page.locator("button").get_attribute("class")
print(f"元素class: {element_class}")

# 获取 href
link_href = page.locator("a").get_attribute("href")
print(f"链接地址: {link_href}")

# 获取 value
input_value = page.locator("input").get_attribute("value")
print(f"输入值: {input_value}")

# 获取 data 属性
test_id = page.locator("button").get_attribute("data-testid")
print(f"测试ID: {test_id}")

# 获取所有属性（通过 evaluate）
all_attrs = page.locator("button").evaluate("""
    element => {
        const attrs = {};
        for (let attr of element.attributes) {
            attrs[attr.name] = attr.value;
        }
        return attrs;
    }
""")
print(f"所有属性: {all_attrs}")
```

### 17. 获取元素的多个属性

*   一次性获取元素的多个属性

```python
# 方法1：多次调用 get_attribute
button = page.locator("button")
button_id = button.get_attribute("id")
button_class = button.get_attribute("class")
button_name = button.get_attribute("name")

# 方法2：使用 evaluate 获取所有属性
def get_all_attributes(locator):
    """获取元素的所有属性"""
    return locator.evaluate("""
        element => {
            const attrs = {};
            for (let attr of element.attributes) {
                attrs[attr.name] = attr.value;
            }
            return attrs;
        }
    """)

attrs = get_all_attributes(page.locator("button"))
print(f"ID: {attrs.get('id')}")
print(f"Class: {attrs.get('class')}")
print(f"Name: {attrs.get('name')}")
```

## 五、定位器的组合和过滤

### 18. 链式定位

*   在已定位的元素内继续定位子元素

```python
# 在容器内定位按钮
container = page.locator(".container")
button = container.locator("button")
button.click()

# 在表单内定位输入框
form = page.locator("form")
username_input = form.locator("[name='username']")
password_input = form.locator("[name='password']")
```

### 19. 过滤定位器

*   使用 `filter()` 方法过滤定位器

```python
# 过滤可见的按钮
visible_buttons = page.locator("button").filter(lambda loc: loc.is_visible())

# 过滤包含特定文本的元素
submit_buttons = page.locator("button").filter(
    lambda loc: "Submit" in loc.inner_text()
)

# 过滤特定属性的元素
enabled_inputs = page.locator("input").filter(
    lambda loc: loc.is_enabled()
)
```

### 20. 获取多个元素

*   处理匹配多个元素的情况

```python
# 获取所有匹配的元素
buttons = page.locator("button")
count = buttons.count()  # 获取数量

# 访问特定元素
first_button = buttons.first
last_button = buttons.last
third_button = buttons.nth(2)  # 索引从0开始

# 遍历所有元素
for i in range(buttons.count()):
    button = buttons.nth(i)
    print(button.inner_text())
```

## 六、实际应用示例

### 示例1：通过 ID 定位并获取属性

```python
# 定位元素
submit_button = page.locator("#submit-btn")

# 获取属性
button_id = submit_button.get_attribute("id")
button_class = submit_button.get_attribute("class")
button_type = submit_button.get_attribute("type")

print(f"按钮ID: {button_id}")
print(f"按钮Class: {button_class}")
print(f"按钮Type: {button_type}")

# 点击按钮
submit_button.click()
```

### 示例2：通过 name 定位表单元素

```python
# 定位表单输入框
username_input = page.locator("[name='username']")
password_input = page.locator("[name='password']")
email_input = page.locator("input[name='email']")

# 获取 name 属性（验证定位正确）
assert username_input.get_attribute("name") == "username"
assert password_input.get_attribute("name") == "password"

# 填充表单
username_input.fill("admin")
password_input.fill("password123")
email_input.fill("admin@example.com")
```

### 示例3：通过 class 定位并获取所有属性

```python
# 定位元素
button = page.locator(".btn-primary")

# 获取所有属性
def get_element_info(locator):
    """获取元素的完整信息"""
    return {
        "id": locator.get_attribute("id"),
        "name": locator.get_attribute("name"),
        "class": locator.get_attribute("class"),
        "type": locator.get_attribute("type"),
        "text": locator.inner_text(),
        "value": locator.get_attribute("value"),
    }

info = get_element_info(button)
print(f"元素信息: {info}")
```

### 示例4：动态获取元素属性并定位

```python
# 先定位一个元素，获取其属性，然后用属性定位其他元素
first_button = page.locator("button").first
button_class = first_button.get_attribute("class")

# 使用获取到的 class 定位所有相同 class 的按钮
all_buttons = page.locator(f".{button_class}")
print(f"找到 {all_buttons.count()} 个相同class的按钮")
```

## 七、定位方法优先级建议

### 推荐顺序

1. **首选**：`get_by_test_id()` - 最稳定，专为测试设计
2. **次选**：`get_by_role()` - 语义化，稳定可靠
3. **表单元素**：`get_by_label()` - 最符合用户视角
4. **文本链接**：`get_by_text()` 或 `get_by_role("link")`
5. **属性定位**：`locator("#id")`, `locator("[name='xxx']")` - 传统方法
6. **最后选择**：XPath - 仅在必要时使用

### 不推荐的情况

```python
# ❌ 不推荐：过于复杂的 CSS 选择器
page.locator("div.container > div.row > div.col-md-6 > form > input[type='text'][name='username']")

# ❌ 不推荐：脆弱的 XPath
page.locator("//html/body/div[1]/div[2]/div[3]/button[2]")

# ✅ 推荐：使用语义化定位器
page.get_by_label("Username")
page.get_by_role("button", name="Submit")
page.get_by_test_id("submit-button")
```

## 八、调试定位问题

### 检查元素是否存在

```python
# 检查元素是否可见
if page.locator("#submit-btn").is_visible():
    print("元素可见")
else:
    print("元素不可见")

# 检查元素数量
count = page.locator("button").count()
print(f"找到 {count} 个按钮")

# 高亮显示元素（调试用）
page.locator("#submit-btn").highlight()
```

### 获取元素信息用于调试

```python
def debug_element(locator, selector_name="元素"):
    """调试元素信息"""
    try:
        print(f"\n=== {selector_name} 调试信息 ===")
        print(f"是否可见: {locator.is_visible()}")
        print(f"是否启用: {locator.is_enabled()}")
        print(f"文本内容: {locator.inner_text()}")
        print(f"ID: {locator.get_attribute('id')}")
        print(f"Name: {locator.get_attribute('name')}")
        print(f"Class: {locator.get_attribute('class')}")
        print(f"Tag: {locator.evaluate('el => el.tagName')}")
    except Exception as e:
        print(f"获取元素信息失败: {e}")

# 使用示例
debug_element(page.locator("#submit-btn"), "提交按钮")
```

## 九、完整定位方法对比表

| 定位方法 | 语法示例 | 适用场景 | 稳定性 | 推荐度 |
|---------|---------|---------|--------|--------|
| `get_by_test_id()` | `page.get_by_test_id("btn")` | 测试专用 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| `get_by_role()` | `page.get_by_role("button", name="Submit")` | 通用按钮、链接 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| `get_by_label()` | `page.get_by_label("Username")` | 表单元素 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| `get_by_text()` | `page.get_by_text("Click me")` | 文本链接、按钮 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| ID 选择器 | `page.locator("#id")` | 有唯一ID的元素 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Name 选择器 | `page.locator("[name='xxx']")` | 表单元素 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Class 选择器 | `page.locator(".class")` | 样式类元素 | ⭐⭐⭐ | ⭐⭐⭐ |
| XPath | `page.locator("//button[@id='xxx']")` | 复杂定位 | ⭐⭐ | ⭐⭐ |

## 十、精准定位方法（以 "Submit" 按钮为例）

### 方法1：使用 `get_by_role()` + `name`（最推荐）

*   通过角色和可访问名称精准定位
*   优点：语义化、稳定、易读

```python
# 精准定位 Submit 按钮
page.get_by_role("button", name="Submit")

# 精确匹配（区分大小写）
page.get_by_role("button", name="Submit", exact=True)

# 如果页面有多个 Submit 按钮，可以结合其他属性
page.get_by_role("button", name="Submit").first  # 第一个
page.get_by_role("button", name="Submit").nth(1)  # 第二个
```

### 方法2：使用 `get_by_text()` + `exact=True`（文本精准匹配）

*   通过文本内容精准定位
*   优点：直观、易理解

```python
# 精确匹配文本
page.get_by_text("Submit", exact=True)

# 如果元素是按钮，可以结合角色
page.get_by_role("button").filter(lambda loc: loc.inner_text() == "Submit")
```

### 方法3：使用 ID 定位（最精准）

*   如果元素有唯一的 ID，这是最精准的方法
*   优点：唯一性、性能好

```python
# HTML: <button id="submit-btn">Submit</button>
page.locator("#submit-btn")

# 或者结合标签
page.locator("button#submit-btn")
```

### 方法4：使用 name 属性定位

*   如果元素有 name 属性，可以使用
*   优点：语义化、稳定

```python
# HTML: <button name="submit">Submit</button>
page.locator("[name='submit']")
page.locator("button[name='submit']")
```

### 方法5：使用 data-testid 定位（测试专用，最稳定）

*   专门为测试设计的属性
*   优点：最稳定、不依赖样式和文本

```python
# HTML: <button data-testid="submit-button">Submit</button>
page.get_by_test_id("submit-button")

# 或者使用 CSS 选择器
page.locator("[data-testid='submit-button']")
```

### 方法6：组合多个属性定位（最精准）

*   组合多个属性进行精确定位
*   优点：唯一性强、避免误匹配

```python
# 组合 type 和 name
page.locator("button[type='submit'][name='submit']")

# 组合 class 和文本
page.locator("button.btn-primary").filter(lambda loc: loc.inner_text() == "Submit")

# 组合多个属性
page.locator("button[type='submit'][class='btn-primary'][id='submit-btn']")
```

### 方法7：使用 XPath 精准定位

*   使用 XPath 表达式进行复杂定位
*   优点：灵活性高、可以精确定位

```python
# 通过文本精准定位
page.locator("//button[text()='Submit']")

# 通过文本和属性组合
page.locator("//button[@type='submit' and text()='Submit']")

# 通过多个属性
page.locator("//button[@id='submit-btn' and @class='btn-primary']")

# 通过部分文本
page.locator("//button[contains(text(), 'Submit')]")
```

### 方法8：在特定容器内定位（避免误匹配）

*   先定位容器，再定位按钮
*   优点：避免定位到其他区域的同名元素

```python
# 在表单内定位 Submit 按钮
form = page.locator("form")
submit_button = form.get_by_role("button", name="Submit")

# 在特定 div 内定位
container = page.locator(".form-container")
submit_button = container.get_by_role("button", name="Submit")

# 在对话框内定位
dialog = page.get_by_role("dialog", name="Confirm")
submit_button = dialog.get_by_role("button", name="Submit")
```

### 方法9：使用 `filter()` 方法过滤（精准筛选）

*   先定位所有可能的元素，再过滤出目标元素
*   优点：可以添加复杂的过滤条件

```python
# 过滤出包含 "Submit" 文本的按钮
submit_button = page.get_by_role("button").filter(
    lambda loc: "Submit" in loc.inner_text()
)

# 过滤出特定属性的按钮
submit_button = page.locator("button").filter(
    lambda loc: loc.get_attribute("type") == "submit"
)

# 组合多个条件
submit_button = page.locator("button").filter(
    lambda loc: (
        loc.get_attribute("type") == "submit" and
        loc.is_visible() and
        "Submit" in loc.inner_text()
    )
)
```

### 方法10：使用 `first`、`last`、`nth()` 处理多个匹配

*   当有多个匹配元素时，选择特定的一个
*   优点：可以精确选择第几个元素

```python
# 第一个 Submit 按钮
page.get_by_role("button", name="Submit").first

# 最后一个 Submit 按钮
page.get_by_role("button", name="Submit").last

# 第 N 个 Submit 按钮（索引从0开始）
page.get_by_role("button", name="Submit").nth(0)  # 第一个
page.get_by_role("button", name="Submit").nth(1)  # 第二个
```

## 十一、精准定位最佳实践

### 优先级推荐（从高到低）

1. **首选**：`get_by_test_id()` - 如果元素有 data-testid 属性
   ```python
   page.get_by_test_id("submit-button")
   ```

2. **次选**：`get_by_role()` + `name` - 语义化定位
   ```python
   page.get_by_role("button", name="Submit")
   ```

3. **第三**：ID 定位 - 如果元素有唯一 ID
   ```python
   page.locator("#submit-btn")
   ```

4. **第四**：容器 + 角色定位 - 避免误匹配
   ```python
   form.get_by_role("button", name="Submit")
   ```

5. **第五**：组合属性定位 - 多个属性组合
   ```python
   page.locator("button[type='submit'][name='submit']")
   ```

6. **最后**：XPath 或复杂选择器 - 仅在必要时使用

### 验证定位是否精准

```python
def verify_locator_precision(locator, expected_count=1):
    """
    验证定位器是否精准（只匹配一个元素）
    
    Args:
        locator: 定位器对象
        expected_count: 期望匹配的元素数量（默认1）
    
    Returns:
        bool: 是否精准
    """
    count = locator.count()
    if count == expected_count:
        print(f"✅ 定位精准：匹配到 {count} 个元素")
        return True
    else:
        print(f"⚠️ 定位不精准：匹配到 {count} 个元素（期望 {expected_count} 个）")
        return False

# 使用示例
submit_button = page.get_by_role("button", name="Submit")
if verify_locator_precision(submit_button):
    submit_button.click()
else:
    # 使用更精确的定位方法
    submit_button = page.locator("button#submit-btn")
    submit_button.click()
```

### 实际应用示例

```python
# 示例1：登录表单的 Submit 按钮
def click_submit_button(page):
    """精准定位并点击 Submit 按钮"""
    # 方法1：在表单内定位（推荐）
    form = page.locator("form")
    submit = form.get_by_role("button", name="Submit")
    
    # 方法2：使用 ID（如果有）
    # submit = page.locator("#submit-btn")
    
    # 方法3：使用 test-id（最稳定）
    # submit = page.get_by_test_id("submit-button")
    
    # 验证定位精准性
    assert submit.count() == 1, "应该只匹配一个 Submit 按钮"
    
    submit.click()

# 示例2：处理多个 Submit 按钮的情况
def click_specific_submit_button(page, button_index=0):
    """点击特定位置的 Submit 按钮"""
    # 获取所有 Submit 按钮
    submit_buttons = page.get_by_role("button", name="Submit")
    
    # 验证至少有一个按钮
    assert submit_buttons.count() > button_index, f"没有第 {button_index + 1} 个 Submit 按钮"
    
    # 点击指定位置的按钮
    submit_buttons.nth(button_index).click()

# 示例3：在特定容器内精准定位
def click_submit_in_dialog(page):
    """在对话框内精准定位 Submit 按钮"""
    # 先定位对话框
    dialog = page.get_by_role("dialog", name="Confirm")
    
    # 在对话框内定位 Submit 按钮
    submit = dialog.get_by_role("button", name="Submit")
    
    # 验证定位精准性
    assert submit.count() == 1, "对话框内应该只有一个 Submit 按钮"
    
    submit.click()
```

### 常见问题解决

**问题1：定位到多个元素**

```python
# ❌ 错误：可能匹配到多个元素
page.get_by_role("button", name="Submit").click()  # 如果页面有多个 Submit 按钮

# ✅ 解决：使用更精确的定位
page.locator("form").get_by_role("button", name="Submit").click()  # 在表单内定位
page.locator("#submit-btn").click()  # 使用唯一 ID
page.get_by_role("button", name="Submit").first.click()  # 选择第一个
```

**问题2：元素文本可能变化**

```python
# ❌ 错误：文本可能变化
page.get_by_text("Submit", exact=True).click()

# ✅ 解决：使用稳定的属性
page.get_by_test_id("submit-button").click()  # 使用 test-id
page.locator("#submit-btn").click()  # 使用 ID
page.get_by_role("button", name="Submit").click()  # 使用角色和名称
```

**问题3：元素在动态加载的内容中**

```python
# ✅ 解决：等待元素出现后再定位
submit_button = page.get_by_role("button", name="Submit")
submit_button.wait_for(state="visible", timeout=5000)
submit_button.click()
```

## 十二、相关资源

- [Playwright 定位器官方文档](https://playwright.dev/python/docs/locators)
- [CSS 选择器参考](https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_Selectors)
- [XPath 语法参考](https://developer.mozilla.org/zh-CN/docs/Web/XPath)
- [项目定位器使用指南](./LOCATOR_GUIDE.md)
- [Locator 操作方法参考](./PLAYWRIGHT_LOCATOR_METHODS.md)

