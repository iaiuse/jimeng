<template>
  <section id="response-dictionary">
    <div class="section-header">
      <div class="section-number">3</div>
      <h2 class="section-title">响应词典</h2>
    </div>
    <div class="dictionary-section">
      <div class="dictionary-tabs">
        <button 
          v-for="tab in dictionaryTabs" 
          :key="tab.id"
          class="dictionary-tab"
          :class="{ active: currentDictionaryTab === tab.id }"
          @click="currentDictionaryTab = tab.id"
        >
          {{ tab.name }}
        </button>
      </div>
      <div class="dictionary-content">
        <div v-for="(item, index) in currentTabContent" :key="index" class="dictionary-item" @click="openPreview(index)">
          <img :src="item.image" :alt="item.name">
          <span>{{ item.name }}</span>
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
import { ref, computed } from 'vue'
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
    { name: '大特写', image: '/api/placeholder/180/180' },
    { name: '特写', image: '/api/placeholder/180/180' },
    { name: '近景', image: '/api/placeholder/180/180' },
    { name: '中景', image: '/api/placeholder/180/180' },
    { name: '全景', image: '/api/placeholder/180/180' },
    { name: '大远景', image: '/api/placeholder/180/180' },
    { name: '背景', image: '/api/placeholder/180/180' },
    { name: '浅景深', image: '/api/placeholder/180/180' },
    { name: '散焦', image: '/api/placeholder/180/180' },
    { name: '焦外', image: '/api/placeholder/180/180' }
  ],
  aesthetic: [
    { name: '极简', image: '/api/placeholder/180/180' },
    { name: '复古', image: '/api/placeholder/180/180' },
    { name: '现代', image: '/api/placeholder/180/180' },
    { name: '未来', image: '/api/placeholder/180/180' },
    { name: '自然', image: '/api/placeholder/180/180' },
    { name: '工业', image: '/api/placeholder/180/180' },
    { name: '科技', image: '/api/placeholder/180/180' },
    { name: '艺术', image: '/api/placeholder/180/180' }
  ],
  trend: [
    { name: '赛博朋克', image: '/api/placeholder/180/180' },
    { name: '蒸汽朋克', image: '/api/placeholder/180/180' },
    { name: '极简主义', image: '/api/placeholder/180/180' },
    { name: '波普艺术', image: '/api/placeholder/180/180' },
    { name: '新艺术', image: '/api/placeholder/180/180' },
    { name: '后现代', image: '/api/placeholder/180/180' }
  ],
  image: [
    { name: '大特写', image: '/api/placeholder/180/180' },
    { name: '特写', image: '/api/placeholder/180/180' },
    { name: '近景', image: '/api/placeholder/180/180' },
    { name: '中景', image: '/api/placeholder/180/180' },
    { name: '全景', image: '/api/placeholder/180/180' },
    { name: '大远景', image: '/api/placeholder/180/180' }
  ],
  design: [
    { name: '平面设计', image: '/api/placeholder/180/180' },
    { name: 'UI设计', image: '/api/placeholder/180/180' },
    { name: '包装设计', image: '/api/placeholder/180/180' },
    { name: '品牌设计', image: '/api/placeholder/180/180' },
    { name: '海报设计', image: '/api/placeholder/180/180' }
  ],
  art: [
    { name: '油画', image: '/api/placeholder/180/180' },
    { name: '水彩', image: '/api/placeholder/180/180' },
    { name: '素描', image: '/api/placeholder/180/180' },
    { name: '插画', image: '/api/placeholder/180/180' },
    { name: '漫画', image: '/api/placeholder/180/180' }
  ],
  material: [
    { name: '金属', image: '/api/placeholder/180/180' },
    { name: '玻璃', image: '/api/placeholder/180/180' },
    { name: '木材', image: '/api/placeholder/180/180' },
    { name: '布料', image: '/api/placeholder/180/180' },
    { name: '塑料', image: '/api/placeholder/180/180' }
  ]
}

const currentTabContent = computed(() => dictionaryContents[currentDictionaryTab.value])

const isPreviewVisible = ref(false)
const previewIndex = ref(0)

const previewImages = computed(() => 
  currentTabContent.value.map(item => ({
    src: item.image,
    title: item.name,
    description: item.name
  }))
)

const openPreview = (index: number) => {
  previewIndex.value = index
  isPreviewVisible.value = true
}

const closePreview = () => {
  isPreviewVisible.value = false
}
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

.dictionary-section {
  background-color: white;
  border-radius: 8px;
  padding: 35px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.dictionary-tabs {
  display: flex;
  border-bottom: 1px solid #eee;
  margin-bottom: 25px;
  overflow-x: auto;
  padding-bottom: 1px;
}

.dictionary-tab {
  padding: 12px 25px;
  background: none;
  border: none;
  color: #555;
  font-weight: 500;
  font-size: 1.1rem;
  cursor: pointer;
  white-space: nowrap;
  border-bottom: 2px solid transparent;
}

.dictionary-tab.active {
  color: #0066cc;
  border-bottom-color: #0066cc;
}

.dictionary-content {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.dictionary-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.dictionary-item img {
  width: 100%;
  border-radius: 6px;
  aspect-ratio: 1;
  object-fit: cover;
  margin-bottom: 12px;
}

.dictionary-item span {
  text-align: center;
  font-size: 1rem;
  color: #555;
}

@media (max-width: 576px) {
  .dictionary-content {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style> 