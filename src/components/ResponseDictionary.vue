<template>
  <section id="response-dictionary">
    <div class="section-header">
      <div class="section-number">3</div>
      <h2 class="section-title">响应词典</h2>
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
          </div>
        </div>
      </div>
    </div>

    <div class="feature-grid">
      <div v-for="feature in features" 
           :key="feature.id" 
           class="feature-card"
           :id="`feature-${feature.id}`">
        <h3><span>{{ feature.title }}</span></h3>
        <p>{{ feature.description }}</p>
        
        <div class="image-grid">
          <div v-for="(item, index) in feature.items" 
               :key="index" 
               class="image-item"
               @click="openPreview(feature.items, index)">
            <div class="category-label">{{ item.name }}</div>
            <div class="image-wrapper">
              <img :src="getImageUrl(item.filename)" 
                   :alt="item.name" 
                   loading="lazy">
              <div class="image-overlay">
                <div class="image-title">{{ item.name }}</div>
                <div class="image-description">{{ item.description }}</div>
              </div>
            </div>
            <div class="image-caption">
              <div class="image-title">{{ item.name }}</div>
              <div class="image-description">{{ item.description }}</div>
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

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import ImagePreview from './ImagePreview.vue'

const getImageUrl = (filename: string) => {
  return `https://jimeng-image.iaiuse.com/3.0/response-directonary/${filename}`
}

// 图片预览相关状态
const isPreviewVisible = ref(false)
const previewImages = ref([])
const previewIndex = ref(0)

// 打开预览
const openPreview = (items: any[], index: number) => {
  previewImages.value = items.map(item => ({
    src: getImageUrl(item.filename),
    title: item.name,
    description: item.description,
    alt: item.alt
  }))
  previewIndex.value = index
  isPreviewVisible.value = true
}

// 关闭预览
const closePreview = () => {
  isPreviewVisible.value = false
}

// 浮动导航相关
const showFloatingNav = ref(false)
const activeSection = ref('')

// 滚动到指定区域
const scrollToSection = (sectionId: string) => {
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

const features = [
  {
    id: 1,
    title: '热门词',
    description: '当前最受欢迎的响应词，适合快速生成高质量图像',
    items: [
      { 
        name: '90年代动画', 
        description: '经典90年代日本动画风格，带有独特的复古画风和色彩处理，突出年代感和怀旧氛围',
        filename: 'hot/90s-anime.webp',
        alt: '90年代动画风格'
      },
      { 
        name: '复古写实', 
        description: '美式复古写实风格，强调自然光影和生活化场景，呈现怀旧氛围和温暖色调',
        filename: 'hot/american-candid.webp',
        alt: '美式复古写实'
      },
      { 
        name: '蓝调胶片', 
        description: '蓝色调为主的胶片效果，营造冷静沉稳的氛围，适合展现城市与人文场景',
        filename: 'hot/blue-tone.webp',
        alt: '蓝调胶片风格'
      },
      { 
        name: '朦胧美学', 
        description: '柔和虚化的艺术效果，通过模糊和光晕创造梦幻般的视觉体验，突出氛围感',
        filename: 'hot/blur-aesthetic.webp',
        alt: '朦胧艺术效果'
      },
      { 
        name: '手绘素描', 
        description: '手绘素描风格的插画效果，强调线条的流畅性和层次感，适合创作艺术插画',
        filename: 'hot/book-sketch.webp',
        alt: '手绘素描风格'
      },
      { 
        name: '生活随拍', 
        description: '自然随性的生活纪实风格，捕捉真实瞬间，呈现日常生活中的温暖与活力',
        filename: 'hot/candid.webp',
        alt: '生活随拍风格'
      },
      { 
        name: '冷色调', 
        description: '以冷色调为主的视觉效果，营造冷静克制的氛围，适合展现都市感和科技感',
        filename: 'hot/cold-tone.webp',
        alt: '冷色调效果'
      },
      { 
        name: '可爱卡通', 
        description: '可爱风格的卡通画效果，强调角色的萌态和画面的趣味性，适合儿童向内容',
        filename: 'hot/cute-kawaii.webp',
        alt: '可爱卡通风格'
      },
      { 
        name: '胶片闪光', 
        description: '复古胶片配合闪光灯效果，营造强烈的光影对比，突出主体和戏剧性效果',
        filename: 'hot/film-flash.webp',
        alt: '胶片闪光效果'
      },
      { 
        name: '扁平插画', 
        description: '现代扁平化插画风格，简约清新的设计语言，适合商业插画和品牌设计',
        filename: 'hot/flat-illustration.webp',
        alt: '扁平插画风格'
      },
      { 
        name: '高对比度', 
        description: '强烈的明暗对比效果，突出画面的戏剧性和视觉冲击力，适合创意摄影',
        filename: 'hot/high-contrast.webp',
        alt: '高对比度效果'
      },
      { 
        name: '冰晶效果', 
        description: '晶莹剔透的冰晶视觉效果，展现材质的通透感和光线折射，适合产品展示',
        filename: 'hot/ice-crystal.webp',
        alt: '冰晶视觉效果'
      },
      { 
        name: 'INS风格', 
        description: '典型的Instagram摄影风格，注重色调的统一性和画面构图，突出生活美学',
        filename: 'hot/ins-style.webp',
        alt: 'Instagram风格'
      },
      { 
        name: '复古网感', 
        description: '互联网早期的复古设计风格，融合像素感和赛博朋克元素，展现科技感',
        filename: 'hot/internet-nostalgia.webp',
        alt: '复古网络风格'
      },
      { 
        name: '可爱清新', 
        description: '温馨可爱的清新风格，柔和的色调搭配，适合少女向内容和温暖场景',
        filename: 'hot/kawaii.webp',
        alt: '可爱清新风格'
      },
      { 
        name: '液态金属', 
        description: '流动的金属质感效果，展现材质的光泽感和未来感，适合科技主题创作',
        filename: 'hot/liquid-metal.webp',
        alt: '液态金属效果'
      },
      { 
        name: '中国水墨', 
        description: '传统中国水墨画风格，强调笔触的韵律感和水墨晕染效果，展现东方美学',
        filename: 'hot/nakada-ikumi.webp',
        alt: '中国水墨风格'
      },
      { 
        name: '九宫格表情', 
        description: '多格漫画风格的表情包设计，适合创作有趣的角色表情和情绪展现',
        filename: 'hot/nine-grid-emoji.webp',
        alt: '九宫格表情包'
      },
      { 
        name: '复古照片', 
        description: '老式照片效果，呈现年代感和历史感，适合创作怀旧主题作品',
        filename: 'hot/old-photo.webp',
        alt: '复古照片效果'
      },
      { 
        name: '过曝对比', 
        description: '强烈的过曝效果配合高对比度，创造独特的光影氛围，突出主题',
        filename: 'hot/overexposed-contrast.webp',
        alt: '过曝对比效果'
      },
      { 
        name: '复古漫画', 
        description: '经典复古漫画风格，强调线条和网点的质感，展现怀旧的艺术效果',
        filename: 'hot/retro-manga.webp',
        alt: '复古漫画风格'
      },
      { 
        name: '复古快照', 
        description: '即时拍摄的复古照片效果，保留胶片相机的独特质感，展现生活记录',
        filename: 'hot/retro-snapshot.webp',
        alt: '复古快照效果'
      },
      { 
        name: '复古闪光', 
        description: '带有闪光效果的复古风格，营造怀旧氛围，适合创作复古主题作品',
        filename: 'hot/retro-sparkle.webp',
        alt: '复古闪光效果'
      },
      { 
        name: '少女漫画', 
        description: '日本少女漫画风格，细腻的人物刻画和情感表现，适合浪漫题材创作',
        filename: 'hot/shoujo-manga.webp',
        alt: '少女漫画风格'
      },
      { 
        name: '昭和复古', 
        description: '日本昭和时代的复古风格，展现特定年代的生活氛围和文化特色',
        filename: 'hot/showa-retro.webp',
        alt: '昭和复古风格'
      },
      { 
        name: '欧式复古', 
        description: '欧洲古典艺术风格，强调光影和构图的戏剧性，展现优雅复古的氛围',
        filename: 'hot/vintage-europea...ok.webp',
        alt: '欧式复古风格'
      },
      { 
        name: '复古童书', 
        description: '老式儿童书籍插画风格，温暖细腻的手绘效果，适合儿童主题创作',
        filename: 'hot/vintage-kids-book.webp',
        alt: '复古童书风格'
      },
      { 
        name: '鲜艳胶片', 
        description: '色彩鲜明的胶片效果，突出画面的色彩饱和度，营造活力氛围',
        filename: 'hot/vivid-film.webp',
        alt: '鲜艳胶片效果'
      },
      { 
        name: 'X光片', 
        description: 'X光片风格的视觉效果，展现物体的内部结构，创造独特的艺术效果',
        filename: 'hot/x-ray.webp',
        alt: 'X光片效果'
      },
      { 
        name: '四格漫画', 
        description: '日本四格漫画风格，简洁有趣的故事表现形式，适合创作短篇漫画',
        filename: 'hot/yonkoma-manga.webp',
        alt: '四格漫画风格'
      }
    ]
  },
  {
    id: 2,
    title: '美学词',
    description: '不同美学风格的响应词，适合特定艺术风格创作',
    items: [
      { 
        name: '极简', 
        description: '简约而不简单，突出设计感',
        filename: 'aesthetic/minimal.webp',
        alt: '极简风格'
      },
      { 
        name: '复古', 
        description: '怀旧风格，突出年代感',
        filename: 'aesthetic/retro.webp',
        alt: '复古风格'
      },
      { 
        name: '现代', 
        description: '时尚简约，突出时代感',
        filename: 'aesthetic/modern.webp',
        alt: '现代风格'
      },
      { 
        name: '未来', 
        description: '科技感十足，突出未来感',
        filename: 'aesthetic/future.webp',
        alt: '未来风格'
      },
      { 
        name: '自然', 
        description: '清新自然，突出生态感',
        filename: 'aesthetic/nature.webp',
        alt: '自然风格'
      },
      { 
        name: '工业', 
        description: '硬朗风格，突出机械感',
        filename: 'aesthetic/industrial.webp',
        alt: '工业风格'
      },
      { 
        name: '科技', 
        description: '高科技感，突出未来感',
        filename: 'aesthetic/tech.webp',
        alt: '科技风格'
      },
      { 
        name: '艺术', 
        description: '艺术气息，突出创意感',
        filename: 'aesthetic/art.webp',
        alt: '艺术风格'
      }
    ]
  },
  {
    id: 3,
    title: '潮流风格',
    description: '当前流行的艺术和设计风格，适合紧跟潮流创作',
    items: [
      { 
        name: '赛博朋克', 
        description: '未来科技与复古元素的碰撞',
        filename: 'trend/cyberpunk.webp',
        alt: '赛博朋克风格'
      },
      { 
        name: '蒸汽朋克', 
        description: '维多利亚时代与蒸汽机械的融合',
        filename: 'trend/steampunk.webp',
        alt: '蒸汽朋克风格'
      },
      { 
        name: '极简主义', 
        description: '简约至上的设计理念',
        filename: 'trend/minimalism.webp',
        alt: '极简主义'
      },
      { 
        name: '波普艺术', 
        description: '流行文化与艺术的结合',
        filename: 'trend/pop.webp',
        alt: '波普艺术'
      },
      { 
        name: '新艺术', 
        description: '自然与装饰艺术的融合',
        filename: 'trend/art-nouveau.webp',
        alt: '新艺术风格'
      },
      { 
        name: '后现代', 
        description: '打破传统，追求创新',
        filename: 'trend/postmodern.webp',
        alt: '后现代风格'
      }
    ]
  },
  {
    id: 4,
    title: '影像',
    description: '专业摄影和电影镜头语言，适合影视风格创作',
    items: [
      { 
        name: '大特写', 
        description: '突出细节表情，强调主体特征',
        filename: 'image/close-up.webp',
        alt: '大特写镜头'
      },
      { 
        name: '特写', 
        description: '刻画人物情绪，展现细节特征',
        filename: 'image/close.webp',
        alt: '特写镜头'
      },
      { 
        name: '近景', 
        description: '强调主体特征，突出人物表情',
        filename: 'image/near.webp',
        alt: '近景镜头'
      },
      { 
        name: '中景', 
        description: '展现人物动作，突出场景氛围',
        filename: 'image/medium.webp',
        alt: '中景镜头'
      },
      { 
        name: '全景', 
        description: '完整场景呈现，突出环境氛围',
        filename: 'image/full.webp',
        alt: '全景镜头'
      },
      { 
        name: '大远景', 
        description: '宏大场面展示，突出空间感',
        filename: 'image/wide.webp',
        alt: '大远景镜头'
      }
    ]
  },
  {
    id: 5,
    title: '设计',
    description: '专业设计领域的风格和技巧，适合设计类创作',
    items: [
      { 
        name: '平面设计', 
        description: '视觉传达的艺术表现',
        filename: 'design/graphic.webp',
        alt: '平面设计'
      },
      { 
        name: 'UI设计', 
        description: '用户界面的交互设计',
        filename: 'design/ui.webp',
        alt: 'UI设计'
      },
      { 
        name: '包装设计', 
        description: '产品包装的视觉设计',
        filename: 'design/packaging.webp',
        alt: '包装设计'
      },
      { 
        name: '品牌设计', 
        description: '品牌形象的视觉传达',
        filename: 'design/brand.webp',
        alt: '品牌设计'
      },
      { 
        name: '海报设计', 
        description: '宣传海报的创意设计',
        filename: 'design/poster.webp',
        alt: '海报设计'
      }
    ]
  },
  {
    id: 6,
    title: '艺术',
    description: '传统和现代艺术风格，适合艺术类创作',
    items: [
      { 
        name: '油画', 
        description: '传统油画的艺术表现',
        filename: 'art/oil.webp',
        alt: '油画风格'
      },
      { 
        name: '水彩', 
        description: '水彩画的艺术表现',
        filename: 'art/watercolor.webp',
        alt: '水彩风格'
      },
      { 
        name: '素描', 
        description: '素描的艺术表现',
        filename: 'art/sketch.webp',
        alt: '素描风格'
      },
      { 
        name: '插画', 
        description: '插画的艺术表现',
        filename: 'art/illustration.webp',
        alt: '插画风格'
      },
      { 
        name: '漫画', 
        description: '漫画的艺术表现',
        filename: 'art/comic.webp',
        alt: '漫画风格'
      }
    ]
  },
  {
    id: 7,
    title: '材质',
    description: '不同材质的表现效果，适合材质渲染创作',
    items: [
      { 
        name: '金属', 
        description: '金属材质的表现效果',
        filename: 'material/metal.webp',
        alt: '金属材质'
      },
      { 
        name: '玻璃', 
        description: '玻璃材质的表现效果',
        filename: 'material/glass.webp',
        alt: '玻璃材质'
      },
      { 
        name: '木材', 
        description: '木材材质的表现效果',
        filename: 'material/wood.webp',
        alt: '木材材质'
      },
      { 
        name: '布料', 
        description: '布料材质的表现效果',
        filename: 'material/fabric.webp',
        alt: '布料材质'
      },
      { 
        name: '塑料', 
        description: '塑料材质的表现效果',
        filename: 'material/plastic.webp',
        alt: '塑料材质'
      }
    ]
  }
]
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

/* 浮动导航样式 */
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

.nav-item:hover {
  background: #f5f9ff;
  border-left-color: #0066cc;
}

.nav-item:hover .nav-item-title {
  color: #0066cc;
}

.nav-item.active {
  background: #f5f9ff;
  border-left-color: #0066cc;
}

.nav-item.active .nav-item-title {
  color: #0066cc;
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
}

@media (max-width: 768px) {
  .floating-nav {
    display: none;
  }
}
</style> 