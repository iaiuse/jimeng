<template>
  <section id="model-highlights">
    <div class="section-header">
      <div class="section-number">1</div>
      <h2 class="section-title">模型亮点</h2>
    </div>
    
    <!-- 添加浮动导航菜单 -->
    <div class="floating-nav" :class="{ 'is-visible': showFloatingNav }">
      <div class="nav-items">
        <div v-for="feature in features" 
             :key="feature.id" 
             class="nav-item"
             :class="{ 'active': activeSection === `feature-${feature.id}` }"
             @click="scrollToSection(`feature-${feature.id}`)">
          <div class="nav-item-content">
            <div class="nav-item-title">{{ feature.title }}</div>
            <div class="nav-item-subtitle">{{ feature.subtitle }}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="feature-grid">
      <div v-for="feature in features" 
           :key="feature.id" 
           class="feature-card"
           :id="`feature-${feature.id}`">
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
              <div class="category-label">{{ image.alt }}</div>
              <div class="image-wrapper">
                <img :src="getImageUrl(image.filename)" 
                     :alt="image.alt" 
                     loading="lazy">
                <div class="image-overlay">
                  <div class="image-title">{{ image.alt }}</div>
                  <div class="image-description">{{ image.description }}</div>
                </div>
              </div>
              <div class="image-caption">
                <div class="image-title">{{ image.alt }}</div>
                <div class="image-description">{{ image.description }}</div>
              </div>
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
import { ref, onMounted, onUnmounted } from 'vue'
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
          { 
            filename: 'realism/texture-1.png', 
            alt: '皮肤质感', 
            description: '精准还原真实皮肤纹理和质地' 
          },
          { 
            filename: 'realism/texture-2.png', 
            alt: '材质细节', 
            description: '准确表现不同材质的细节特征' 
          },
          { 
            filename: 'realism/texture-3.png', 
            alt: '光影质感', 
            description: '自然的光影过渡和材质反射' 
          }
        ]
      },
      {
        title: '情绪真实',
        description: '去僵硬感、摆拍感、ai眼神空洞感，情绪细腻有感染力',
        images: [
          { 
            filename: 'realism/emotion-1.png', 
            alt: '自然表情', 
            description: '真实自然的面部表情和情绪' 
          },
          { 
            filename: 'realism/emotion-2.png', 
            alt: '眼神传神', 
            description: '富有生命力的眼神表现' 
          },
          { 
            filename: 'realism/emotion-3.png', 
            alt: '情绪张力', 
            description: '细腻的情感状态表达' 
          }
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
          { 
            filename: 'hd/scene-1.png', 
            alt: '1K分辨率', 
            description: '基础分辨率输出，细节清晰' 
          },
          { 
            filename: 'hd/scene-2.png', 
            alt: '1.5K分辨率', 
            description: '更高分辨率，细节更丰富' 
          },
          { 
            filename: 'hd/scene-3.png', 
            alt: '2K分辨率', 
            description: '超高清输出，结构准确度提升' 
          }
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
        title: '电影类型',
        description: '准确理解不同类型电影的视觉风格与氛围',
        images: [
          { filename: 'pro/film/type-1.jpg', alt: 'CG概念', description: '科幻场景的视觉表现' },
          { filename: 'pro/film/type-2.jpg', alt: '电影剧照', description: '戏剧性场景呈现' },
          { filename: 'pro/film/type-3.jpg', alt: '恐怖片', description: '恐怖氛围营造' },
          { filename: 'pro/film/type-4.jpg', alt: '纪录片', description: '真实纪实风格' },
          { filename: 'pro/film/type-5.jpg', alt: '爱情片', description: '浪漫情感表达' },
          { filename: 'pro/film/type-6.jpg', alt: '公路片', description: '旅途探索主题' }
        ]
      },
      {
        title: '镜头语言',
        description: '精准控制镜头视角、景别、焦段等专业摄影参数',
        images: [
          { filename: 'pro/film/lens-1.jpeg', alt: '大特写', description: '突出细节表情' },
          { filename: 'pro/film/lens-2.jpeg', alt: '特写', description: '刻画人物情绪' },
          { filename: 'pro/film/lens-3.jpeg', alt: '近景', description: '强调主体特征' },
          { filename: 'pro/film/lens-4.jpeg', alt: '中景', description: '展现人物动作' },
          { filename: 'pro/film/lens-5.jpeg', alt: '全景', description: '完整场景呈现' },
          { filename: 'pro/film/lens-6.jpeg', alt: '大远景', description: '宏大场面展示' },
          { filename: 'pro/film/lens-7.jpeg', alt: '背面', description: '背影氛围营造' },
          { filename: 'pro/film/lens-8.jpeg', alt: '浅景深', description: '主体虚实对比' },
          { filename: 'pro/film/lens-9.jpeg', alt: '动态模糊', description: '运动感表现' },
          { filename: 'pro/film/lens-10.jpeg', alt: '柔焦镜头', description: '柔美效果渲染' },
          { filename: 'pro/film/lens-11.jpeg', alt: '猫眼镜头', description: '变形视觉效果' },
          { filename: 'pro/film/lens-12.jpeg', alt: '鱼眼镜头', description: '超广角视角' }
        ]
      },
      {
        title: '动漫场景',
        description: '风格更多元、细节更丰富、色调更统一，不再有2.1的"抠图感"',
        images: [
          { 
            filename: 'pro/anime-1.jpg', 
            alt: '写实动漫', 
            description: '精致的写实风格动漫角色' 
          },
          { 
            filename: 'pro/anime-2.jpg', 
            alt: '二次元风格', 
            description: '典型二次元美术风格' 
          },
          { 
            filename: 'pro/anime-3.jpg', 
            alt: '赛璐璐风格', 
            description: '传统赛璐璐动画风格' 
          },
          { 
            filename: 'pro/anime-4.jpg', 
            alt: '水彩风格', 
            description: '柔和的水彩画风动漫' 
          },
          { 
            filename: 'pro/anime-5.jpg', 
            alt: '插画风格', 
            description: '现代插画风格作品' 
          }
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

// 浮动导航相关
const showFloatingNav = ref(false)
const activeSection = ref('')

// 滚动到指定区域
const scrollToSection = (sectionId) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

// 检查滚动位置并更新导航状态
const checkScroll = () => {
  // 显示/隐藏浮动导航
  showFloatingNav.value = window.scrollY > 200

  // 更新当前激活的区域
  const sections = features.map(f => `feature-${f.id}`)
  for (const sectionId of sections) {
    const element = document.getElementById(sectionId)
    if (element) {
      const rect = element.getBoundingClientRect()
      if (rect.top <= 100 && rect.bottom >= 100) {
        activeSection.value = sectionId
        break
      }
    }
  }
}

// 监听滚动事件
onMounted(() => {
  window.addEventListener('scroll', checkScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', checkScroll)
})
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

.sub-feature p {
  color: #666;
  margin-bottom: 25px;
  font-size: 1.1rem;
  line-height: 1.6;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 25px;
  margin-top: 20px;
}

.image-item {
  position: relative;
  cursor: pointer;
  overflow: visible;
  border-radius: 8px;
  background-color: white;
  transition: transform 0.3s ease;
}

.image-wrapper {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  aspect-ratio: 16/9;
  background-color: #f5f5f5;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.image-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.image-item:hover {
  transform: translateY(-2px);
}

.image-item:hover img {
  transform: scale(1.05);
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  padding: 20px;
  color: white;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.image-item:hover .image-overlay {
  opacity: 1;
}

.image-caption {
  padding: 12px 0;
  text-align: center;
}

.image-title {
  font-size: 1rem;
  font-weight: 500;
  color: #333;
  margin-bottom: 4px;
}

.image-description {
  font-size: 0.9rem;
  color: #666;
  line-height: 1.4;
}

/* 分类标签样式 */
.category-label {
  position: absolute;
  top: 10px;
  left: 10px;
  background: rgba(0,0,0,0.6);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  z-index: 1;
}

/* 响应式调整 */
@media (max-width: 1200px) {
  .feature-grid {
    padding: 0 20px;
  }
  
  .image-grid {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 20px;
  }
}

@media (max-width: 768px) {
  .feature-card {
    padding: 25px;
  }
  
  .image-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
  }
  
  .image-caption {
    padding: 8px 0;
  }

  .image-title {
    font-size: 0.95rem;
  }

  .image-description {
    font-size: 0.85rem;
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

/* 修改浮动导航样式 */
.floating-nav {
  position: fixed;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  padding: 15px 0;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 100;
  min-width: 200px;
}

.floating-nav.is-visible {
  opacity: 1;
  visibility: visible;
}

.nav-items {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.nav-item {
  padding: 12px 20px;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  border-left: 3px solid transparent;
}

.nav-item-content {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.nav-item-title {
  color: #333;
  font-size: 1rem;
  font-weight: 500;
  transition: color 0.2s ease;
}

.nav-item-subtitle {
  color: #666;
  font-size: 0.85rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: color 0.2s ease;
}

.nav-item:hover {
  background: #f5f9ff;
  border-left-color: #0066cc;
}

.nav-item:hover .nav-item-title {
  color: #0066cc;
}

.nav-item:hover .nav-item-subtitle {
  color: #0066cc;
}

.nav-item.active {
  background: #f5f9ff;
  border-left-color: #0066cc;
}

.nav-item.active .nav-item-title {
  color: #0066cc;
}

.nav-item.active .nav-item-subtitle {
  color: #0066cc;
}

/* 响应式调整 */
@media (max-width: 1400px) {
  .floating-nav {
    right: 10px;
    min-width: 180px;
  }
  
  .nav-item {
    padding: 10px 15px;
  }

  .nav-item-title {
    font-size: 0.95rem;
  }

  .nav-item-subtitle {
    font-size: 0.8rem;
  }
}

@media (max-width: 768px) {
  .floating-nav {
    display: none; /* 在移动端隐藏浮动导航 */
  }
}
</style> 