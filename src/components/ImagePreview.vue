<template>
  <div class="image-preview" v-if="isVisible" @click="closePreview">
    <div class="preview-content" @click.stop>
      <button class="close-button" @click="closePreview">&times;</button>
      <button class="nav-button prev" @click="prevImage" :disabled="currentIndex === 0">&lt;</button>
      <button class="nav-button next" @click="nextImage" :disabled="currentIndex === images.length - 1">&gt;</button>
      <img :src="currentImage" :alt="currentTitle" class="preview-image">
      <div class="preview-info">
        <h3>{{ currentTitle }}</h3>
        <p>{{ currentDescription }}</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  isVisible: boolean
  images: Array<{
    src: string
    title: string
    description?: string
  }>
  initialIndex: number
}>()

const emit = defineEmits<{
  (e: 'close'): void
}>()

const currentIndex = ref(props.initialIndex)

const currentImage = computed(() => props.images[currentIndex.value]?.src)
const currentTitle = computed(() => props.images[currentIndex.value]?.title)
const currentDescription = computed(() => props.images[currentIndex.value]?.description)

const closePreview = () => {
  emit('close')
}

const prevImage = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--
  }
}

const nextImage = () => {
  if (currentIndex.value < props.images.length - 1) {
    currentIndex.value++
  }
}

// 键盘事件处理
const handleKeydown = (e: KeyboardEvent) => {
  if (!props.isVisible) return
  
  switch (e.key) {
    case 'Escape':
      closePreview()
      break
    case 'ArrowLeft':
      prevImage()
      break
    case 'ArrowRight':
      nextImage()
      break
  }
}

// 添加和移除键盘事件监听
onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
.image-preview {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  cursor: pointer;
}

.preview-content {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--card-bg);
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 12px var(--card-shadow);
}

.preview-image {
  max-width: 100%;
  max-height: 80vh;
  object-fit: contain;
  border-radius: 4px;
}

.close-button {
  position: absolute;
  top: -40px;
  right: 0;
  background: none;
  border: none;
  color: white;
  font-size: 2rem;
  cursor: pointer;
  padding: 5px 10px;
}

.nav-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  font-size: 2rem;
  padding: 20px 10px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.nav-button:hover {
  background: rgba(255, 255, 255, 0.3);
}

.nav-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.prev {
  left: -60px;
}

.next {
  right: -60px;
}

.preview-info {
  margin-top: 20px;
  color: var(--text-color);
  text-align: center;
  max-width: 600px;
}

.preview-info h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.preview-info p {
  font-size: 1.1rem;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .nav-button {
    padding: 10px 5px;
    font-size: 1.5rem;
  }

  .prev {
    left: -40px;
  }

  .next {
    right: -40px;
  }
}
</style> 