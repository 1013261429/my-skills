---
name: bailian
description: |
  阿里云百炼 (Alibaba Cloud Bailian) 大模型 API 调用。支持：
  1. 千问 (Qwen) 系列模型对话
  2. 联网搜索功能（使用 qwen-max、qwen-turbo 等模型时自动启用）
  3. 文本生成、代码辅助、知识问答
  
  Use when: 需要中文大模型能力、实时网络搜索、知识问答等场景。
  
metadata:
  {
    "openclaw":
      {
        "emoji": "🔍",
        "requires": { "env": ["DASHSCOPE_API_KEY"], "bins": ["curl"] },
        "primaryEnv": "DASHSCOPE_API_KEY",
      },
  }
---

# 阿里云百炼 (Bailian) 技能

## 概述

使用阿里云百炼平台调用通义千问系列大模型，支持联网搜索、代码解释等能力。

## 环境变量

| 变量名 | 说明 | 获取方式 |
|--------|------|----------|
| `DASHSCOPE_API_KEY` | 百炼 API Key | [阿里云百炼控制台](https://bailian.console.aliyun.com/) |

## 支持的模型

| 模型名 | 说明 | 特点 |
|--------|------|------|
| `qwen-max` | 通义千问-Max | 最强性能，支持复杂推理和联网搜索 |
| `qwen-plus` | 通义千问-Plus | 平衡性能与速度 |
| `qwen-turbo` | 通义千问-Turbo | 高速响应，轻量级任务 |
| `qwen-coder-plus` | 通义千问-代码 | 代码生成和解释 |

## 调用方式

### OpenAI 兼容接口（推荐）

```bash
# 流式对话
curl https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-max",
    "messages": [{"role": "user", "content": "你好，请介绍一下自己"}],
    "stream": true
  }'
```

### 启用联网搜索

```bash
curl https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions \
  -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen-max",
    "messages": [{"role": "user", "content": "今天的新闻"}],
    "extra_body": {
      "enable_search": true
    }
  }'
```

## 示例任务

1. **知识问答**
   ```
   使用 bailian 询问通义千问：什么是量子计算？
   ```

2. **联网搜索**
   ```
   使用 bailian 搜索今天的科技新闻（启用 enable_search）
   ```

3. **代码辅助**
   ```
   使用 bailian-coder 写一个 Python 函数计算斐波那契数列
   ```

## 注意事项

- 联网搜索需要在 extra_body 中设置 `"enable_search": true`
- API Key 请妥善保管，不要泄露到公开代码中
- 流式响应用 `"stream": true`
