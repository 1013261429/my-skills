# 小智 MCP 服务

为小智设备（Xiaozhi）提供的 MCP (Model Context Protocol) 扩展服务。

## 🛠️ 功能

| 工具名 | 功能 | 触发场景 |
|--------|------|----------|
| `get_current_time` | 获取当前时间 | 问几点、今天几号 |
| `search_web` | 网络搜索 | 查新闻、知识、实时信息 |
| `calculator` | 数学计算 | 算数、公式、单位换算 |
| `get_weather` | 天气查询 | 问天气、气温 |

## 📦 安装

```bash
pip install -r requirements.txt
```

依赖：
- `mcp` - MCP 协议库
- `ddgr` - DuckDuckGo 命令行搜索（可选，用于 search_web）

## 🚀 使用

### 1. 获取 mcp_pipe.py 桥接脚本

```bash
curl -O https://raw.githubusercontent.com/78/mcp-calculator/main/mcp_pipe.py
```

### 2. 配置环境变量

```bash
export MCP_ENDPOINT=ws://your-xiaozhi-device-endpoint
```

### 3. 启动服务

```bash
python mcp_pipe.py server.py
```

## 📝 注意事项

1. 工具名和参数名已按规范命名，便于大模型理解
2. 函数文档注释（`"""..."""`）引导大模型何时调用该工具
3. 使用 `logger` 输出调试信息，避免 `print` 占用 stdio
4. 返回值控制在 1024 字节以内
5. 每个 MCP 接入点连接数有限制

## 🔗 参考

- [MCP Calculator 示例](https://github.com/78/mcp-calculator)
- [MCP 协议文档](https://modelcontextprotocol.io)
