---
name: ddg-search
description: |
  DuckDuckGo 网络搜索 - 无需 API Key，匿名搜索网页内容。
  
  Use when: 需要搜索网络信息、查找资料、获取最新资讯等。
  
  Features:
  - 无需 API Key，完全免费
  - 保护隐私，不追踪用户
  - 支持中文搜索
  - 可获取搜索结果摘要
  
metadata:
  {
    "openclaw":
      {
        "emoji": "🦆",
        "requires": { "bins": ["ddgr", "python3"] },
        "install":
          [
            {
              "id": "pip",
              "kind": "pip",
              "package": "ddgr",
              "bins": ["ddgr"],
              "label": "Install ddgr via pip",
            },
          ],
      },
  }
---

# DuckDuckGo 搜索技能 (ddg-search)

## 概述

使用 DuckDuckGo 搜索引擎进行匿名网页搜索，**无需 API Key**，完全免费。

## 安装依赖

```bash
# 方式1：通过 pip 安装
pip3 install ddgr

# 方式2：从源码安装
git clone https://github.com/jarun/ddgr.git
cd ddgr
sudo make install
```

## 基本用法

### 1. 简单搜索
```bash
# 搜索关键词
ddgr "OpenClaw 安装教程"

# 搜索中文内容
ddgr "阿里云百炼使用方法"
```

### 2. 获取前 N 个结果
```bash
# 获取前 5 个结果
ddgr -n 5 "Python 教程"

# 获取前 10 个结果（默认）
ddgr -n 10 "机器学习入门"
```

### 3. 指定网站搜索
```bash
# 仅在 github.com 搜索
ddgr -w github.com "openclaw"
```

### 4. 输出 JSON 格式（便于程序处理）
```bash
ddgr --json "人工智能最新进展"
```

## 常用选项

| 选项 | 说明 | 示例 |
|------|------|------|
| `-n NUM` | 结果数量 | `ddgr -n 5 "关键词"` |
| `-w SITE` | 限定网站 | `ddgr -w wikipedia.org "量子力学"` |
| `--json` | JSON 输出 | `ddgr --json "新闻"` |
| `--noprompt` | 非交互模式 | `ddgr --noprompt "快速搜索"` |
| `-x` | 包含 URL | `ddgr -x "教程"` |
| `-C` | 禁用颜色 | `ddgr -C "纯文本输出"` |

## 使用示例

### 搜索技术文档
```bash
ddgr --json -n 3 "OpenClaw 官方文档"
```

### 搜索新闻资讯
```bash
ddgr -n 5 "今日科技新闻"
```

### 搜索代码示例
```bash
ddgr -w github.com -n 5 "docker compose 示例"
```

## 注意事项

1. **无需 API Key** - DuckDuckGo 是匿名搜索引擎
2. **可能有频率限制** - 大量搜索时建议适当间隔
3. **网络要求** - 需要能访问 DuckDuckGo (duckduckgo.com)
4. **中文支持** - 支持中文搜索，但部分结果可能受限

## 替代方案

如果 `ddgr` 不可用，可以使用 `curl` + `pup` 解析：

```bash
# 直接使用 curl 获取搜索结果
curl -s "https://html.duckduckgo.com/html/?q=OpenClaw" | \
  grep -oP '(?<=<a class="result__a" href=")[^"]*' | head -5
```
