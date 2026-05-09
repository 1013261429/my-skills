---
name: browser-auto
description: |
  浏览器自动化技能 - 让OpenClaw能打开网页、点击、输入、截图，实现任何浏览器操作。
  相当于给AI装上了"手和眼睛"。
  
  支持：
  - 网页截图
  - 表单自动填写
  - 点击、滚动、导航
  - 网页内容提取
  - JavaScript执行
  
  Use when: 需要与网页交互、获取动态内容、自动化网页操作等场景。
  
metadata:
  {
    "openclaw":
      {
        "emoji": "🌐",
        "requires": { "bins": ["playwright", "python3"] },
      },
  }
---

# 浏览器自动化 (browser-auto)

## 概述
使用 Playwright 实现浏览器自动化，支持网页截图、表单填写、点击操作等。

## 安装依赖
```bash
pip3 install playwright
playwright install chromium
```

## 功能
- 网页截图
- 表单填写与提交
- 内容提取
- 自动化操作
