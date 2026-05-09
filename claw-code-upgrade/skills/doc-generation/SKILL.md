# Document Generation Skill

## Description
智能文档生成系统，自动生成API文档、架构图和CHANGELOG。

## When to Use
- 需要更新API文档时
- 需要生成架构图时
- 需要编写CHANGELOG时

## Instructions

### API Documentation
自动生成:
- 函数签名
- 参数说明
- 返回值
- 使用示例

### Architecture Diagrams
支持格式:
- Markdown
- DOT/Graphviz
- HTML

### Changelog
自动生成:
- 版本历史
- 变更分类
- 贡献者列表

### Commands
- `doc-api` - API文档
- `doc-architecture` - 架构文档
- `doc-changelog` - 变更日志

## Examples

### Generate API Docs
```bash
doc-api --source-dir src/ --output docs/api/
```

### Create Architecture Doc
```bash
doc-architecture --format md --output ARCHITECTURE.md
```

### Generate Changelog
```bash
doc-changelog --since v1.0.0 --output CHANGELOG.md
```

## References
- `scripts/doc-api`
- `scripts/doc-architecture`
- `scripts/doc-changelog`
