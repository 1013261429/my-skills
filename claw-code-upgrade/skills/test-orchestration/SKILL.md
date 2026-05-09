# Test Orchestration Skill

## Description
自动化测试编排系统，支持测试发现、执行和覆盖率分析。

## When to Use
- 需要运行测试套件时
- 需要分析测试覆盖率时
- 需要发现测试文件时

## Instructions

### Test Discovery
自动检测:
- 测试框架类型
- 测试文件位置
- 测试用例列表

### Coverage Analysis
支持报告:
- 行覆盖率
- 分支覆盖率
- 函数覆盖率
- HTML报告

### Commands
- `test-discover` - 发现测试
- `test-coverage` - 覆盖率分析

## Examples

### Discover Tests
```bash
test-discover --framework pytest --output tests.json
```

### Run Coverage Analysis
```bash
test-coverage --format html --output coverage/
```

### Full Test Pipeline
```bash
test-discover && test-coverage --format html
```

## References
- `scripts/test-discover`
- `scripts/test-coverage`
