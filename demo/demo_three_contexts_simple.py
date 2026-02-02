"""
演示：三个会话同时打开百度（使用异步 API）
Playwright 同步 API 不支持多线程，需要使用异步 API 实现并发
"""
import asyncio
import time
from playwright.async_api import async_playwright


async def open_baidu(context_num, browser):
    """在指定 Context 中打开百度"""
    print(f"\n[会话{context_num}] 开始创建 Context...")
    
    # 创建新的 Context
    context = await browser.new_context()
    page = await context.new_page()
    
    try:
        print(f"[会话{context_num}] 正在打开百度...")
        await page.goto("https://www.baidu.com", wait_until="networkidle")
        print(f"[会话{context_num}] ✅ 百度打开成功！")
        title = await page.title()
        print(f"[会话{context_num}] 页面标题: {title}")
        
        # 等待3秒，方便观察
        await asyncio.sleep(3)
        
        print(f"[会话{context_num}] 会话完成")
        
    finally:
        await page.close()
        await context.close()
        print(f"[会话{context_num}] Context 已关闭")


async def main():
    """主函数：使用异步实现三个会话同时打开百度"""
    print("=" * 60)
    print("演示：三个会话同时打开百度（异步并发）")
    print("=" * 60)
    
    async with async_playwright() as playwright:
        # 启动浏览器
        print("\n正在启动浏览器...")
        browser = await playwright.chromium.launch(headless=False)
        print("浏览器启动成功！\n")
        
        try:
            # 同时启动三个会话（使用 asyncio.gather）
            print("同时启动三个会话...\n")
            start_time = time.time()
            
            # 使用 asyncio.gather 同时执行三个任务
            await asyncio.gather(
                open_baidu(1, browser),
                open_baidu(2, browser),
                open_baidu(3, browser)
            )
            
            elapsed_time = time.time() - start_time
            
            print("\n" + "=" * 60)
            print(f"✅ 所有会话完成！总耗时: {elapsed_time:.2f} 秒")
            print("=" * 60)
            
        finally:
            # 关闭浏览器
            print("\n正在关闭浏览器...")
            await browser.close()
            print("完成！")


if __name__ == "__main__":
    # 运行异步主函数
    asyncio.run(main())
