 <?xml version="1.0" encoding="UTF-8"?>
<template>
  <section class="prompt-highlights">
    <div class="section-header">
      <div class="section-number">2</div>
      <h2 class="section-title">提示词秘籍</h2>
    </div>

    <div class="highlight-content">
      <div v-for="section in promptSections" :key="section.id" class="highlight-section">
        <h3 class="highlight-title">{{ section.title }}</h3>
        
        <!-- 语言表达部分 -->
        <template v-if="section.id === 'language'">
          <p class="highlight-desc">{{ section.description }}</p>
          <div class="highlight-note">{{ section.note }}</div>
          <div class="example-grid">
            <div v-for="(example, index) in section.examples" :key="index" class="example-card">
              <img :src="example.image" :alt="example.alt">
              <div class="example-info">
                <span v-for="tag in example.tags" :key="tag" class="example-tag">{{ tag }}</span>
              </div>
            </div>
          </div>
        </template>

        <!-- 画面描述部分 -->
        <template v-if="section.id === 'description'">
          <div class="description-points">
            <div v-for="point in section.points" :key="point.label" class="point">
              <strong>{{ point.label }}：</strong>
              <span>{{ point.content }}</span>
            </div>
          </div>
        </template>

        <!-- 专业词汇部分 -->
        <template v-if="section.id === 'vocabulary'">
          <div class="vocab-examples">
            <div v-for="item in section.items" :key="item.cn" class="vocab-item">
              <img :src="item.image" :alt="item.alt">
              <div class="vocab-pair">
                <span class="vocab-cn">{{ item.cn }}</span>
                <span class="vocab-en">{{ item.en }}</span>
              </div>
            </div>
          </div>
        </template>
      </div>

      <!-- 场景推荐 -->
      <div class="highlight-section">
        <h3 class="highlight-title">场景应用推荐</h3>
        <div class="scene-tags">
          <span v-for="tag in sceneTags" :key="tag" class="scene-tag">{{ tag }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const promptSections = ref([
  {
    id: 'language',
    title: '语言表达的精准性',
    description: '用简单直接的语言表达，在表达准确的基础上，短提示词也能发挥惊艳的效果',
    note: '长提示词并不一定代表好的生图效果，自己输入的提示词可能会比AI生成的更有效',
    examples: [
      {
        image: '/prompthighlights/image001.webp',
        tags: ['复古风格', '海报设计'],
        alt: '复古汽车海报'
      },
      {
        image: '/prompthighlights/image002.webp',
        tags: ['温馨风格', '宠物元素'],
        alt: '宠物主题海报'
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
        image: '/prompthighlights/image003.webp',
        cn: '复古色调',
        en: 'vintage color',
        alt: '复古色调示例'
      },
      {
        image: '/prompthighlights/image004.webp',
        cn: '强对比',
        en: 'high contrast',
        alt: '强对比示例'
      }
    ]
  }
])

const sceneTags = ref([
  'PPT封面背景图',
  '广告海报设计',
  '纪实摄影'
])
</script>

<style scoped>
.prompt-highlights {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  color: #2c3e50;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

.section-header {
  display: flex;
  align-items: center;
  margin-bottom: 2.5rem;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 1.5rem;
}

.section-number {
  width: 40px;
  height: 40px;
  border: 2px solid #2c3e50;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  margin-right: 1rem;
}

.section-title {
  font-size: 1.75rem;
  font-weight: 600;
  letter-spacing: -0.5px;
}

.highlight-section {
  margin-bottom: 3rem;
  background: #fff;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.highlight-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  color: #2c3e50;
  position: relative;
  padding-left: 1rem;
}

.highlight-title::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 4px;
  height: 1.25em;
  background: #2c3e50;
  border-radius: 2px;
}

.highlight-desc {
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 1rem;
  color: #4a5568;
}

.highlight-note {
  font-size: 0.875rem;
  color: #718096;
  font-style: italic;
  margin-bottom: 1.5rem;
  padding: 0.75rem;
  background: #f7fafc;
  border-radius: 6px;
  border-left: 4px solid #e2e8f0;
}

.example-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.example-card {
  border-radius: 8px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.example-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.example-card img {
  width: 100%;
  height: auto;
  object-fit: cover;
  aspect-ratio: 16/9;
}

.example-info {
  padding: 1rem;
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.example-tag {
  font-size: 0.75rem;
  padding: 0.25rem 0.75rem;
  background: #f1f5f9;
  border-radius: 4px;
  color: #475569;
  transition: background-color 0.2s ease;
}

.example-tag:hover {
  background: #e2e8f0;
}

.description-points {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.point {
  display: flex;
  align-items: baseline;
  gap: 1rem;
  padding: 0.75rem;
  background: #f8fafc;
  border-radius: 6px;
  transition: background-color 0.2s ease;
}

.point:hover {
  background: #f1f5f9;
}

.point strong {
  min-width: 5rem;
  color: #2c3e50;
  font-weight: 500;
}

.vocab-examples {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
}

.vocab-item {
  text-align: center;
  transition: transform 0.2s ease;
}

.vocab-item:hover {
  transform: translateY(-4px);
}

.vocab-item img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  margin-bottom: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  aspect-ratio: 1;
  object-fit: cover;
}

.vocab-pair {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  align-items: center;
}

.vocab-cn {
  font-weight: 500;
  color: #2c3e50;
}

.vocab-en {
  color: #64748b;
  font-size: 0.875rem;
  font-family: 'Courier New', monospace;
}

.scene-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.scene-tag {
  padding: 0.5rem 1rem;
  background: #f1f5f9;
  border-radius: 6px;
  font-size: 0.875rem;
  color: #475569;
  transition: all 0.2s ease;
  cursor: pointer;
}

.scene-tag:hover {
  background: #e2e8f0;
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .prompt-highlights {
    padding: 1rem;
  }
  
  .highlight-section {
    padding: 1.5rem;
  }
  
  .example-grid {
    grid-template-columns: 1fr;
  }
  
  .vocab-examples {
    grid-template-columns: 1fr;
  }
  
  .point {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .point strong {
    min-width: auto;
  }
  
  .section-title {
    font-size: 1.5rem;
  }
  
  .highlight-title {
    font-size: 1.1rem;
  }
}
</style>