# search-r-research Skill

This skill implements the SEARCH-R methodology for systematic AI Agent research.

## Core Methodology: SEARCH-R Cycle

```
S ─ Survey（观察调研）    → 从实践中发现问题
E ─ Explore（探索检索）   → 检索相关知识  
A ─ Analyze（分析思考）   → 深度理论构建
R ─ Review（评审探讨）    → Human参与探讨
C ─ Confirm（确认验证）   → 实践中验证
H ─ Harvest（收获产出）   → 沉淀研究成果
R ─ Reflect（反思迭代）   → 持续优化方法
     ↓
  回到 S 继续循环
```

## Five Levels of Research Depth

| Level | Question | Method |
|-------|----------|--------|
| L0: 第一性原理 | XXX的本质是什么？为什么要XXX？ | 追问"为什么"直到无法再追问 |
| L1: 理论框架 | XXX如何建模？决策模型是什么？ | 构建模型、形式化表达、逻辑推演 |
| L2: 设计原则 | 应该遵循什么原则？原则如何权衡？ | 从理论推导原则 |
| L3: 实现思路 | 如何设计？有哪些方案？ | 从原则推导思路 |
| L4: 实施建议 | 代码怎么写？配置放哪里？ | ❌ 这不是 Research Agent 的职责 |

## When to Use This Skill

✅ **适用场景：**
- 框架和方法论研究（需要系统性构建理论框架）
- 技术调研和评估（需要深入分析技术方案）
- 架构设计和演进（需要从第一性原理思考）
- 知识沉淀和提炼（需要记录和复用研究成果）

❌ **不适用场景：**
- 简单信息查询（不需要深度研究）
- 具体代码实现（这是执行层工作）
- 日常项目管理（不是研究型任务）
- 简单问题解决（不需要系统性方法）

## Research Agent System Architecture

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

## Quality Gate Framework

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

## Research Workflow

### Step 1: Survey（观察调研）
从实践中发现问题，记录观察笔记。

**输出：** `observation-notes.md`
- 发现了什么问题？
- 问题的具体表现？
- 触发的场景和条件？

### Step 2: Explore（探索检索）
检索相关知识，构建知识图谱。

**输出：** `retrieval-report.md`
- 检索了哪些信息源？
- 发现了哪些相关概念？
- 现有解决方案有哪些？

### Step 3: Analyze（分析思考）
深度理论构建，回答第一性原理问题。

**输出：** `theory-analysis.md`
- 本质是什么？（L0）
- 如何建模？（L1）
- 设计原则是什么？（L2）
- 实现思路有哪些？（L3）

### Step 4: Review（评审探讨）
与 Human 探讨，验证思考方向。

**注意：** Human 的双角色：
- **信息传递者**（不算介入）
- **关键决策者**（算介入，影响研究方向）

### Step 5: Confirm（确认验证）
在实践中验证理论。

### Step 6: Harvest（收获产出）
沉淀研究成果，更新文档。

### Step 7: Reflect（反思迭代）
反思研究过程，优化方法论。

**输出：** `reflection.md`
- 本次研究的收获
- 方法论的问题
- 改进建议

## Document Templates

### Observation Notes Template
```markdown
# Observation Notes - [日期]

## 问题发现
- **问题描述：**
- **触发场景：**
- **具体表现：**

## 初步思考
- **可能的原因：**
- **需要验证的假设：**

## 下一步
- [ ] 需要检索的知识点
```

### Theory Analysis Template
```markdown
# Theory Analysis - [主题]

## L0: 第一性原理
- **本质是什么？**
- **为什么要做这个？**

## L1: 理论框架
- **如何建模？**
- **决策模型是什么？**

## L2: 设计原则
- **应该遵循什么原则？**
- **原则之间如何权衡？**

## L3: 实现思路
- **方案A：**
- **方案B：**
- **方案对比：**
```

## Key Principles

1. **可追溯（Traceable）**
   - 记录问题如何被发现
   - 记录洞见如何产生
   - 记录决策如何做出

2. **深度（Deep）**
   - 追问第一性原理
   - 构建理论框架
   - 推导设计原则

3. **进化（Evolving）**
   - 每次会话后反思
   - 发现问题时迭代
   - 持续优化方法

## Reference

Based on SEARCH-R Framework by Sonnet0524
- GitHub: https://github.com/Sonnet0524/SEARCH-R
- License: AGPL v3.0
