<template>
  <section id="model-highlights">
    <div class="section-header">
      <div class="section-number">1</div>
      <h2 class="section-title">模型亮点</h2>
    </div>
    <div class="feature-grid">
      <div v-for="feature in features" :key="feature.id" class="feature-card">
        <h3><span>{{ feature.title }}:</span> {{ feature.subtitle }}</h3>
        <p>{{ feature.description }}</p>
        
        <div v-for="(subFeature, idx) in feature.subFeatures" 
             :key="idx" 
             class="sub-feature">
          <h4>{{ subFeature.title }}</h4>
          <p>{{ subFeature.description }}</p>
          
          <div class="image-grid">
            <div v-for="(image, imageIdx) in subFeature.images" 
                 :key="imageIdx" 
                 class="image-item"
                 @click="openPreview(subFeature.images, imageIdx)">
              <img :src="getImageUrl(image.filename)" 
                   :alt="image.alt" 
                   loading="lazy"
                   :title="'点击查看大图'">
            </div>
          </div>
        </div>
      </div>
    </div>

    <ImagePreview
      :is-visible="isPreviewVisible"
      :images="previewImages"
      :initial-index="previewIndex"
      @close="closePreview"
    />
  </section>
</template>

<script setup>
import { ref } from 'vue'
import ImagePreview from './ImagePreview.vue'

const getImageUrl = (filename) => {
  return `https://jimeng-image.iaiuse.com/3.0/model-highlights/${filename}`;
}

// 图片预览相关状态
const isPreviewVisible = ref(false)
const previewImages = ref([])
const previewIndex = ref(0)

// 打开预览
const openPreview = (images, index) => {
  previewImages.value = images.map(img => ({
    src: getImageUrl(img.filename),
    title: img.alt,
    description: img.alt
  }))
  previewIndex.value = index
  isPreviewVisible.value = true
}

// 关闭预览
const closePreview = () => {
  isPreviewVisible.value = false
}

const features = [
  {
    id: 1,
    title: '真实',
    subtitle: '去ai味、以假乱真',
    description: '3.0模型能够精准还原真实细节和质感，去除AI图像常见的虚饰感和假脸感。',
    subFeatures: [
      {
        title: '质感真实',
        description: '去磨皮感、假脸感、ai油腻感',
        images: [
          { filename: 'realism/texture-1.png', alt: '质感真实示例1' },
          { filename: 'realism/texture-2.png', alt: '质感真实示例2' },
          { filename: 'realism/texture-3.png', alt: '质感真实示例3' }
        ]
      },
      {
        title: '情绪真实',
        description: '去僵硬感、摆拍感、ai眼神空洞感，情绪细腻有感染力',
        images: [
          { filename: 'realism/emotion-1.png', alt: '情绪真实示例1' },
          { filename: 'realism/emotion-2.png', alt: '情绪真实示例2' },
          { filename: 'realism/emotion-3.png', alt: '情绪真实示例3' }
        ]
      }
    ]
  },
  {
    id: 2,
    title: '高清',
    subtitle: '默认1k、可支持2K',
    description: '图像清晰度和结构准确性显著提升，2k时画面结构更准确',
    subFeatures: [
      {
        title: '分辨率提升',
        description: '支持更高分辨率输出，保持结构稳定',
        images: [
          { filename: 'hd/scene-1.png', alt: '1K' },
          { filename: 'hd/scene-2.png', alt: '1.5K' },
          { filename: 'hd/scene-3.png', alt: '2K' }
        ]
      }
    ]
  },
  {
    id: 3,
    title: '专业',
    subtitle: '专业级的画面效果',
    description: '提供专业级别的影像和动漫创作能力',
    subFeatures: [
      {
        title: '影像场景',
        description: '更准确的电影类型片、镜头语言响应',
        images: [
          // 电影类型片
          { filename: 'pro/film-type-1.jpg', alt: '电影类型1' },
          { filename: 'pro/film-type-2.jpg', alt: '电影类型2' },
          { filename: 'pro/film-type-3.jpg', alt: '电影类型3' },
          { filename: 'pro/film-type-4.jpg', alt: '电影类型4' },
          { filename: 'pro/film-type-5.jpg', alt: '电影类型5' },
          { filename: 'pro/film-type-6.jpg', alt: '电影类型6' },
          // 镜头语言
          { filename: 'pro/lens-1.jpg', alt: '镜头语言1' },
          { filename: 'pro/lens-2.jpg', alt: '镜头语言2' },
          { filename: 'pro/lens-3.jpg', alt: '镜头语言3' },
          { filename: 'pro/lens-4.jpg', alt: '镜头语言4' },
          { filename: 'pro/lens-5.jpg', alt: '镜头语言5' },
          { filename: 'pro/lens-6.jpg', alt: '镜头语言6' },
          { filename: 'pro/lens-7.jpg', alt: '镜头语言7' }
        ]
      },
      {
        title: '动漫场景',
        description: '风格更多元、细节更丰富、色调更统一，不再有2.1的"抠图感"',
        images: [
          { filename: 'pro/anime-1.jpg', alt: '动漫场景1' },
          { filename: 'pro/anime-2.jpg', alt: '动漫场景2' },
          { filename: 'pro/anime-3.jpg', alt: '动漫场景3' },
          { filename: 'pro/anime-4.jpg', alt: '动漫场景4' },
          { filename: 'pro/anime-5.jpg', alt: '动漫场景5' }
        ]
      }
    ]
  },
  {
    id: 4,
    title: '文字',
    subtitle: '更准确的字体响应、专业的设计排版',
    description: '支持多样化的字体和专业级排版效果',
    subFeatures: [
      {
        title: '字体响应能力',
        description: '大字小字都能响应、支持不同字体',
        images: [
          // 字重
          { filename: 'typography/weight-1.jpg', alt: '字重示例1' },
          { filename: 'typography/weight-2.jpg', alt: '字重示例2' },
          { filename: 'typography/weight-3.jpg', alt: '字重示例3' },
          { filename: 'typography/weight-4.jpg', alt: '字重示例4' },
          // 字体
          { filename: 'typography/font-1.jpg', alt: '字体示例1' },
          { filename: 'typography/font-2.jpg', alt: '字体示例2' },
          { filename: 'typography/font-3.jpg', alt: '字体示例3' },
          { filename: 'typography/font-4.jpg', alt: '字体示例4' }
        ]
      },
      {
        title: '专业排版',
        description: '多样字体搭配设计排版和高美感底图，有效帮助创作者降低后期成本，提升直出效率',
        images: [
          // 手写字体+手绘插画
          { filename: 'typography/handwriting-1.jpg', alt: '手写字体示例1' },
          { filename: 'typography/handwriting-2.jpg', alt: '手写字体示例2' },
          { filename: 'typography/handwriting-3.jpg', alt: '手写字体示例3' },
          // 创意字体+矢量插画
          { filename: 'typography/creative-1.jpg', alt: '创意字体示例1' },
          { filename: 'typography/creative-2.jpg', alt: '创意字体示例2' },
          { filename: 'typography/creative-3.jpg', alt: '创意字体示例3' },
          // 常规字体+写实摄影
          { filename: 'typography/regular-1.jpg', alt: '常规字体示例1' },
          { filename: 'typography/regular-2.jpg', alt: '常规字体示例2' },
          { filename: 'typography/regular-3.jpg', alt: '常规字体示例3' }
        ]
      }
    ]
  }
];
</script>

<style scoped>
.section-header {
  display: flex;
  align-items: center;
  margin-bottom: 25px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

.section-number {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  background-color: #0066cc;
  color: white;
  border-radius: 50%;
  margin-right: 15px;
  font-weight: 600;
  font-size: 1.2rem;
}

.section-title {
  font-size: 1.8rem;
  color: #333;
  font-weight: 600;
}

.feature-grid {
  display: flex;
  flex-direction: column;
  gap: 40px;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  padding: 35px;
  width: 100%;
}

.feature-card h3 {
  font-size: 1.8rem;
  margin-bottom: 20px;
  color: #333;
  display: flex;
  align-items: center;
}

.feature-card h3 span {
  color: #0066cc;
  margin-right: 12px;
  font-weight: 600;
}

.feature-card p {
  color: #666;
  margin-bottom: 25px;
  font-size: 1.2rem;
  line-height: 1.6;
}

.sub-feature {
  margin-top: 35px;
  padding-top: 35px;
  border-top: 1px solid #eee;
}

.sub-feature h4 {
  font-size: 1.4rem;
  color: #444;
  margin-bottom: 15px;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 25px;
  margin-top: 20px;
}

.image-item {
  position: relative;
  cursor: pointer;
  overflow: hidden;
  border-radius: 8px;
  background-color: #f5f5f5;
  aspect-ratio: 16/9;
}

.image-item img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.image-item:hover img {
  transform: scale(1.02);
}

.image-item::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.1);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.image-item:hover::after {
  opacity: 1;
}

@media (max-width: 1200px) {
  .feature-grid {
    padding: 0 20px;
  }
  
  .image-grid {
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  }
}

@media (max-width: 768px) {
  .feature-card {
    padding: 25px;
  }

  .image-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .image-grid {
    grid-template-columns: 1fr;
  }
  
  .feature-card h3 {
    font-size: 1.5rem;
  }
}
</style> 