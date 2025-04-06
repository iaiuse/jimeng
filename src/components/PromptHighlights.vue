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
            <div v-for="(example, index) in section.examples" 
                 :key="index" 
                 :class="['example-card', { 'example-card-horizontal': example.filename === 'image004.webp' }]"
                 @click="openPreview(section.examples, index)">
              <div :class="{'example-image-container': example.filename === 'image004.webp'}">
                <img :src="getImageUrl(example.filename)" :alt="example.alt">
                <div class="example-info" v-if="example.filename !== 'image004.webp'">
                  <span v-for="tag in example.tags" :key="tag" class="example-tag">{{ tag }}</span>
                </div>
              </div>
              <div :class="{'example-content-container': example.filename === 'image004.webp'}">
                <div class="example-info" v-if="example.filename === 'image004.webp'">
                  <span v-for="tag in example.tags" :key="tag" class="example-tag">{{ tag }}</span>
                </div>
                <div v-if="example.details" class="example-details">
                  <div class="detail-section">
                    <strong>风格：</strong>
                    <span>{{ example.details.style }}</span>
                  </div>
                  <div class="detail-section" v-if="typeof example.details.composition === 'string'">
                    <strong>构图：</strong>
                    <span>{{ example.details.composition }}</span>
                  </div>
                  <div class="detail-section" v-else-if="example.details.composition">
                    <strong>构图：</strong>
                    <div class="composition-details">
                      <div class="composition-item">布局：{{ example.details.composition.layout }}</div>
                      <div class="composition-item">视角：{{ example.details.composition.viewpoint }}</div>
                      <div class="composition-item">景别：{{ example.details.composition.range }}</div>
                    </div>
                  </div>
                  <div class="detail-section">
                    <strong>元素：</strong>
                    <div class="element-tags">
                      <span v-for="element in example.details.elements" 
                            :key="element" 
                            class="element-tag">
                        {{ element }}
                      </span>
                    </div>
                  </div>
                  <div class="detail-section">
                    <strong>色彩：</strong>
                    <span v-if="typeof example.details.colors === 'string'">
                      {{ example.details.colors }}
                    </span>
                    <div v-else class="color-details">
                      <div>主色调：{{ example.details.colors.main }}</div>
                      <div>配色：{{ example.details.colors.palette }}</div>
                    </div>
                  </div>
                  <div class="detail-section" v-if="example.details.effects">
                    <strong>特效：</strong>
                    <div class="effects-list">
                      <span v-for="effect in example.details.effects" 
                            :key="effect" 
                            class="effect-item">
                        {{ effect }}
                      </span>
                    </div>
                  </div>
                  <div class="detail-section" v-if="example.details.text">
                    <strong>文字：</strong>
                    <div class="text-details">
                      <p>内容：{{ example.details.text.content }}</p>
                      <p>位置：{{ example.details.text.position }}</p>
                      <p>补充：{{ example.details.text.additional }}</p>
                    </div>
                  </div>
                </div>
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
            <div v-for="(item, index) in section.items" 
                 :key="item.cn" 
                 class="vocab-item"
                 @click="openPreview(section.items, index)">
              <img :src="getImageUrl(item.filename)" :alt="item.alt">
              <div class="vocab-pair">
                <span class="vocab-cn">{{ item.cn }}</span>
                <span class="vocab-en">{{ item.en }}</span>
              </div>
            </div>
          </div>
        </template>
      </div>

      <!-- 场景应用推荐 -->
      <div class="highlight-section">
        <h3 class="highlight-title">场景应用推荐</h3>
        <div class="scene-applications">
          <div v-for="scene in sceneApplications" 
               :key="scene.id" 
               class="scene-card">
            <img :src="getImageUrl(scene.image)" :alt="scene.alt" class="scene-image">
            <div class="scene-info">
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
import { ref } from 'vue'
import ImagePreview from './ImagePreview.vue'

const getImageUrl = (filename) => {
  return `https://jimeng-image.iaiuse.com/3.0/prompthighlights/${filename}`;
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
    description: img.description || img.alt
  }))
  previewIndex.value = index
  isPreviewVisible.value = true
}

// 关闭预览
const closePreview = () => {
  isPreviewVisible.value = false
}

const promptSections = ref([
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

.example-details {
  padding: 1rem;
  background: #f7fafc;
  border-radius: 6px;
  margin-top: 1rem;
}

.detail-section {
  margin-bottom: 0.5rem;
}

.detail-section strong {
  font-weight: 500;
  color: #2c3e50;
}

.detail-section span {
  font-size: 0.875rem;
  color: #4a5568;
}

.composition-details {
  display: flex;
  gap: 0.5rem;
}

.element-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
}

.element-tag {
  font-size: 0.75rem;
  padding: 0.25rem 0.5rem;
  background: #f1f5f9;
  border-radius: 4px;
  color: #475569;
}

.color-details {
  display: flex;
  gap: 0.5rem;
}

.effects-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
}

.effect-item {
  font-size: 0.75rem;
  padding: 0.25rem 0.5rem;
  background: #f1f5f9;
  border-radius: 4px;
  color: #475569;
}

.text-details {
  margin-top: 0.5rem;
}

.text-details p {
  margin: 0.25rem 0;
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

.scene-applications {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.scene-card {
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.scene-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.scene-image {
  width: 100%;
  height: 160px;
  object-fit: cover;
}

.scene-info {
  padding: 1rem;
}

.scene-tag {
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.scene-description {
  font-size: 0.875rem;
  color: #64748b;
}

.example-card.example-card-horizontal {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 2rem;
  max-width: 100%;
  margin-top: 1rem;
  padding: 1.5rem;
}

.example-image-container {
  width: 100%;
  height: 100%;
}

.example-image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

.example-content-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.example-card-horizontal .example-details {
  padding: 0;
  background: transparent;
}

.composition-details {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.composition-item {
  font-size: 0.875rem;
  color: #4a5568;
}

.color-details {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 0.5rem;
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
  
  .example-card.example-card-horizontal {
    grid-template-columns: 1fr;
    gap: 1rem;
    padding: 1rem;
  }
  
  .example-image-container {
    min-height: 200px;
  }
  
  .scene-applications {
    grid-template-columns: 1fr;
  }
  
  .scene-image {
    height: 140px;
  }
}
</style>