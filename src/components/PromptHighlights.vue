<template>
  <section id="prompt-highlights">
    <div class="section-header">
      <div class="section-number">2</div>
      <h2 class="section-title">提示词秘籍</h2>
    </div>
    
    <!-- 浮动导航菜单 -->
    <div class="floating-nav" :class="{ 'is-visible': showFloatingNav }">
      <div class="nav-items">
        <div v-for="section in promptSections" 
             :key="section.id" 
             class="nav-item"
             :class="{ 'active': activeSection === `section-${section.id}` }"
             @click="scrollToSection(`section-${section.id}`)">
          <div class="nav-item-content">
            <div class="nav-item-title">{{ section.title }}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="feature-grid">
      <!-- 语言表达部分 -->
      <div class="feature-card" :id="`section-${promptSections[0].id}`">
        <h3><span>{{ promptSections[0].title }}</span></h3>
        <p>{{ promptSections[0].description }}</p>
        <div class="highlight-note">{{ promptSections[0].note }}</div>
        
        <div class="image-grid">
          <div v-for="(example, index) in promptSections[0].examples || []" 
               :key="index" 
               :class="[
                 'image-item',
                 { 'image-item-horizontal': example.filename === 'image004.webp' }
               ]"
               @click="openPreview(promptSections[0].examples || [], index)">
            <div class="category-label">
              <span v-for="tag in example.tags" :key="tag" class="example-tag">{{ tag }}</span>
            </div>
            <div class="image-wrapper" :class="{ 'horizontal-image': example.filename === 'image004.webp' }">
              <img :src="getImageUrl(example.filename)" :alt="example.alt" loading="lazy">
              <div class="image-overlay">
                <div class="image-title">{{ example.alt }}</div>
                <div class="image-description">{{ example.description }}</div>
              </div>
            </div>
            <div v-if="example.details" 
                 :class="[
                   'image-caption',
                   { 'horizontal-caption': example.filename === 'image004.webp' }
                 ]">
              <div class="detail-section" v-for="(value, key) in example.details" :key="key">
                <strong>{{ key }}：</strong>
                <span v-if="typeof value === 'string'">{{ value }}</span>
                <div v-else class="detail-content">
                  <div v-for="(item, itemKey) in value" :key="itemKey">
                    {{ typeof item === 'string' ? item : `${itemKey}: ${item}` }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 画面描述部分 -->
      <div class="feature-card" :id="`section-${promptSections[1].id}`">
        <h3><span>{{ promptSections[1].title }}</span></h3>
        <div class="description-points">
          <div v-for="point in promptSections[1].points" 
               :key="point.label" 
               class="point">
            <strong>{{ point.label }}：</strong>
            <span>{{ point.content }}</span>
          </div>
        </div>
      </div>

      <!-- 专业词汇部分 -->
      <div class="feature-card" :id="`section-${promptSections[2].id}`">
        <h3><span>{{ promptSections[2].title }}</span></h3>
        <div class="image-grid">
          <div v-for="(item, index) in promptSections[2].items || []" 
               :key="item.cn" 
               class="image-item"
               @click="openPreview(promptSections[2].items || [], index)">
            <div class="image-wrapper">
              <img :src="getImageUrl(item.filename)" :alt="item.alt" loading="lazy">
              <div class="image-overlay">
                <div class="image-title">{{ item.cn }}</div>
                <div class="image-description">{{ item.en }}</div>
              </div>
            </div>
            <div class="image-caption">
              <div class="vocab-pair">
                <span class="vocab-cn">{{ item.cn }}</span>
                <span class="vocab-en">{{ item.en }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 场景应用推荐 -->
      <div class="feature-card" id="section-applications">
        <h3><span>场景应用推荐</span></h3>
        <div class="image-grid">
          <div v-for="scene in sceneApplications" 
               :key="scene.id" 
               class="image-item">
            <div class="image-wrapper">
              <img :src="getImageUrl(scene.image)" :alt="scene.alt" loading="lazy">
              <div class="image-overlay">
                <div class="image-title">{{ scene.label }}</div>
                <div class="image-description">{{ scene.description }}</div>
              </div>
            </div>
            <div class="image-caption">
              <div class="scene-tag">{{ scene.label }}</div>
              <div class="scene-description">{{ scene.description }}</div>
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

interface ImageItem {
  filename: string;
  alt: string;
  description?: string;
  tags?: string[];
  details?: Record<string, any>;
}

interface VocabItem {
  filename: string;
  alt: string;
  description?: string;
  cn: string;
  en: string;
}

interface PromptSection {
  id: string;
  title: string;
  description?: string;
  note?: string;
  examples?: ImageItem[];
  points?: Array<{ label: string; content: string }>;
  items?: VocabItem[];
}

const getImageUrl = (filename: string): string => {
  return `https://jimeng-image.iaiuse.com/3.0/prompthighlights/${filename}`;
}

// 图片预览相关状态
const isPreviewVisible = ref(false)
const previewImages = ref<any[]>([])
const previewIndex = ref(0)

// 打开预览
const openPreview = (images: (ImageItem | VocabItem)[], clickedIndex: number): void => {
  previewImages.value = images.map(img => ({
    src: getImageUrl(img.filename),
    title: img.alt,
    description: img.description || img.alt
  }))
  previewIndex.value = clickedIndex
  isPreviewVisible.value = true
}

// 关闭预览
const closePreview = () => {
  isPreviewVisible.value = false
}

const promptSections = ref<PromptSection[]>([
  {
    id: 'language',
    title: '语言表达的精准性',
    description: '用简单直接的语言表达，在表达准确的基础上，短提示词也能发挥惊艳的效果',
    note: '长提示词并不一定代表好的生图效果，自己输入的提示词可能会比AI生成的更有效',
    examples: [
      {
        filename: 'image001.webp',
        tags: ['复古风格', '海报设计'],
        alt: '复古汽车海报',
        description: '复古风格的汽车海报设计，展现经典美学',
        details: {
          style: '复古美式风格',
          composition: '海报设计',
          elements: ['复古汽车', '公路场景', '山地背景'],
          colors: '复古蓝绿色调',
          mood: '自由探索精神'
        }
      },
      {
        filename: 'image002.webp',
        tags: ['温馨风格', '宠物元素'],
        alt: '宠物主题海报',
        description: '温馨可爱的宠物主题设计',
        details: {
          style: '温馨插画风格',
          composition: '宠物主题海报',
          elements: ['可爱狗狗', '猫咪', '中国建筑元素'],
          colors: '暖色调为主',
          mood: '温馨友好'
        }
      },
      {
        filename: 'image003.webp',
        tags: ['商务风格', '简约设计'],
        alt: '美食主题海报',
        description: '简约大气的美食广告设计',
        details: {
          style: '商业美食摄影',
          composition: '美食广告设计',
          elements: ['炸鸡', '薯条', '饮品'],
          colors: '暖色调，高饱和度',
          mood: '美味诱人'
        }
      },
      {
        filename: 'image004.webp',
        tags: ['艺术风格', '创意设计'],
        alt: '春季主题广告',
        description: '广告海报设计，卡通Q版风格',
        details: {
          style: '卡通插画风格',
          composition: {
            layout: '动态构图',
            viewpoint: '仰视视角',
            range: '中景到全景'
          },
          elements: ['卡通人物', '新鲜食材', '动态效果'],
          colors: {
            main: '暖色调',
            palette: '橙黄色和绿色搭配'
          },
          effects: [
            '光影强烈对比',
            '强烈反射折射效果',
            '超高质量渲染',
            '3D渲染',
            '数字艺术',
            'C4D与OC渲染器'
          ],
          text: {
            content: '"呼伦贝尔肉业集团春季推广"',
            position: '左下角',
            additional: '日期和地点信息，字体为小号'
          }
        }
      }
    ]
  },
  {
    id: 'description',
    title: '画面描述的层次性',
    points: [
      { label: '主体描述', content: '主体 + 行为 + 环境，构建完整场景' },
      { label: '风格表达', content: '风格、色彩、光影、构图等美学要素' },
      { label: '文字处理', content: '将关键文字放入"引号中"，提升准确率' }
    ]
  },
  {
    id: 'vocabulary',
    title: '专业词汇的精确性',
    items: [
      {
        filename: 'image005.webp',
        cn: '复古色调',
        en: 'vintage color',
        alt: '复古色调猫咪照片',
        description: '展现经典复古色调效果的猫咪照片'
      },
      {
        filename: 'image006.webp',
        cn: '强对比',
        en: 'high contrast',
        alt: '高对比度黑白猫咪照片',
        description: '黑白色调下的强对比度猫咪剪影'
      },
      {
        filename: 'image007.webp',
        cn: '柔和色调',
        en: 'soft tone',
        alt: '柔和色调抽象图案',
        description: '蓝绿色系的柔和渐变抽象图案'
      }
    ]
  }
])

const sceneApplications = ref([
  {
    id: 'ppt',
    label: 'PPT封面背景图',
    description: '适用于演示文稿封面和背景',
    image: 'image008.webp',
    alt: '柔和渐变PPT背景'
  },
  {
    id: 'poster',
    label: '广告海报设计',
    description: '适用于商业广告和宣传海报',
    image: 'image009.webp',
    alt: '烟花图案海报'
  },
  {
    id: 'photo',
    label: '纪实摄影',
    description: '适用于新闻和纪实类摄影作品',
    image: 'image010.webp',
    alt: '科技风格背景'
  }
])

// 添加浮动导航相关逻辑
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
  showFloatingNav.value = window.scrollY > 200

  const sections = [...promptSections.value.map(s => `section-${s.id}`), 'section-applications']
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

<style>
@import '../styles/shared-section.css';

.image-item-horizontal {
  grid-column: 1 / -1;
  display: flex;
  flex-direction: row;
  gap: 2rem;
  background: var(--card-bg);
  border-radius: var(--border-radius);
  padding: 1.5rem;
}

.image-item-horizontal .horizontal-image {
  flex: 0 0 50%;
  max-width: 50%;
}

.image-item-horizontal .horizontal-caption {
  flex: 1;
  padding: 0;
  margin-top: 0;
}

.image-item-horizontal .category-label {
  position: absolute;
  top: 1rem;
  left: 1rem;
  z-index: 2;
}

.horizontal-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>

