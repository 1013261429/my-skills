---
name: video-subs
description: |
  视频字幕提取 - 直接用yt-dlp从视频链接提取字幕，无需处理音频，一键转录视频为文本。
  
  支持平台：
  - YouTube
  - Bilibili
  - 其他主流视频平台
  
  功能：
  - 提取内置字幕
  - 自动语音识别（如果无字幕）
  - 多语言支持
  
metadata:
  {
    "openclaw":
      {
        "emoji": "🎬",
        "requires": { "bins": ["yt-dlp", "ffmpeg"] },
      },
  }
---

# 视频字幕提取 (video-subs)

## 概述
从视频链接快速提取字幕，支持YouTube、B站等平台。

## 安装
```bash
pip3 install yt-dlp
```

## 用法
```bash
# 提取YouTube字幕
yt-dlp --list-subs "视频链接"
yt-dlp --write-subs --sub-langs zh-CN "视频链接"
```
