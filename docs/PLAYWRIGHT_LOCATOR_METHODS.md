# Playwright Locator 操作方法（按优先级排序）

## 第一优先级：基础交互操作（最常用）

### 1. `click()` - 点击操作

*   点击元素，支持多种点击方式
*   参数：
    *   `button`: 鼠标按钮（"left" | "right" | "middle"）
    *   `click_count`: 点击次数（默认1）
    *   `delay`: 按下和释放之间的延迟（毫秒）
    *   `force`: 强制点击（即使元素不可操作）
    *   `modifiers`: 修饰键列表（["Shift", "Control", "Alt", "Meta"]）
    *   `no_wait_after`: 点击后不等待导航
    *   `position`: 点击位置 {x, y}
    *   `timeout`: 超时时间（毫秒）

```python
locator.click()
locator.click(button="right")  # 右键点击
locator.click(modifiers=["Shift"])  # 按住Shift点击
locator.click(click_count=2)  # 双击
```

### 2. `fill()` - 填充输入框

*   清空输入框后填充文本（推荐用于输入框）
*   参数：
    *   `value`: 要填充的文本
    *   `force`: 强制填充（即使元素不可编辑）
    *   `no_wait_after`: 填充后不等待导航
    *   `timeout`: 超时时间（毫秒）

```python
locator.fill("username")
locator.fill("admin@example.com")
```

### 3. `type()` - 逐字符输入

*   模拟真实输入，逐字符输入文本
*   参数：
    *   `text`: 要输入的文本
    *   `delay`: 每个字符之间的延迟（毫秒，默认0）
    *   `timeout`: 超时时间（毫秒）

```python
locator.type("password123", delay=100)  # 每个字符延迟100ms
```

### 4. `inner_text()` - 获取可见文本

*   获取元素的可见文本内容
*   返回：字符串

```python
text = locator.inner_text()
assert "Welcome" in text
```

### 5. `text_content()` - 获取所有文本

*   获取元素的所有文本内容（包括隐藏文本）
*   返回：字符串

```python
content = locator.text_content()
```

### 6. `input_value()` - 获取输入框值

*   获取输入框、文本区域或选择框的值
*   返回：字符串

```python
value = locator.input_value()
assert value == "expected_value"
```

## 第二优先级：状态检查（断言常用）

### 7. `is_visible()` - 检查是否可见

*   检查元素是否可见
*   返回：布尔值
*   注意：不等待元素，立即返回结果

```python
if locator.is_visible():
    locator.click()
```

### 8. `is_hidden()` - 检查是否隐藏

*   检查元素是否隐藏
*   返回：布尔值

```python
assert locator.is_hidden()
```

### 9. `is_enabled()` - 检查是否启用

*   检查元素是否启用
*   返回：布尔值

```python
assert locator.is_enabled()
```

### 10. `is_disabled()` - 检查是否禁用

*   检查元素是否禁用
*   返回：布尔值

```python
assert locator.is_disabled()
```

### 11. `is_checked()` - 检查是否选中

*   检查复选框或单选按钮是否选中
*   返回：布尔值

```python
assert locator.is_checked()
```

### 12. `is_editable()` - 检查是否可编辑

*   检查元素是否可编辑
*   返回：布尔值

```python
assert locator.is_editable()
```

### 13. `is_focused()` - 检查是否聚焦

*   检查元素是否聚焦
*   返回：布尔值

```python
assert locator.is_focused()
```

## 第三优先级：表单操作

### 14. `check()` - 勾选复选框/单选按钮

*   勾选复选框或单选按钮
*   参数：
    *   `force`: 强制勾选
    *   `no_wait_after`: 勾选后不等待导航
    *   `position`: 点击位置
    *   `timeout`: 超时时间

```python
locator.check()
locator.check(force=True)
```

### 15. `uncheck()` - 取消勾选

*   取消勾选复选框
*   参数：同 `check()`

```python
locator.uncheck()
```

### 16. `select_option()` - 选择下拉框选项

*   选择下拉框、多选框或单选组中的选项
*   参数：
    *   `value`: 选项值
    *   `label`: 选项标签文本
    *   `index`: 选项索引（0-based）
    *   `values`: 多选值列表
    *   `force`: 强制选择
    *   `timeout`: 超时时间

```python
locator.select_option("value1")
locator.select_option(label="选项文本")
locator.select_option(index=0)
locator.select_option(values=["value1", "value2"])  # 多选
```

### 17. `set_input_files()` - 文件上传

*   设置文件输入框的文件
*   参数：
    *   `files`: 文件路径字符串或路径列表
    *   `timeout`: 超时时间

```python
locator.set_input_files("path/to/file.pdf")
locator.set_input_files(["file1.pdf", "file2.pdf"])
locator.set_input_files([], files=[])  # 清空文件
```

## 第四优先级：鼠标和键盘操作

### 18. `hover()` - 鼠标悬停

*   鼠标悬停在元素上
*   参数：
    *   `force`: 强制悬停（即使元素被遮挡）
    *   `modifiers`: 修饰键列表
    *   `position`: 悬停位置
    *   `timeout`: 超时时间

```python
locator.hover()
locator.hover(force=True)
```

### 19. `focus()` - 聚焦元素

*   聚焦元素
*   参数：
    *   `timeout`: 超时时间

```python
locator.focus()
```

### 20. `blur()` - 取消聚焦

*   取消元素聚焦
*   参数：
    *   `timeout`: 超时时间

```python
locator.blur()
```

### 21. `press()` - 按下键盘按键

*   按下单个键盘按键
*   参数：
    *   `key`: 按键名称（如 "Enter", "Escape", "ArrowDown"）
    *   `delay`: 按下和释放之间的延迟
    *   `timeout`: 超时时间

```python
locator.press("Enter")
locator.press("Escape")
locator.press("ArrowDown")
```

### 22. `press_sequentially()` - 按顺序输入

*   按顺序输入文本，模拟真实键盘输入
*   参数：
    *   `text`: 要输入的文本
    *   `delay`: 每个字符之间的延迟
    *   `timeout`: 超时时间

```python
locator.press_sequentially("Hello World", delay=50)
```

### 23. `drag_to()` - 拖拽到目标

*   拖拽元素到目标位置
*   参数：
    *   `target`: 目标定位器
    *   `force`: 强制拖拽
    *   `no_wait_after`: 拖拽后不等待导航
    *   `source_position`: 源位置
    *   `target_position`: 目标位置
    *   `timeout`: 超时时间

```python
locator.drag_to(target_locator)
locator.drag_to(target_locator, force=True)
```

### 24. `dblclick()` - 双击

*   双击元素
*   参数：同 `click()`

```python
locator.dblclick()
```

## 第五优先级：滚动和视图

### 25. `scroll_into_view_if_needed()` - 滚动到视图

*   如果元素不在视图中，则滚动到视图
*   参数：
    *   `timeout`: 超时时间

```python
locator.scroll_into_view_if_needed()
```

## 第六优先级：等待操作

### 26. `wait_for()` - 等待状态

*   等待元素达到指定状态
*   参数：
    *   `state`: 状态（"visible" | "hidden" | "attached" | "detached"）
    *   `timeout`: 超时时间（毫秒）

```python
locator.wait_for(state="visible", timeout=5000)
locator.wait_for(state="hidden")
locator.wait_for(state="attached")
locator.wait_for(state="detached")
```

## 第七优先级：截图和调试

### 27. `screenshot()` - 元素截图

*   对元素进行截图
*   参数：
    *   `path`: 截图保存路径
    *   `animations`: 是否等待动画完成（"disabled" | "allow"）
    *   `caret`: 是否显示插入符号（"hide" | "initial"）
    *   `full_page`: 是否截取完整页面
    *   `mask`: 要遮罩的定位器列表
    *   `omit_background`: 是否省略背景
    *   `quality`: 图片质量（0-100，仅JPEG）
    *   `timeout`: 超时时间
    *   `type`: 图片类型（"png" | "jpeg"）

```python
locator.screenshot(path="element.png")
locator.screenshot(path="element.png", full_page=True)
```

### 28. `highlight()` - 高亮显示

*   高亮显示元素（用于调试）
*   注意：此方法主要用于调试，会在元素周围添加高亮边框

```python
locator.highlight()
```

## 第八优先级：边界框和位置

### 29. `bounding_box()` - 获取边界框

*   获取元素的边界框（位置和尺寸）
*   返回：字典 `{x, y, width, height}` 或 `None`

```python
box = locator.bounding_box()
if box:
    print(f"位置: ({box['x']}, {box['y']})")
    print(f"尺寸: {box['width']} x {box['height']}")
```

### 30. `get_attribute()` - 获取属性值

*   获取元素的属性值
*   参数：
    *   `name`: 属性名称
    *   `timeout`: 超时时间
*   返回：属性值字符串或 `None`

```python
href = locator.get_attribute("href")
class_name = locator.get_attribute("class")
```

## 第九优先级：过滤和查找

### 31. `first` - 第一个匹配元素

*   获取第一个匹配的定位器
*   返回：新的定位器对象

```python
first_button = page.get_by_role("button").first
first_button.click()
```

### 32. `last` - 最后一个匹配元素

*   获取最后一个匹配的定位器
*   返回：新的定位器对象

```python
last_button = page.get_by_role("button").last
last_button.click()
```

### 33. `nth(index)` - 第N个元素

*   获取指定索引的定位器（0-based）
*   参数：
    *   `index`: 索引位置（从0开始）
*   返回：新的定位器对象

```python
third_button = page.get_by_role("button").nth(2)  # 第3个按钮
third_button.click()
```

### 34. `count()` - 获取元素数量

*   获取匹配元素的数量
*   返回：整数

```python
button_count = page.get_by_role("button").count()
assert button_count == 5
```

### 35. `filter()` - 过滤定位器

*   根据条件过滤定位器
*   参数：
    *   `predicate`: 过滤函数，接收 Locator 返回布尔值
*   返回：新的定位器对象

```python
visible_buttons = page.get_by_role("button").filter(
    lambda loc: loc.is_visible()
)
```

### 36. `locator(selector)` - 查找子元素

*   在当前定位器范围内查找子元素
*   参数：
    *   `selector`: 选择器字符串或定位器
*   返回：新的定位器对象

```python
container = page.locator(".container")
button = container.locator("button")
```

## 第十优先级：JavaScript 执行

### 37. `evaluate()` - 执行 JavaScript

*   在元素上执行 JavaScript 表达式
*   参数：
    *   `expression`: JavaScript 表达式字符串
    *   `arg`: 传递给表达式的参数
*   返回：表达式执行结果

```python
result = locator.evaluate("element => element.scrollTop")
result = locator.evaluate("(element, value) => element.value = value", "new value")
```

### 38. `evaluate_handle()` - 执行 JavaScript 返回句柄

*   执行 JavaScript 并返回 JSHandle
*   参数：同 `evaluate()`
*   返回：JSHandle 对象

```python
handle = locator.evaluate_handle("element => element")
```

## 第十一优先级：批量获取

### 39. `all_inner_texts()` - 获取所有文本列表

*   获取所有匹配元素的可见文本列表
*   返回：字符串列表

```python
texts = page.get_by_role("button").all_inner_texts()
assert "Submit" in texts
```

### 40. `all_text_contents()` - 获取所有文本内容列表

*   获取所有匹配元素的文本内容列表（包括隐藏文本）
*   返回：字符串列表

```python
contents = page.get_by_role("button").all_text_contents()
```

## 使用建议

### 优先级选择原则

1. **基础操作优先**：`click()`, `fill()`, `inner_text()` 用于 80% 的场景
2. **状态检查**：使用 `is_*()` 方法进行条件判断
3. **表单操作**：`check()`, `select_option()`, `set_input_files()` 用于表单场景
4. **高级操作**：`drag_to()`, `hover()` 用于复杂交互
5. **等待和调试**：`wait_for()`, `screenshot()` 用于调试和稳定性

### 最佳实践

```python
# ✅ 推荐：使用语义化定位器
page.get_by_role("button", name="Submit").click()
page.get_by_label("Username").fill("admin")

# ✅ 推荐：使用 fill() 而非 type()（除非需要模拟真实输入）
locator.fill("text")  # 快速填充

# ✅ 推荐：使用 expect() 进行断言
from playwright.sync_api import expect
expect(locator).to_be_visible()
expect(locator).to_have_text("Expected")

# ✅ 推荐：利用自动等待，减少手动 wait_for()
locator.click()  # Playwright 会自动等待元素可点击

# ✅ 推荐：使用 first, last, nth() 处理多个匹配元素
page.get_by_role("button").first.click()
page.get_by_role("button").nth(2).click()
```

## 完整方法列表（按字母顺序）

```python
# A
all_inner_texts()
all_text_contents()

# B
blur()
bounding_box()

# C
check()
click()
count()

# D
dblclick()
drag_to()

# E
evaluate()
evaluate_handle()

# F
fill()
first
focus()

# G
get_attribute()

# H
highlight()
hover()

# I
input_value()
inner_text()
is_checked()
is_disabled()
is_editable()
is_enabled()
is_focused()
is_hidden()
is_visible()

# L
last
locator()

# N
nth()

# P
press()
press_sequentially()

# S
screenshot()
scroll_into_view_if_needed()
select_option()
set_input_files()

# T
text_content()
type()

# U
uncheck()

# W
wait_for()
```

## 相关资源

- [Playwright 官方文档 - Locator](https://playwright.dev/python/docs/locators)
- [Playwright 官方文档 - API Reference](https://playwright.dev/python/docs/api/class-locator)
- [项目定位器使用指南](./LOCATOR_GUIDE.md)

