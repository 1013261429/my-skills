# Code Intelligence Skill

## Description
智能代码分析系统，提供代码审查、复杂度检测和安全扫描。

## When to Use
- 需要评估代码质量时
- 需要检测潜在安全漏洞时
- 需要生成代码度量报告时

## Instructions

### Code Metrics
分析维度:
- 代码行数统计
- 函数数量
- 复杂度指标
- 依赖分析

### Security Scan
检查项:
- 密钥泄露
- 不安全函数使用
- 依赖漏洞
- 权限问题

### Commands
- `code-metrics` - 代码度量分析
- `security-audit` - 安全审计
- `complexity-report` - 复杂度报告

## Examples

### Analyze Code Metrics
```bash
code-metrics --language rust --output json
```

### Run Security Audit
```bash
security-audit --deep --format sarif
```

### Generate Complexity Report
```bash
complexity-report --threshold 10 --output report.html
```

## References
- `scripts/code-metrics`
- `scripts/security-audit`
- `scripts/complexity-report`
