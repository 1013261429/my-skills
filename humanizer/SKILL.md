---
name: humanizer
description: |
  去AI味神器，能把AI生成的文本改写得更自然、更像人类撰写，适合需要伪装成人工内容的场景。
  
  特点：
  - 添加口语化表达
  - 插入自然停顿
  - 使用emoji和表情
  - 变化句式结构
  
metadata:
  {
    "openclaw":
      {
        "emoji": "✨",
        "requires": { "env": ["OPENAI_API_KEY"] },
        "primaryEnv": "OPENAI_API_KEY",
      },
  }
---

# 去AI味神器 (humanizer)

## 概述
将AI生成的机械文本转换为自然、生动的人类风格。

## 示例
**原文：**
> 根据数据分析，该产品具有良好的市场前景。

**改写后：**
> 看了下数据，感觉这产品还挺有搞头的 😄

## 使用
配置OPENAI_API_KEY后使用
