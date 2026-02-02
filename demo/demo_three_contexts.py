"""
演示：三个会话同时打开百度
使用多线程实现真正的并行执行
"""
import threading
import time
from playwright.sync_api import sync_playwright
from loguru import logger

def open_baidu_in_context(context_num, browser):
    """
    在指定的 Context 中打开百度
    
    Args:
        context_num: 会话编号（1, 2, 3）
        browser: Browser 对象
    """
    logger.info(f"会话{context_num}: 开始创建 Context...")
    
    # 创建新的 Context（会话）
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        locale="zh-CN",
    )
    
    logger.info(f"会话{context_num}: Context 创建成功")
    
    # 创建 Page
    page = context.new_page()
    
    try:
        logger.info(f"会话{context_num}: 正在打开百度...")
        
        # 打开百度
        page.goto("https://www.baidu.com", wait_until="networkidle")
        
        logger.info(f"会话{context_num}: 百度打开成功！")
        logger.info(f"会话{context_num}: 页面标题 = {page.title()}")
        logger.info(f"会话{context_num}: 页面URL = {page.url}")
        
        # 等待一下，方便观察
        time.sleep(3)
        
        logger.info(f"会话{context_num}: 会话完成")
        
    except Exception as e:
        logger.error(f"会话{context_num}: 发生错误 - {e}")
    
    finally:
        # 清理资源
        page.close()
        context.close()
        logger.info(f"会话{context_num}: Context 已关闭")


def main():
    """主函数：使用多线程同时打开三个会话"""
    logger.info("=" * 50)
    logger.info("开始演示：三个会话同时打开百度")
    logger.info("=" * 50)
    
    with sync_playwright() as playwright:
        # 启动浏览器（只启动一次）
        logger.info("正在启动浏览器...")
        browser = playwright.chromium.launch(headless=False)  # headless=False 可以看到浏览器
        logger.info("浏览器启动成功！")
        
        try:
            # 创建三个线程，每个线程负责一个会话
            threads = []
            
            for i in range(1, 4):
                thread = threading.Thread(
                    target=open_baidu_in_context,
                    args=(i, browser),
                    name=f"Thread-{i}"
                )
                threads.append(thread)
            
            # 同时启动所有线程（真正的并行）
            logger.info("\n同时启动三个会话...")
            start_time = time.time()
            
            for thread in threads:
                thread.start()
                logger.info(f"{thread.name} 已启动")
            
            # 等待所有线程完成
            for thread in threads:
                thread.join()
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            logger.info("\n" + "=" * 50)
            logger.info(f"所有会话完成！总耗时: {elapsed_time:.2f} 秒")
            logger.info("=" * 50)
            
        except Exception as e:
            logger.error(f"发生错误: {e}")
        
        finally:
            # 关闭浏览器
            logger.info("正在关闭浏览器...")
            browser.close()
            logger.info("浏览器已关闭")


if __name__ == "__main__":
    main()
