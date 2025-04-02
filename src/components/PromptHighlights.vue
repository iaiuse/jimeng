<template>
  <section id="prompt-highlights">
    <div class="section-header">
      <div class="section-number">2</div>
      <h2 class="section-title">提示词亮点</h2>
    </div>
    <div class="prompt-tabs">
      <button 
        v-for="tab in promptTabs" 
        :key="tab.id"
        class="prompt-tab"
        :class="{ active: currentPromptTab === tab.id }"
        @click="currentPromptTab = tab.id"
      >
        {{ tab.name }}
      </button>
    </div>
    <div class="prompt-content">
      <h3>{{ currentTabContent.title }}</h3>
      <div class="prompt-details">
        <p v-for="(detail, index) in currentTabContent.details" :key="index">
          <strong>{{ detail.label }}:</strong> {{ detail.content }}
        </p>
      </div>
      <div class="image-grid">
        <div v-for="(image, index) in currentTabContent.images" :key="index" class="image-card" @click="openPreview(index)">
          <img :src="image.src" :alt="image.title">
          <div class="info">
            <h4>{{ image.title }}</h4>
            <p>{{ image.description }}</p>
            <div class="tags">
              <span v-for="(tag, tagIndex) in image.tags" :key="tagIndex" class="tag">{{ tag }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="prompt-examples">
        <h4>推荐提示词:</h4>
        <p v-for="(example, index) in currentTabContent.examples" :key="index">
          "<strong>{{ example }}</strong>"
        </p>
      </div>
    </div>

    <ImagePreview
      :is-visible="isPreviewVisible"
      :images="currentTabContent.images"
      :initial-index="previewIndex"
      @close="closePreview"
    />
  </section>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import ImagePreview from './ImagePreview.vue'

const promptTabs = [
  { id: 'real', name: '真实' },
  { id: 'hd', name: '高清' },
  { id: 'pro', name: '专业' },
  { id: 'text', name: '文字准确' }
]

const currentPromptTab = ref('real')

const tabContents = {
  real: {
    title: '真实：去虚饰、以假乱真',
    details: [
      { label: '原画真实', content: '去虚饰感，假脸感，AI油腻感' },
      { label: '情绪真实', content: '去僵硬感，摆拍感，AI眼神空洞感，情绪细腻有感染力' }
    ],
    images: [
      {
        src: '/api/placeholder/240/240',
        title: '人物写实',
        description: '去除AI特征，真实肤质',
        tags: ['写实', '人像']
      },
      {
        src: '/api/placeholder/240/240',
        title: '情绪表达',
        description: '自然眼神，情感真实',
        tags: ['情绪', '细节']
      },
      {
        src: '/api/placeholder/240/240',
        title: '场景真实',
        description: '光影自然，空间合理',
        tags: ['场景', '光影']
      },
      {
        src: '/api/placeholder/240/240',
        title: '材质表现',
        description: '质感细腻，真实反光',
        tags: ['材质', '质感']
      }
    ],
    examples: [
      '自然肤质, 真实细节, 去AI感, 自然光线',
      '真实情绪, 自然表情, 有神的眼睛, 情感表达'
    ]
  },
  hd: {
    title: '高清：默认1k，可支持2K',
    details: [
      { label: '高分辨率', content: '支持1K和2K输出，细节丰富' },
      { label: '画面稳定', content: '2K时画面结构更稳定，无失真' }
    ],
    images: [
      {
        src: '/api/placeholder/240/240',
        title: '高分辨率',
        description: '清晰度提升，细节丰富',
        tags: ['高清', '细节']
      },
      {
        src: '/api/placeholder/240/240',
        title: '纹理清晰',
        description: '材质细节清晰可见',
        tags: ['纹理', '清晰']
      }
    ],
    examples: [
      '高分辨率, 细节丰富, 清晰度提升, 纹理清晰',
      '2K输出, 画面稳定, 无失真, 细节保留'
    ]
  },
  pro: {
    title: '专业：专业级的画面效果',
    details: [
      { label: '商业品质', content: '满足各种商业创意和设计需求' },
      { label: '专业摄影', content: '提供专业的商业摄影效果' }
    ],
    images: [
      {
        src: '/api/placeholder/240/240',
        title: '商业摄影',
        description: '专业摄影效果，广告级质感',
        tags: ['商业', '摄影']
      },
      {
        src: '/api/placeholder/240/240',
        title: '设计作品',
        description: '专业设计品质输出',
        tags: ['设计', '品质']
      }
    ],
    examples: [
      '专业摄影效果, 广告级质感, 商业品质输出',
      '专业设计, 商业创意, 高品质输出'
    ]
  },
  text: {
    title: '文字准确：更准确的字体响应',
    details: [
      { label: '字体准确', content: '支持不同字体，专业的设计排版' },
      { label: '多语言', content: '支持多语言文字生成' }
    ],
    images: [
      {
        src: '/api/placeholder/240/240',
        title: '字体排版',
        description: '排版美观，字体清晰',
        tags: ['排版', '字体']
      },
      {
        src: '/api/placeholder/240/240',
        title: '多语言',
        description: '支持多语言文字生成',
        tags: ['多语言', '文字']
      }
    ],
    examples: [
      '排版美观, 字体清晰, 多语言支持, 设计感强',
      '专业排版, 字体准确, 多语言, 设计感'
    ]
  }
}

const currentTabContent = computed(() => tabContents[currentPromptTab.value])

const isPreviewVisible = ref(false)
const previewIndex = ref(0)

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

.prompt-tabs {
  display: flex;
  background-color: white;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 25px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.prompt-tab {
  padding: 18px 30px;
  background: none;
  border: none;
  color: #555;
  font-weight: 500;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.2s;
  text-align: center;
  flex: 1;
}

.prompt-tab.active {
  background-color: #0066cc;
  color: white;
}

.prompt-tab:hover:not(.active) {
  background-color: #f5f9ff;
}

.prompt-content {
  background-color: white;
  border-radius: 8px;
  padding: 35px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.prompt-content h3 {
  font-size: 1.5rem;
  margin-bottom: 20px;
  color: #333;
}

.prompt-details {
  margin-bottom: 25px;
}

.prompt-details p {
  margin-bottom: 12px;
  font-size: 1.1rem;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 25px;
  margin-bottom: 25px;
}

.image-card {
  background-color: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.image-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.image-card img {
  width: 100%;
  display: block;
  aspect-ratio: 1;
  object-fit: cover;
}

.image-card .info {
  padding: 20px;
}

.image-card h4 {
  font-size: 1.2rem;
  margin-bottom: 8px;
  color: #333;
}

.image-card p {
  color: #666;
  font-size: 1rem;
}

.tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 12px;
}

.tag {
  background-color: #f0f7ff;
  color: #0066cc;
  padding: 4px 10px;
  border-radius: 4px;
  font-size: 0.85rem;
}

.prompt-examples {
  background-color: #f8f8f8;
  padding: 20px;
  border-radius: 6px;
  margin-top: 20px;
}

.prompt-examples h4 {
  margin-bottom: 12px;
  color: #555;
  font-size: 1.1rem;
}

.prompt-examples p {
  margin-bottom: 10px;
  font-size: 1rem;
}

@media (max-width: 576px) {
  .image-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  
  .prompt-tab {
    padding: 12px 15px;
    font-size: 0.9rem;
  }
}
</style> 