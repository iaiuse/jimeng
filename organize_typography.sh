#!/bin/bash

# 设置基础路径
BASE_DIR=~/Downloads/3.0/model-highlights/typography

# 创建所需的子目录
mkdir -p "$BASE_DIR/weight"
mkdir -p "$BASE_DIR/style"
mkdir -p "$BASE_DIR/handwriting"
mkdir -p "$BASE_DIR/creative"
mkdir -p "$BASE_DIR/commercial"

# 字重示例
mv "$BASE_DIR/image35.jpeg" "$BASE_DIR/weight/thin.png"
mv "$BASE_DIR/image36.jpeg" "$BASE_DIR/weight/regular.png"
mv "$BASE_DIR/image37.jpeg" "$BASE_DIR/weight/bold.png"
mv "$BASE_DIR/image38.jpeg" "$BASE_DIR/weight/extra-bold.png"

# 字体风格
mv "$BASE_DIR/image39.jpeg" "$BASE_DIR/style/serif.png"      # 弯曲字体
mv "$BASE_DIR/image40.jpeg" "$BASE_DIR/style/modern.png"     # 时尚体
mv "$BASE_DIR/image41.jpeg" "$BASE_DIR/style/cute.png"       # 可爱体
mv "$BASE_DIR/image42.jpeg" "$BASE_DIR/style/calligraphy.png" # 连笔字
mv "$BASE_DIR/image43.jpeg" "$BASE_DIR/style/graffiti.png"   # 涂鸦字
mv "$BASE_DIR/image44.png"  "$BASE_DIR/style/pixel.png"      # 像素字
mv "$BASE_DIR/image45.jpeg" "$BASE_DIR/style/english.png"    # 英文字体
mv "$BASE_DIR/image46.jpeg" "$BASE_DIR/style/mixed.png"      # 混合字体

# 手写字体
mv "$BASE_DIR/image47.jpeg" "$BASE_DIR/handwriting/casual.png"    # 随性手写
mv "$BASE_DIR/image48.png"  "$BASE_DIR/handwriting/neat.png"      # 工整手写
mv "$BASE_DIR/image49.jpeg" "$BASE_DIR/handwriting/sketch.png"    # 速写手绘

# 创意排版
mv "$BASE_DIR/image50.jpeg" "$BASE_DIR/creative/poster.png"   # 海报设计
mv "$BASE_DIR/image51.jpeg" "$BASE_DIR/creative/logo.png"     # Logo设计
mv "$BASE_DIR/image52.jpeg" "$BASE_DIR/creative/banner.png"   # 横幅设计

# 商业排版
mv "$BASE_DIR/image53.png"  "$BASE_DIR/commercial/brand.png"      # 品牌设计
mv "$BASE_DIR/image54.png"  "$BASE_DIR/commercial/ad.png"         # 广告设计
mv "$BASE_DIR/image55.png"  "$BASE_DIR/commercial/packaging.png"  # 包装设计

echo "文件整理完成！" 