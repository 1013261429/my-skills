# Multimodal Processing Skill

## Description
多模态内容处理系统，支持图像分析、音频转录和视频提取。

## When to Use
- 需要分析图像内容时
- 需要转录音频文件时
- 需要从视频中提取帧或信息时

## Instructions

### Image Analysis
支持格式: PNG, JPG, WebP, BMP
功能:
- 图像尺寸调整
- 格式转换
- 优化压缩

### Audio Transcription
支持格式: MP3, WAV, OGG, FLAC
功能:
- 格式转换
- 比特率调整
- 音频剪辑

### Video Processing
支持格式: MP4, AVI, MOV
功能:
- 帧提取
- 缩略图生成
- 格式转换

### Commands
- `image-process` - 图像处理
- `audio-convert` - 音频转换
- `video-frame` - 视频帧提取

## Examples

### Resize Image
```bash
image-process input.png --resize 800x600 --format jpg --optimize
```

### Convert Audio
```bash
audio-convert input.wav --format mp3 --bitrate 128k
```

### Extract Video Frames
```bash
video-frame input.mp4 --rate 1 --output-dir frames/ --format jpg
```

## References
- `scripts/image-process`
- `scripts/audio-convert`
- `scripts/video-frame`
