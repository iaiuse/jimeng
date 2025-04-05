<template>
  <section id="response-dictionary">
    <div class="section-header">
      <div class="section-number">3</div>
      <h2 class="section-title">响应词典</h2>
    </div>
    
    <!-- 添加浮动导航菜单 -->
    <div class="floating-nav" :class="{ 'is-visible': showFloatingNav }">
      <div class="nav-items">
        <div v-for="category in categories" 
             :key="category.id" 
             class="nav-item"
             :class="{ 'active': activeSection === `category-${category.id}` }"
             @click="scrollToSection(`category-${category.id}`)">
          <div class="nav-item-content">
            <div class="nav-item-title">{{ category.name }}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="feature-grid">
      <div v-for="category in categories" 
           :key="category.id" 
           class="feature-card"
           :id="`category-${category.id}`">
        <h3><span>{{ category.name }}</span></h3>
        
        <div class="image-grid">
          <div v-for="(item, index) in category.items" 
               :key="index" 
               class="image-item"
               @click="openPreview(category.items, index)">
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

const dictionaryTabs = [
  { id: 'hot', name: '热门词' },
  { id: 'aesthetic', name: '美学词' },
  { id: 'trend', name: '潮流风格' },
  { id: 'image', name: '影像' },
  { id: 'design', name: '设计' },
  { id: 'art', name: '艺术' },
  { id: 'material', name: '材质' }
]

const currentDictionaryTab = ref('hot')

const dictionaryContents = {
  hot: [
    { 
      name: '胶片，闪光灯拍摄，过曝，压暗周围颜色，明影加重', 
      image: '/api/placeholder/180/180',
      description: '通过胶片和闪光灯拍摄，营造强烈的光影对比效果',
      filename: 'response-dictionary/hot/film-flash.webp',
      alt: '胶片闪光效果'
    },
    { 
      name: '过曝，强对比，胶片摄影，闪光灯拍摄，极简', 
      image: '/api/placeholder/180/180',
      description: '利用过曝和强对比突出主体，营造极简风格',
      filename: 'response-dictionary/hot/overexposed-contrast.webp',
      alt: '高对比胶片风格'
    },
    { 
      name: '过曝，冷色调，光影氛围，强对比', 
      image: '/api/placeholder/180/180',
      description: '冷色调配合过曝效果，创造独特光影氛围',
      filename: 'response-dictionary/hot/cold-tone.webp',
      alt: '冷色调光影'
    },
    { 
      name: '蓝色调，胶片质感，氛围感，极简', 
      image: '/api/placeholder/180/180',
      description: '蓝色调胶片效果，突出简约氛围',
      filename: 'response-dictionary/hot/blue-tone.webp',
      alt: '蓝调胶片'
    },
    { 
      name: '液态金属', 
      image: '/api/placeholder/180/180',
      description: '展现流动的金属质感和光泽',
      filename: 'response-dictionary/hot/liquid-metal.webp',
      alt: '液态金属效果'
    },
    { 
      name: '水晶xx，由冰晶雕琢而成，电影级光线', 
      image: '/api/placeholder/180/180',
      description: '冰晶质感与电影级打光的结合',
      filename: 'response-dictionary/hot/ice-crystal.webp',
      alt: '冰晶光效'
    },
    { 
      name: 'ins风', 
      image: '/api/placeholder/180/180',
      description: '典型的Instagram风格影像',
      filename: 'response-dictionary/hot/ins-style.webp',
      alt: 'Instagram风格'
    },
    { 
      name: '90s Japanese anime', 
      image: '/api/placeholder/180/180',
      description: '90年代日本动画风格',
      filename: 'response-dictionary/hot/90s-anime.webp',
      alt: '90年代动画'
    },
    { 
      name: '古早日漫风格', 
      image: '/api/placeholder/180/180',
      description: '复古日本漫画艺术风格',
      filename: 'response-dictionary/hot/retro-manga.webp',
      alt: '复古漫画'
    },
    { 
      name: '强对比，氛围感', 
      image: '/api/placeholder/180/180',
      description: '强烈的明暗对比营造特殊氛围',
      filename: 'response-dictionary/hot/high-contrast.webp',
      alt: '强对比氛围'
    },
    { 
      name: '昭和复古', 
      image: '/api/placeholder/180/180',
      description: '日本昭和时代的复古风格',
      filename: 'response-dictionary/hot/showa-retro.webp',
      alt: '昭和风格'
    },
    { 
      name: '生命力，高饱和度，高对比，胶片', 
      image: '/api/placeholder/180/180',
      description: '充满生命力的高饱和度胶片效果',
      filename: 'response-dictionary/hot/vivid-film.webp',
      alt: '生命力胶片'
    },
    { 
      name: '抓拍', 
      image: '/api/placeholder/180/180',
      description: '自然真实的抓拍风格',
      filename: 'response-dictionary/hot/candid.webp',
      alt: '抓拍风格'
    },
    { 
      name: '老照片，胶片感，褪色，低饱和度', 
      image: '/api/placeholder/180/180',
      description: '复古老照片效果，低饱和褪色处理',
      filename: 'response-dictionary/hot/old-photo.webp',
      alt: '老照片效果'
    },
    { 
      name: '拍摄模糊 失焦美学', 
      image: '/api/placeholder/180/180',
      description: '艺术性的模糊失焦效果',
      filename: 'response-dictionary/hot/blur-aesthetic.webp',
      alt: '失焦美学'
    },
    { 
      name: 'Retro Snapshot', 
      image: '/api/placeholder/180/180',
      description: '复古快照风格摄影',
      filename: 'response-dictionary/hot/retro-snapshot.webp',
      alt: '复古快照'
    },
    { 
      name: '美式抓拍风', 
      image: '/api/placeholder/180/180',
      description: '美国街头摄影风格',
      filename: 'response-dictionary/hot/american-candid.webp',
      alt: '美式街拍'
    },
    { 
      name: 'x光片', 
      image: '/api/placeholder/180/180',
      description: 'X光片透视效果',
      filename: 'response-dictionary/hot/x-ray.webp',
      alt: 'X光效果'
    },
    { 
      name: '美式复古儿童书籍', 
      image: '/api/placeholder/180/180',
      description: '美国复古儿童绘本风格',
      filename: 'response-dictionary/hot/vintage-kids-book.webp',
      alt: '复古童书'
    },
    { 
      name: '可爱萌系', 
      image: '/api/placeholder/180/180',
      description: '可爱风格插画',
      filename: 'response-dictionary/hot/cute-kawaii.webp',
      alt: '萌系风格'
    },
    { 
      name: '少女漫画', 
      image: '/api/placeholder/180/180',
      description: '少女漫画艺术风格',
      filename: 'response-dictionary/hot/shoujo-manga.webp',
      alt: '少女漫画'
    },
    { 
      name: 'Nakada Ikumi', 
      image: '/api/placeholder/180/180',
      description: 'Nakada Ikumi艺术风格',
      filename: 'response-dictionary/hot/nakada-ikumi.webp',
      alt: '中田郁美风格'
    },
    { 
      name: '老式绘本 欧美绘本', 
      image: '/api/placeholder/180/180',
      description: '欧美复古绘本艺术风格',
      filename: 'response-dictionary/hot/vintage-european-book.webp',
      alt: '欧式绘本'
    },
    { 
      name: '卡哇伊', 
      image: '/api/placeholder/180/180',
      description: '日系可爱风格',
      filename: 'response-dictionary/hot/kawaii.webp',
      alt: '卡哇伊风格'
    },
    { 
      name: '高饱和度，扁平插画风格，粗线条', 
      image: '/api/placeholder/180/180',
      description: '高饱和扁平化插画设计',
      filename: 'response-dictionary/hot/flat-illustration.webp',
      alt: '扁平插画'
    },
    { 
      name: '互联网怀旧风', 
      image: '/api/placeholder/180/180',
      description: '早期互联网复古风格',
      filename: 'response-dictionary/hot/internet-nostalgia.webp',
      alt: '网络复古'
    },
    { 
      name: '复古亮闪闪', 
      image: '/api/placeholder/180/180',
      description: '复古闪光效果设计',
      filename: 'response-dictionary/hot/retro-sparkle.webp',
      alt: '复古闪光'
    },
    { 
      name: '九宫格表情包', 
      image: '/api/placeholder/180/180',
      description: '九宫格式表情包设计',
      filename: 'response-dictionary/hot/nine-grid-emoji.webp',
      alt: '表情九宫格'
    },
    { 
      name: '绘本手稿风', 
      image: '/api/placeholder/180/180',
      description: '手绘绘本草稿风格',
      filename: 'response-dictionary/hot/book-sketch.webp',
      alt: '绘本手稿'
    },
    { 
      name: '古早四格漫画风', 
      image: '/api/placeholder/180/180',
      description: '传统四格漫画风格',
      filename: 'response-dictionary/hot/yonkoma-manga.webp',
      alt: '四格漫画'
    }
  ],
  aesthetic: [
    { 
      name: '极简', 
      image: '/api/placeholder/180/180',
      description: '简约而不简单，突出设计感',
      filename: 'aesthetic/minimal.webp'
    },
    { 
      name: '复古', 
      image: '/api/placeholder/180/180',
      description: '怀旧风格，突出年代感',
      filename: 'aesthetic/retro.webp'
    },
    { 
      name: '现代', 
      image: '/api/placeholder/180/180',
      description: '时尚简约，突出时代感',
      filename: 'aesthetic/modern.webp'
    },
    { 
      name: '未来', 
      image: '/api/placeholder/180/180',
      description: '科技感十足，突出未来感',
      filename: 'aesthetic/future.webp'
    },
    { 
      name: '自然', 
      image: '/api/placeholder/180/180',
      description: '清新自然，突出生态感',
      filename: 'aesthetic/nature.webp'
    },
    { 
      name: '工业', 
      image: '/api/placeholder/180/180',
      description: '硬朗风格，突出机械感',
      filename: 'aesthetic/industrial.webp'
    },
    { 
      name: '科技', 
      image: '/api/placeholder/180/180',
      description: '高科技感，突出未来感',
      filename: 'aesthetic/tech.webp'
    },
    { 
      name: '艺术', 
      image: '/api/placeholder/180/180',
      description: '艺术气息，突出创意感',
      filename: 'aesthetic/art.webp'
    }
  ],
  trend: [
    { 
      name: '赛博朋克', 
      image: '/api/placeholder/180/180',
      description: '未来科技与复古元素的碰撞',
      filename: 'trend/cyberpunk.webp'
    },
    { 
      name: '蒸汽朋克', 
      image: '/api/placeholder/180/180',
      description: '维多利亚时代与蒸汽机械的融合',
      filename: 'trend/steampunk.webp'
    },
    { 
      name: '极简主义', 
      image: '/api/placeholder/180/180',
      description: '简约至上的设计理念',
      filename: 'trend/minimalism.webp'
    },
    { 
      name: '波普艺术', 
      image: '/api/placeholder/180/180',
      description: '流行文化与艺术的结合',
      filename: 'trend/pop.webp'
    },
    { 
      name: '新艺术', 
      image: '/api/placeholder/180/180',
      description: '自然与装饰艺术的融合',
      filename: 'trend/art-nouveau.webp'
    },
    { 
      name: '后现代', 
      image: '/api/placeholder/180/180',
      description: '打破传统，追求创新',
      filename: 'trend/postmodern.webp'
    }
  ],
  image: [
    { 
      name: '大特写', 
      image: '/api/placeholder/180/180',
      description: '突出细节表情，强调主体特征',
      filename: 'image/close-up.webp'
    },
    { 
      name: '特写', 
      image: '/api/placeholder/180/180',
      description: '刻画人物情绪，展现细节特征',
      filename: 'image/close.webp'
    },
    { 
      name: '近景', 
      image: '/api/placeholder/180/180',
      description: '强调主体特征，突出人物表情',
      filename: 'image/near.webp'
    },
    { 
      name: '中景', 
      image: '/api/placeholder/180/180',
      description: '展现人物动作，突出场景氛围',
      filename: 'image/medium.webp'
    },
    { 
      name: '全景', 
      image: '/api/placeholder/180/180',
      description: '完整场景呈现，突出环境氛围',
      filename: 'image/full.webp'
    },
    { 
      name: '大远景', 
      image: '/api/placeholder/180/180',
      description: '宏大场面展示，突出空间感',
      filename: 'image/wide.webp'
    }
  ],
  design: [
    { 
      name: '平面设计', 
      image: '/api/placeholder/180/180',
      description: '视觉传达的艺术表现',
      filename: 'design/graphic.webp'
    },
    { 
      name: 'UI设计', 
      image: '/api/placeholder/180/180',
      description: '用户界面的交互设计',
      filename: 'design/ui.webp'
    },
    { 
      name: '包装设计', 
      image: '/api/placeholder/180/180',
      description: '产品包装的视觉设计',
      filename: 'design/packaging.webp'
    },
    { 
      name: '品牌设计', 
      image: '/api/placeholder/180/180',
      description: '品牌形象的视觉传达',
      filename: 'design/brand.webp'
    },
    { 
      name: '海报设计', 
      image: '/api/placeholder/180/180',
      description: '宣传海报的创意设计',
      filename: 'design/poster.webp'
    }
  ],
  art: [
    { 
      name: '油画', 
      image: '/api/placeholder/180/180',
      description: '传统油画的艺术表现',
      filename: 'art/oil.webp'
    },
    { 
      name: '水彩', 
      image: '/api/placeholder/180/180',
      description: '水彩画的艺术表现',
      filename: 'art/watercolor.webp'
    },
    { 
      name: '素描', 
      image: '/api/placeholder/180/180',
      description: '素描的艺术表现',
      filename: 'art/sketch.webp'
    },
    { 
      name: '插画', 
      image: '/api/placeholder/180/180',
      description: '插画的艺术表现',
      filename: 'art/illustration.webp'
    },
    { 
      name: '漫画', 
      image: '/api/placeholder/180/180',
      description: '漫画的艺术表现',
      filename: 'art/comic.webp'
    }
  ],
  material: [
    { 
      name: '金属', 
      image: '/api/placeholder/180/180',
      description: '金属材质的表现效果',
      filename: 'material/metal.webp'
    },
    { 
      name: '玻璃', 
      image: '/api/placeholder/180/180',
      description: '玻璃材质的表现效果',
      filename: 'material/glass.webp'
    },
    { 
      name: '木材', 
      image: '/api/placeholder/180/180',
      description: '木材材质的表现效果',
      filename: 'material/wood.webp'
    },
    { 
      name: '布料', 
      image: '/api/placeholder/180/180',
      description: '布料材质的表现效果',
      filename: 'material/fabric.webp'
    },
    { 
      name: '塑料', 
      image: '/api/placeholder/180/180',
      description: '塑料材质的表现效果',
      filename: 'material/plastic.webp'
    }
  ]
}

const currentTabContent = computed(() => dictionaryContents[currentDictionaryTab.value])

const isPreviewVisible = ref(false)
const previewIndex = ref(0)

const previewImages = computed(() => 
  currentTabContent.value.map(item => ({
    src: `https://jimeng-image.iaiuse.com/3.0/${item.filename}`,
    title: item.name,
    description: item.description,
    alt: item.alt
  }))
)

const openPreview = (items: any[], index: number) => {
  previewImages.value = items.map(item => ({
    src: `https://jimeng-image.iaiuse.com/3.0/${item.filename}`,
    title: item.name,
    description: item.description,
    alt: item.alt
  }))
  previewIndex.value = index
  isPreviewVisible.value = true
}

const closePreview = () => {
  isPreviewVisible.value = false
}

const showFloatingNav = ref(false)
const activeSection = ref('')

const scrollToSection = (sectionId: string) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

const checkScroll = () => {
  showFloatingNav.value = window.scrollY > 200

  const sections = dictionaryTabs.map(c => `category-${c.id}`)
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

onMounted(() => {
  window.addEventListener('scroll', checkScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', checkScroll)
})

const getImageUrl = (filename: string) => {
  return `https://jimeng-image.iaiuse.com/3.0/${filename}`
}

const categories = [
  { 
    id: 'hot', 
    name: '热门词',
    items: dictionaryContents.hot
  },
  { 
    id: 'aesthetic', 
    name: '美学词',
    items: dictionaryContents.aesthetic
  },
  { 
    id: 'trend', 
    name: '潮流风格',
    items: dictionaryContents.trend
  },
  { 
    id: 'image', 
    name: '影像',
    items: dictionaryContents.image
  },
  { 
    id: 'design', 
    name: '设计',
    items: dictionaryContents.design
  },
  { 
    id: 'art', 
    name: '艺术',
    items: dictionaryContents.art
  },
  { 
    id: 'material', 
    name: '材质',
    items: dictionaryContents.material
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