# Security Audit Skill

## Description
安全审计系统，提供漏洞扫描、密钥检测和合规审计。

## When to Use
- 需要安全评估时
- 需要合规检查时
- 需要密钥审计时

## Instructions

### Vulnerability Scan
检查项:
- 依赖漏洞
- 已知CVE
- 配置问题
- 权限问题

### Secret Scan
检测:
- API密钥
- 密码
- 令牌
- 私钥

### Compliance Audit
支持标准:
- OWASP Top 10
- ISO 27001
- SOC 2

### Commands
- `vuln-check` - 漏洞扫描
- `secret-scan` - 密钥扫描
- `compliance-audit` - 合规审计

## Examples

### Vulnerability Check
```bash
vuln-check --deep --format json
```

### Secret Scan
```bash
secret-scan --strict --output secrets.json
```

### Compliance Audit
```bash
compliance-audit --standard owasp --output compliance.json
```

## References
- `scripts/vuln-check`
- `scripts/secret-scan`
- `scripts/compliance-audit`
