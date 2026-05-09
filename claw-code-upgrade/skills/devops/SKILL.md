# DevOps Integration Skill

## Description
DevOps集成系统，支持CI/CD触发、部署验证和监控查询。

## When to Use
- 需要触发CI流水线时
- 需要验证部署时
- 需要查询监控状态时

## Instructions

### CI Pipeline
支持功能:
- 工作流触发
- 状态查询
- 日志获取
- 构件下载

### Deployment Verification
验证项:
- HTTP响应
- 健康检查
- API端点
- 响应时间

### Monitoring
查询指标:
- CPU/内存/磁盘
- 进程状态
- 错误日志
- 告警状态

### Commands
- `ci-pipeline` - CI流水线
- `deploy-verify` - 部署验证
- `monitor-alert` - 监控告警

## Examples

### Trigger CI
```bash
ci-pipeline --trigger --workflow test.yml
```

### Verify Deployment
```bash
deploy-verify --url https://api.example.com --health-path /health
```

### Check Alerts
```bash
monitor-alert --service api --status critical --since 1h
```

## References
- `scripts/ci-pipeline`
- `scripts/deploy-verify`
- `scripts/monitor-alert`
