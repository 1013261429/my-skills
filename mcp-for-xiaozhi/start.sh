#!/bin/bash
# 小智 MCP 服务一键启动脚本

echo "🚀 启动小智 MCP 服务..."

# 设置 WebSocket 端点
export MCP_ENDPOINT="wss://api.xiaozhi.me/mcp/?token=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjE1MzA5MSwiYWdlbnRJZCI6NDc3NjEsImVuZHBvaW50SWQiOiJhZ2VudF80Nzc2MSIsInB1cnBvc2UiOiJtY3AtZW5kcG9pbnQiLCJpYXQiOjE3NzgzNzY5NTQsImV4cCI6MTgwOTkzNDU1NH0.pBhz63ERykpOIFjt2hqabKMDxzlJlvFKYgaq-4FEIJBEqg-0lqFxickITqM0cuxkxBc8ZNvzvHxr999P2JhBIQ"

echo "📡 WebSocket 端点已配置: wss://api.xiaozhi.me/mcp/"

# 检查 mcp_pipe.py 是否存在
if [ ! -f "mcp_pipe.py" ]; then
    echo "⬇️  下载 mcp_pipe.py 桥接脚本..."
    curl -O https://raw.githubusercontent.com/78/mcp-calculator/main/mcp_pipe.py
    if [ $? -ne 0 ]; then
        echo "❌ 下载失败，请手动下载: https://raw.githubusercontent.com/78/mcp-calculator/main/mcp_pipe.py"
        exit 1
    fi
fi

# 启动 MCP 服务
echo "▶️  启动 server.py..."
python3 mcp_pipe.py server.py