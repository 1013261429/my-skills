---
name: tavily-search
description: |
  联网搜索天花板，ClawHub安装量最高的搜索技能，可查新闻、价格、方案，结果经过AI结构化处理，信息精准度远超普通搜索引擎。
  
  特点：
  - AI驱动的搜索结果优化
  - 结构化信息输出
  - 支持深度搜索
  - 实时新闻和价格查询
  
metadata:
  {
    "openclaw":
      {
        "emoji": "🔍",
        "requires": { "env": ["TAVILY_API_KEY"] },
        "primaryEnv": "TAVILY_API_KEY",
      },
  }
---

# Tavily 搜索 (tavily-search)

## 概述
专为AI应用设计的搜索引擎，提供结构化、高质量的搜索结果。

## 功能
- 智能搜索：AI优化的搜索结果
- 深度搜索：获取更全面的信息
- 结构化输出：便于程序处理
- 实时信息：新闻、价格、方案查询

## 获取API Key
访问 https://tavily.com/ 注册获取 API Key

## 使用
配置 `TAVILY_API_KEY` 后即可使用
