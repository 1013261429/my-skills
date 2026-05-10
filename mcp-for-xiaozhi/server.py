from mcp.server.fastmcp import FastMCP
import logging
import json
from datetime import datetime
import subprocess

logger = logging.getLogger('xiaozhi_mcp')

# 创建 MCP 服务
mcp = FastMCP("XiaozhiAssistant")

@mcp.tool()
def get_current_time() -> dict:
    """获取当前日期和时间。当用户询问现在几点、今天几号、当前时间、星期几时调用此工具。无需参数。"""
    now = datetime.now()
    return {
        "success": True,
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
        "weekday": now.strftime("%A"),
        "date": now.strftime("%Y年%m月%d日"),
        "time": now.strftime("%H:%M:%S")
    }

@mcp.tool()
def search_web(keywords: str) -> dict:
    """使用网络搜索获取信息。当用户询问新闻、知识百科、实时信息、需要联网查询时调用此工具。参数 keywords 是搜索关键词，如'北京天气'、'最新的科技新闻'。"""
    try:
        result = subprocess.run(
            ['ddgr', '--np', '-n', '3', '--json', keywords],
            capture_output=True, text=True, timeout=15
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            summaries = []
            for item in data[:3]:
                title = item.get('title', '')
                url = item.get('url', '')
                summaries.append(f"{title}: {url}")
            return {
                "success": True,
                "results": summaries,
                "keywords": keywords
            }
        else:
            return {"success": False, "error": result.stderr}
    except Exception as e:
        logger.error(f"Search failed: {e}")
        return {"success": False, "error": str(e)}

@mcp.tool()
def calculator(python_expression: str) -> dict:
    """数学计算工具。当用户需要进行数学运算、公式计算、数据换算时调用此工具。参数 python_expression 是一个 Python 数学表达式，如 '3.14159 * (8/2)**2'、'100 * 0.85'。math 和 random 库可用。"""
    try:
        import math
        import random
        allowed = {"__builtins__": {}}
        allowed.update({name: getattr(math, name) for name in dir(math) if not name.startswith('_')})
        allowed.update({name: getattr(random, name) for name in dir(random) if not name.startswith('_')})
        allowed.update({"abs": abs, "round": round, "max": max, "min": min, "sum": sum, "pow": pow})
        
        result = eval(python_expression, allowed)
        logger.info(f"Calculating: {python_expression} = {result}")
        return {"success": True, "result": result}
    except Exception as e:
        logger.error(f"Calculation failed: {e}")
        return {"success": False, "error": str(e)}

@mcp.tool()
def get_weather(city_name: str) -> dict:
    """查询指定城市的天气信息。当用户询问天气、气温、穿衣建议时调用此工具。参数 city_name 是城市名称，如'北京'、'上海'、'成都'。"""
    try:
        result = subprocess.run(
            ['curl', '-s', f'https://wttr.in/{city_name}?format=%C+%t+%h+%w&lang=zh'],
            capture_output=True, text=True, timeout=10
        )
        weather = result.stdout.strip()
        return {"success": True, "weather": weather, "city": city_name}
    except Exception as e:
        logger.error(f"Weather query failed: {e}")
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    mcp.run(transport="stdio")
