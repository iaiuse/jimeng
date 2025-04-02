<template>
  <section id="more-showcase" class="showcase-section">
    <div class="section-header">
      <div class="section-number">4</div>
      <h2 class="section-title">更多Showcase</h2>
    </div>
    <div class="showcase-header">
      <div class="showcase-categories">
        <button 
          v-for="category in categories" 
          :key="category.id"
          class="category-button"
          :class="{ active: currentCategory === category.id }"
          @click="currentCategory = category.id"
        >
          {{ category.name }}
        </button>
      </div>
    </div>
    <div class="showcase-grid">
      <div v-for="(item, index) in filteredShowcase" :key="index" class="showcase-item" @click="openPreview(index)">
        <img :src="item.image" :alt="item.title">
        <div class="overlay">
          <h4>{{ item.title }}</h4>
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

const categories = [
  { id: 'all', name: '全部' },
  { id: 'image', name: '影像' },
  { id: 'art', name: '艺术' },
  { id: 'design', name: '设计' },
  { id: 'anime', name: '动漫风格' },
  { id: 'material', name: '材质' }
]

const currentCategory = ref('all')

const showcaseItems = [
  {
    id: 1,
    title: '写实人像风格',
    image: '/api/placeholder/400/300',
    category: 'image'
  },
  {
    id: 2,
    title: '电影叙事风格',
    image: '/api/placeholder/400/300',
    category: 'image'
  },
  {
    id: 3,
    title: '动漫场景风格',
    image: '/api/placeholder/400/300',
    category: 'anime'
  },
  {
    id: 4,
    title: '奇幻概念艺术',
    image: '/api/placeholder/400/300',
    category: 'art'
  },
  {
    id: 5,
    title: '写实质感材质',
    image: '/api/placeholder/400/300',
    category: 'material'
  },
  {
    id: 6,
    title: '插画艺术风格',
    image: '/api/placeholder/400/300',
    category: 'art'
  },
  {
    id: 7,
    title: 'UI设计展示',
    image: '/api/placeholder/400/300',
    category: 'design'
  },
  {
    id: 8,
    title: '品牌设计案例',
    image: '/api/placeholder/400/300',
    category: 'design'
  }
]

const filteredShowcase = computed(() => {
  if (currentCategory.value === 'all') {
    return showcaseItems
  }
  return showcaseItems.filter(item => item.category === currentCategory.value)
})

const isPreviewVisible = ref(false)
const previewIndex = ref(0)

const previewImages = computed(() => 
  filteredShowcase.value.map(item => ({
    src: item.image,
    title: item.title,
    description: item.category
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

.showcase-section {
  margin-top: 50px;
}

.showcase-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

.showcase-categories {
  display: flex;
  gap: 12px;
  overflow-x: auto;
  padding-bottom: 5px;
}

.category-button {
  padding: 10px 20px;
  background-color: white;
  border: 1px solid #e0e0e0;
  border-radius: 25px;
  color: #555;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.category-button:hover, .category-button.active {
  background-color: #0066cc;
  color: white;
  border-color: #0066cc;
}

.showcase-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
}

.showcase-item {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.showcase-item:hover {
  transform: scale(1.02);
}

.showcase-item img {
  width: 100%;
  display: block;
  aspect-ratio: 4/3;
  object-fit: cover;
}

.showcase-item .overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(transparent, rgba(0,0,0,0.7));
  color: white;
  padding: 25px 20px 20px;
}

.showcase-item h4 {
  font-size: 1.3rem;
  margin-bottom: 8px;
}

@media (max-width: 768px) {
  .showcase-grid {
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  }
}

@media (max-width: 576px) {
  .showcase-grid {
    grid-template-columns: 1fr;
  }
}
</style> 