---
name: skil-vetterl
description: |
  技能安全审查，在安装来自ClawHub、GitHub等来源的技能时，帮你检查安全性，避免恶意脚本风险。
  
  检查项：
  - 恶意代码检测
  - 可疑网络请求
  - 权限过度申请
  - 敏感信息泄露风险
  
metadata:
  {
    "openclaw":
      {
        "emoji": "🔒",
        "requires": { "bins": ["python3"] },
      },
  }
---

# 技能安全审查 (skil-vetterl)

## 概述
在安装技能前自动进行安全检查。

## 检查内容
1. 代码静态分析
2. 可疑命令检测
3. 网络请求审查
4. 权限合理性检查

## 使用
安装技能前自动触发检查
