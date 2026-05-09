---
name: youtube-transcript
description: |
  视频字幕提取，直接用yt-dlp从视频链接提取字幕，无需处理音频，一键转录YouTube视频为文本。
  
  支持平台：
  - YouTube
  - Bilibili
  - 其他主流视频平台
  
metadata:
  {
    "openclaw":
      {
        "emoji": "🎬",
        "requires": { "bins": ["yt-dlp"] },
      },
  }
---

# 视频字幕提取 (youtube-transcript)

## 概述
从视频链接快速提取字幕文本。

## 安装
```bash
pip3 install yt-dlp
```

## 用法
```bash
# 提取字幕
yt-dlp --list-subs "视频URL"
yt-dlp --write-subs --sub-langs zh-CN "视频URL"
```
