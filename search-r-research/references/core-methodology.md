# SEARCH-R 核心方法论参考

## 1. Agent 与 Subagent 的区分标准

区分标准：**决策自主性**（不是文档）

```
┌──────────────────────────────────────────────────────────┐
│                Distinction Standard                      │
│            Decision Autonomy (NOT documentation)         │
└──────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
            │                               │
            ▼                               ▼
┌─────────────────────┐           ┌─────────────────────┐
│       Agent         │           │     Subagent        │
│   (Has autonomy)    │           │   (No autonomy)     │
├─────────────────────┤           ├─────────────────────┤
│ ✅ Autonomous       │           │ ❌ Task-bound       │
│ ✅ Independent      │           │ ❌ Decision-limited │
│ ✅ Responsible      │           │ ❌ Execute assigned │
├─────────────────────┤           ├─────────────────────┤
│ Example:            │           │ Example:            │
│ • PM Agent          │           │ • AI Team           │
│ • Research Agent    │           │ • Core Team         │
└─────────────────────┘           └─────────────────────┘
```

## 2. Skills 分离原则

### 什么应该成为 Skills？

```
┌──────────────────────────────────────────────────────────┐
│           What should be Skills?                         │
└──────────────────────────────────────────────────────────┘

   Principle 1     Principle 2     Principle 3
   ───────────     ───────────     ───────────
   Not every time  Reusable        Independent
   ─────────────── ─────────────── ───────────────
         │               │               │
         └───────────────┼───────────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    Can be Skills    │
              └─────────────────────┘
```

### Skills 分类

| 类别 | 示例 |
|------|------|
| 🎯 决策支持 | quality-gate, risk-assessment |
| 🔄 工作流 | git-workflow, review-process |
| 📋 标准 | coding-standards, doc-guide |
| 📚 领域知识 | embedding-models, vector-search |

## 3. 记忆系统 vs 访问系统

```
┌──────────────────────────────────────────────────────────┐
│                    Key Distinction                       │
└──────────────────────────────────────────────────────────┘

      Memory System              Access System
      ─────────────              ─────────────
         (Content)                  (Method)

      ┌─────────────┐            ┌─────────────┐
      │  Books in   │            │   Library   │
      │  a library  │            │   catalog   │
      └─────────────┘            └─────────────┘

      Stored information         Method to retrieve
      itself                     content
```

**重要提示：** Index ≠ Memory
- Index 是"目录"，不是"内容"
- Index 是"方法"，不是"记忆"

## 4. Human 的双角色

```
┌─────────────────────────────────────────────────────────┐
│                 Human's Dual Roles                      │
└─────────────────────────────────────────────────────────┘
                    │
    ┌───────────────┴───────────────┐
    │                               │
    ▼                               ▼
┌─────────────────────┐   ┌─────────────────────┐
│      Role 1         │   │      Role 2         │
│   ─────────         │   │   ─────────         │
│  Information        │   │   Key Decision      │
│  Transmitter        │   │   Maker             │
├─────────────────────┤   ├─────────────────────┤
│ • Agent间信息传递   │   │ • 研究方向选择      │
│ • 不做决策          │   │ • 设计方案决策      │
│ • 不算"介入"        │   │ • 影响项目方向      │
└─────────────────────┘   └─────────────────────┘
        │                         │
        │                         │
        ▼                         ▼
   Not counted                IS counted
   as intervention           as intervention
```

## 5. 质量门控三层架构

```
┌─────────────────────────────────────────────────────────┐
│  Layer 1: Metacognitive Awareness (Inseparable)         │
│  ─────────────────────────────────────────────────────  │
│  "I know when I don't know"                             │
│  ├─ Defined in AGENTS.md                                │
│  └─ Core attribute of Agent                             │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Evaluation Rules (Can be Skills)              │
│  ─────────────────────────────────────────────────────  │
│  ├─ Determinism evaluation (HIGH/MEDIUM/LOW)            │
│  ├─ Acceptability evaluation                            │
│  └─ Confusion detection                                 │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Evaluation Tools (Can be Skills)              │
│  ─────────────────────────────────────────────────────  │
│  ├─ Quality gate schemas                                │
│  └─ Evaluation workflows                                │
└─────────────────────────────────────────────────────────┘
```

## 6. 研究深度五级模型

```
┌──────────────────────────────────────────────────────────┐
│ Level 0: 第一性原理层                                    │
│ 问题：XXX的本质是什么？为什么要XXX？                      │
│ 方法：追问"为什么"直到无法再追问                          │
├──────────────────────────────────────────────────────────┤
│ Level 1: 理论框架层                                      │
│ 问题：XXX如何建模？决策模型是什么？                       │
│ 方法：构建模型、形式化表达、逻辑推演                      │
├──────────────────────────────────────────────────────────┤
│ Level 2: 设计原则层                                      │
│ 问题：应该遵循什么原则？原则如何权衡？                    │
│ 方法：从理论推导原则                                      │
├──────────────────────────────────────────────────────────┤
│ Level 3: 实现思路层                                      │
│ 问题：如何设计？有哪些方案？                              │
│ 方法：从原则推导思路                                      │
├──────────────────────────────────────────────────────────┤
│ Level 4: 实施建议层 ❌                                   │
│ 问题：代码怎么写？配置放哪里？                            │
│ 方法：这不是Research Agent的职责范围                      │
└──────────────────────────────────────────────────────────┘
```

## 7. Agent 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                    Agent System                         │
├─────────────────────────────────────────────────────────┤
│  Identity Layer                                         │
│  ├─ File: AGENTS.md                                     │
│  ├─ Content: Role + Core Capabilities                   │
│  └─ Nature: Long-term, Stable                           │
├─────────────────────────────────────────────────────────┤
│  Capability System                                      │
│  ├─ Core Capabilities (Inseparable)                     │
│  └─ General Capabilities (Skills, Reusable)             │
├─────────────────────────────────────────────────────────┤
│  Memory System                                          │
│  ├─ Identity Memory (AGENTS.md)                         │
│  ├─ State Memory (CATCH_UP.md)                          │
│  ├─ Experience Memory (experiences/)                    │
│  └─ Session Memory (session-log.md)                     │
├─────────────────────────────────────────────────────────┤
│  Access System                                          │
│  ├─ Memory Index (memory-index.yaml)                    │
│  ├─ Retrieval Mechanism                                 │
│  └─ Compression Mechanism                               │
└─────────────────────────────────────────────────────────┘
```

## 8. 研究循环流程

```
 ┌───────────────────────────────────────┐
 │                                       │
 │  S ─ Survey（观察调研）               │
 │     从实践中发现问题                  │
 │     ↓                                 │
 │  E ─ Explore（探索检索）              │
 │     检索相关知识                      │
 │     ↓                                 │
 │  A ─ Analyze（分析思考）              │
 │     深度理论构建                      │
 │     ↓                                 │
 │  R ─ Review（评审探讨）               │
 │     Human参与探讨                     │
 │     ↓                                 │
 │  C ─ Confirm（确认验证）              │
 │     实践中验证                        │
 │     ↓                                 │
 │  H ─ Harvest（收获产出）              │
 │     沉淀研究成果                      │
 │     ↓                                 │
 │  R ─ Reflect（反思迭代）              │
 │     持续优化方法                      │
 │                                       │
 └───────────────────────────────────────┘
              ↓
         回到S继续循环
```

## 9. 设计哲学三原则

### 1️⃣ 可追溯（Traceable）
每次研究都应该记录：
- 问题是如何被发现的
- 洞见是如何产生的
- 决策是如何做出的

### 2️⃣ 深度（Deep）
不应该停留在表面：
- 追问第一性原理
- 构建理论框架
- 推导设计原则

### 3️⃣ 进化（Evolving）
研究方法应该不断进化：
- 每次会话后反思
- 发现问题时迭代
- 持续优化方法

## 10. Research Agent 的职责边界

```
┌─────────────────────────────────────────────────────────┐
│                   Research Agent                        │
│                   ─────────────                         │
│                                                         │
│  Focus on:          Not on:                             │
│  ─────────          ─────────                           │
│  ✅ Why              ❌ How to implement                 │
│  ✅ What             ❌ Code details                     │
│  ✅ Principles       ❌ Configuration                    │
│                                                         │
│  Provide:                                               │
│  ─────────                                              │
│  💡 Theoretical support                                 │
│  🎨 Design thinking                                     │
│  📋 Implementation approaches                           │
└─────────────────────────────────────────────────────────┘
```

---

Source: https://github.com/Sonnet0524/SEARCH-R
License: AGPL v3.0
