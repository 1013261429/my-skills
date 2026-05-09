# Collaboration Skill

## Description
协作开发系统，支持PR分析、智能分配和通知发送。

## When to Use
- 需要审查PR时
- 需要分配审查者时
- 需要发送通知时

## Instructions

### PR Analysis
分析维度:
- 变更文件
- 代码统计
- 审查状态
- 测试覆盖

### PR Assignment
分配策略:
- 轮询分配
- 负载均衡
- 专长匹配

### Notifications
支持渠道:
- Slack
- Discord
- Email

### Commands
- `pr-analyze` - PR分析
- `pr-assign` - PR分配
- `pr-notify` - PR通知

## Examples

### Analyze PR
```bash
pr-analyze --pr 123 --repo owner/repo
```

### Assign PR
```bash
pr-assign --pr 123 --strategy round-robin
```

### Send Notification
```bash
pr-notify --pr 123 --message "Ready for review" --channel slack
```

## References
- `scripts/pr-analyze`
- `scripts/pr-assign`
- `scripts/pr-notify`
