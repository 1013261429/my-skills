# Knowledge Graph Skill

## Description
知识图谱集成系统，构建项目知识库和关系图谱。

## When to Use
- 需要理解项目结构时
- 需要查找代码依赖关系时
- 需要构建项目文档时

## Instructions

### Building Knowledge Graph
从源代码提取:
- 函数定义
- 模块关系
- 调用链
- 依赖图

### Querying
支持查询:
- 函数位置
- 调用关系
- 模块依赖
- 代码统计

### Commands
- `kg-build` - 构建知识图谱
- `kg-query` - 查询知识图谱

## Examples

### Build Knowledge Graph
```bash
kg-build --source-dir src/ --output knowledge-graph.json
```

### Query for Functions
```bash
kg-query "my_function" --graph knowledge-graph.json
```

### Analyze Dependencies
```bash
kg-build --source-dir src/ && kg-query "main" --graph knowledge-graph.json
```

## References
- `scripts/kg-build`
- `scripts/kg-query`
