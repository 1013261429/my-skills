# Workflow Engine Skill

## Description
智能工作流编排系统，支持DAG定义、依赖管理和并行执行。

## When to Use
- 需要执行多步骤、有依赖关系的任务时
- 需要并行执行多个独立任务时
- 需要可视化和追踪任务执行状态时

## Instructions

### Workflow Definition
工作流使用JSON格式定义：

```json
{
  "workflow_id": "unique-id",
  "name": "Workflow Name",
  "tasks": [
    {
      "id": "task1",
      "type": "bash",
      "command": "echo 'step 1'",
      "dependencies": []
    },
    {
      "id": "task2",
      "type": "bash", 
      "command": "echo 'step 2'",
      "dependencies": ["task1"]
    }
  ]
}
```

### Commands
- `WorkflowCreate` - 创建新工作流
- `WorkflowGet` - 获取工作流状态
- `WorkflowList` - 列出所有工作流
- `WorkflowStop` - 停止工作流

### Best Practices
1. 定义清晰的任务依赖关系
2. 使用幂等操作确保可重试
3. 设置合理的超时时间
4. 添加错误处理和重试逻辑

## Examples

### Example 1: CI Pipeline Workflow
```json
{
  "tasks": [
    {"id": "lint", "type": "bash", "command": "cargo fmt --check", "dependencies": []},
    {"id": "build", "type": "bash", "command": "cargo build", "dependencies": []},
    {"id": "test", "type": "bash", "command": "cargo test", "dependencies": ["build"]},
    {"id": "deploy", "type": "bash", "command": "deploy.sh", "dependencies": ["lint", "test"]}
  ]
}
```

### Example 2: Data Processing Pipeline
```json
{
  "tasks": [
    {"id": "extract", "type": "bash", "command": "extract_data.py", "dependencies": []},
    {"id": "transform", "type": "bash", "command": "transform.py", "dependencies": ["extract"]},
    {"id": "load", "type": "bash", "command": "load.py", "dependencies": ["transform"]}
  ]
}
```

## References
- `scripts/rbac-audit`
- `scripts/rbac-config`
