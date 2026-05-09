# RBAC Enhancement Skill

## Description
高级权限矩阵系统，提供细粒度的基于角色的访问控制(RBAC)。

## When to Use
- 需要配置不同用户角色的权限时
- 需要审计当前权限配置时
- 需要实施最小权限原则时

## Instructions

### Permission Levels
- `ReadOnly` - 只读访问
- `WorkspaceWrite` - 工作区写入
- `DangerFullAccess` - 完全访问（危险操作）

### Roles
- `viewer` - 只读角色
- `developer` - 开发角色（读写）
- `admin` - 管理员角色（完全访问）
- `auditor` - 审计角色（只读+审计）

### Commands
- `rbac-audit` - 审计权限配置
- `rbac-config` - 配置权限

### Configuration
权限配置存储在 `.claw/settings.local.json`：
```json
{
  "permissions": {
    "defaultMode": "plan",
    "allowedTools": ["read_file", "glob_search"]
  }
}
```

## Examples

### Audit Current Permissions
```bash
rbac-audit --format=json
```

### Configure Developer Role
```bash
rbac-config --mode acceptEdits --tools read_file,write_file,edit_file,bash
```

### Restrict to Read-Only
```bash
rbac-config --mode plan --tools read_file,glob_search,grep_search
```

## References
- `scripts/rbac-audit`
- `scripts/rbac-config`
