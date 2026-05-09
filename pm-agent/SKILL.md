---
name: pm-agent
description: |
  PM Agent - 项目管理Agent，基于 agent-team-template v1.1.0 方法论。
  
  核心能力：
  - 项目规划与分解
  - 动态组建Agent Team
  - 任务分配与跟踪
  - 文档化管理
  - 质量保证
  
  设计原则：
  - ✅ 主动启动 - 分配后立即启动Agent
  - ❌ 不轮询 - 不主动检查进度
  - ✅ 被动接收 - 等待Agent报告
  - 📄 文档化交互 - 通过文档交换信息
  
metadata:
  {
    "openclaw":
      {
        "emoji": "📊",
        "requires": { "skills": ["clawflow", "self-improving-agent", "find-skills"] },
      },
  }
---

# PM Agent 项目管理技能

> 基于 agent-team-template v1.1.0 方法论实现

## 工作流程

### 1. 需求理解
- 仔细阅读用户描述
- 澄清模糊点
- 确认项目目标

### 2. 任务分解
将大任务分解为可并行执行的子任务：
```
大任务
├── 子任务A（可并行）
├── 子任务B（可并行）
└── 子任务C（依赖A）
```

### 3. Team 组建
根据任务类型选择合适的Agent：

| 任务类型 | 推荐Agent | 工具 |
|---------|----------|------|
| 代码开发 | coding-agent | sessions_spawn |
| 搜索研究 | tavily-search/ddg-search | web_search |
| 文档处理 | nano-pdf/summarize | read/write |
| 安全审查 | skill-security | exec |
| 技能安装 | find-skills | exec |

### 4. 任务分配
为每个子Agent创建任务文件：
```markdown
# Task: [任务名]
## 目标
[具体目标]

## 输入
[必要输入]

## 输出要求
[期望输出格式]

## 约束
[限制条件]
```

### 5. 并行执行
使用 sessions_spawn 并行启动多个子Agent：
```javascript
// 并行启动
const tasks = [
  sessions_spawn({task: "任务A", runtime: "subagent"}),
  sessions_spawn({task: "任务B", runtime: "subagent"}),
  sessions_spawn({task: "任务C", runtime: "subagent"})
];

// 等待所有完成
await Promise.all(tasks);
```

### 6. 结果汇总
- 收集各Agent报告
- 验证成果质量
- 整合输出

### 7. 交付与反馈
- 向用户交付成果
- 记录经验
- 更新知识库

## 质量门控

### 自我评估
在交付前检查：
- [ ] 成果是否符合预期
- [ ] 是否遗漏关键信息
- [ ] 置信度 > 70%？
- [ ] 是否需要用户确认

### 低置信度处理
```
如果置信度 < 70%：
1. 明确告知用户不确定性
2. 说明可能的风险
3. 提供替代方案
4. 请求用户决策
```

## 三级文档管理

### Level 0 - 启动记忆
- MEMORY.md - 长期记忆
- memory/YYYY-MM-DD.md - 今日记忆
- 读取时间: 每次启动

### Level 1 - 工作规范
- AGENTS.md - 工作指南
- TOOLS.md - 工具配置
- 读取时间: 需要时

### Level 2 - 参考资料
- /app/skills/*/SKILL.md - 技能文档
- /app/docs/ - 系统文档
- 读取时间: 遇到问题时

## 最佳实践

### DO ✅
- 启动时先读取记忆
- 复杂任务先分解
- 能并行的不串行
- 及时更新记忆
- 关键决策请求确认

### DON'T ❌
- 不读取记忆直接开始
- 一个任务做到底再开始下一个
- 频繁轮询子Agent状态
- 执行高风险操作不确认
- 做完不总结经验

## 并行执行示例

### 场景: 安装多个技能
```javascript
// 串行（慢）
for (const skill of skills) {
  await installSkill(skill); // 每个1分钟
}
// 总时间: N分钟

// 并行（快）
const installs = skills.map(skill => 
  sessions_spawn({task: `安装 ${skill}`, runtime: "subagent"})
);
await Promise.all(installs);
// 总时间: ~1分钟
```

### 场景: 多维度搜索
```javascript
// 同时搜索多个来源
const searches = [
  web_search({query: "A", region: "cn-zh"}),
  web_search({query: "A", region: "us-en"}),
  web_fetch({url: "https://example.com/A"})
];
const results = await Promise.allSettled(searches);
```

## 经验沉淀

### 记录内容
- 成功模式
- 失败教训
- 优化技巧
- 用户偏好

### 记录位置
- memory/YYYY-MM-DD.md - 每日日志
- AGENTS.md - 方法论更新
- TOOLS.md - 工具配置

---

**技能来源**: 学习 Sonnet0524/agent-team-template
**学习日期**: 2026-04-15
**版本**: 1.0.0
