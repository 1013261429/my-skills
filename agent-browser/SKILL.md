---
name: agent-browser
description: |
  浏览器自动化，让OpenClaw能打开网页、点击、输入、截图，实现任何浏览器操作，相当于给AI装上了"手和眼睛"。
  
  支持：
  - 网页截图
  - 表单自动填写
  - 点击、滚动、导航
  - 网页内容提取
  - JavaScript执行
  
metadata:
  {
    "openclaw":
      {
        "emoji": "🌐",
        "requires": { "bins": ["playwright"] },
      },
  }
---

# 浏览器自动化 (agent-browser)

## 概述
使用Playwright实现浏览器自动化控制。

## 功能
- 网页截图
- 表单填写
- 元素点击
- 内容提取
- 页面导航

## 安装
```bash
pip3 install playwright
playwright install chromium
```
