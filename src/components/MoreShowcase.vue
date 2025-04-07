<template>
  <section id="response-dictionary">
    <div class="section-header">
      <div class="section-number">4</div>
      <h2 class="section-title">更多展示</h2>
    </div>
    
    <!-- 添加浮动导航菜单 -->
    <div class="floating-nav" :class="{ 'is-visible': showFloatingNav && !isNavManuallyHidden }">
      <!-- 导航菜单内的切换按钮 -->
      <div class="nav-toggle" @click="toggleNavVisibility">
        <span class="toggle-icon">&gt;&gt;</span>
      </div>
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

    <!-- 单独的导航切换按钮，仅在菜单隐藏时可见 -->
    <div class="nav-toggle-button" 
         :class="{ 'is-visible': showFloatingNav && isNavManuallyHidden }" 
         @click="toggleNavVisibility">
      <span class="toggle-icon">&lt;&lt;</span>
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
import { features } from '../data/showcase'
import type { ResponseItem } from '../data/showcase'

const getImageUrl = (filename: string) => {
  return `https://jimeng-image.iaiuse.com/3.0/more-showcase/${filename}`
}

// 图片预览相关状态
const isPreviewVisible = ref(false)
const previewImages = ref<any[]>([])
const previewIndex = ref(0)

// 打开预览
const openPreview = (items: ResponseItem[], index: number) => {
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
const isNavManuallyHidden = ref(false)

// 切换导航菜单的显示/隐藏状态
const toggleNavVisibility = () => {
  isNavManuallyHidden.value = !isNavManuallyHidden.value
}

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
</script>

<style>
@import '../styles/shared-section.css';

/* 导航菜单内的切换按钮样式 */
.nav-toggle {
  text-align: center;
  padding: 8px 0;
  cursor: pointer;
  color: var(--link-color);
  border-bottom: 1px solid var(--border-color);
  margin-bottom: 10px;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-toggle:hover {
  background-color: var(--nav-hover-bg);
}

/* 单独的导航切换按钮样式 */
.nav-toggle-button {
  position: fixed;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  background: var(--card-bg);
  border-radius: 12px;
  box-shadow: 0 2px 12px var(--card-shadow);
  padding: 8px 15px;
  z-index: 100;
  cursor: pointer;
  color: var(--link-color);
  transition: all 0.2s ease;
  opacity: 0;
  visibility: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 40px;
  height: 40px;
}

.nav-toggle-button.is-visible {
  opacity: 1;
  visibility: visible;
}

.nav-toggle-button:hover {
  background-color: var(--nav-hover-bg);
}

.toggle-icon {
  font-size: 1.2rem;
  font-weight: bold;
  font-family: monospace;
}

/* 当滚动到一定位置时显示切换按钮 */
@media (min-width: 769px) {
  .nav-toggle-button {
    opacity: 0;
    visibility: hidden;
  }
}
</style>