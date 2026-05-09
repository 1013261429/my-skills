# Performance Analysis Skill

## Description
性能监控分析系统，提供性能分析、回归检测和火焰图生成。

## When to Use
- 需要测量代码性能时
- 需要检测性能回归时
- 需要优化瓶颈时

## Instructions

### Benchmarking
测量指标:
- 执行时间
- 内存使用
- CPU使用率
- 吞吐量

### Regression Detection
比较维度:
- 基线对比
- 趋势分析
- 阈值告警

### Commands
- `perf-benchmark` - 性能基准测试
- `perf-regression` - 回归检测

## Examples

### Run Benchmark
```bash
perf-benchmark --command "cargo test" --iterations 5 --output perf.json
```

### Check Regression
```bash
perf-regression --baseline baseline.json --current current.json --threshold 10
```

## References
- `scripts/perf-benchmark`
- `scripts/perf-regression`
