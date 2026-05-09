---
name: free-ride
description: |
  免费AI模型管理器，管理OpenRouter提供的免费模型，自动按质量排序、限流切换，零成本体验GPT-4、Claude等顶级模型。
  
  功能：
  - 免费模型自动发现
  - 智能限流管理
  - 质量排序
  - 自动故障切换
  
metadata:
  {
    "openclaw":
      {
        "emoji": "🆓",
        "requires": { "env": ["OPENROUTER_API_KEY"] },
        "primaryEnv": "OPENROUTER_API_KEY",
      },
  }
---

# 免费AI模型管理器 (free-ride)

## 概述
零成本使用OpenRouter上的免费AI模型。

## 功能
- 自动发现免费模型
- 质量评分排序
- 限流保护
- 故障自动切换

## 获取API Key
访问 https://openrouter.ai/ 注册获取
