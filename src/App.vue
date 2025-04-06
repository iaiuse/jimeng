<template>
  <div class="app">
    <header>
      <div class="header-container container">
        <a href="#" class="logo">
          即梦图片3.0
        </a>
        <button class="menu-toggle" @click="toggleMenu">
          <span></span>
          <span></span>
          <span></span>
        </button>
        <div class="header-right" :class="{ 'menu-open': isMenuOpen }">
          <nav class="main-nav">
            <a 
              v-for="tab in tabs" 
              :key="tab.id"
              class="nav-link"
              :class="{ active: currentTab === tab.id }"
              @click.prevent="currentTab = tab.id"
              href="#"
            >
              {{ tab.name }}
            </a>
          </nav>
        </div>
      </div>
    </header>

    <main class="main-content">
      <div class="container">
        <div class="handbook-header">
          <h1>即梦图片3.0模型 提示词攻略手册</h1>
          <p>探索新一代AI图像生成模型，实现真实、高清、专业的视觉创作</p>
          <div class="update-info">最新更新时间: 2025年4月1日</div>
        </div>

        <component :is="currentComponent"></component>
      </div>
    </main>

    <footer>
      <div class="footer-content">
        <div class="footer-info">
          <p>即梦图片3.0模型是由ByteDance开发的新一代AI图像生成技术，提供真实、高清、专业的图像创作体验。</p>
        </div>
        <div class="footer-links">
          <ul class="social-list">
            <li>
              <a href="https://github.com/iaiuse" target="_blank" class="social-link">
                <i class="fab fa-github"></i>
                <span>GitHub</span>
                <div class="qr-tooltip">
                  <img src="/qr/github-qr.png" alt="GitHub QR Code">
                </div>
              </a>
            </li>
            <li>
              <a href="https://okjk.co/T4JBo0" target="_blank" class="social-link">
                <i class="fas fa-compass"></i>
                <span>即刻</span>
                <div class="qr-tooltip">
                  <img src="/qr/jike-qr.png" alt="即刻 QR Code">
                </div>
              </a>
            </li>
            <li>
              <a href="https://www.xiaohongshu.com/user/profile/5b2bc6dbf7e8b97ff70a63b2" target="_blank" class="social-link">
                <i class="fas fa-book"></i>
                <span>小红书</span>
                <div class="qr-tooltip">
                  <img src="/qr/xiaohongshu-qr.png" alt="小红书 QR Code">
                </div>
              </a>
            </li>
            <li>
              <a href="https://mp.weixin.qq.com/s/Eh8vlal4L02eToTOlaeFww" target="_blank" class="social-link">
                <i class="fab fa-weixin"></i>
                <span>公众号</span>
                <div class="qr-tooltip">
                  <img src="/qr/wechat-qr.png" alt="公众号 QR Code">
                </div>
              </a>
            </li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2025 大雨@waytoagi. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import ModelHighlights from './components/ModelHighlights.vue'
import PromptHighlights from './components/PromptHighlights.vue'
import ResponseDictionary from './components/ResponseDictionary.vue'
import MoreShowcase from './components/MoreShowcase.vue'

const tabs = [
  { id: 'model-highlights', name: '模型亮点' },
  { id: 'prompt-highlights', name: '提示词亮点' },
  { id: 'response-dictionary', name: '响应词典' },
  { id: 'more-showcase', name: '更多展示' }
]

const currentTab = ref('model-highlights')
const isMenuOpen = ref(false)

const currentComponent = computed(() => {
  switch (currentTab.value) {
    case 'model-highlights':
      return ModelHighlights
    case 'prompt-highlights':
      return PromptHighlights
    case 'response-dictionary':
      return ResponseDictionary
    case 'more-showcase':
      return MoreShowcase
    default:
      return ModelHighlights
  }
})

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}
</script>

<style>
/* 保留所有组件特定样式 */
header {
  background-color: white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.logo {
  display: flex;
  align-items: center;
  gap: 15px;
  font-weight: 500;
  font-size: 1.4rem;
  color: #333;
  text-decoration: none;
  opacity: 0.5;
  transition: opacity 0.3s ease;
}

.logo:hover {
  opacity: 1;
}

.header-right {
  display: block;
}

.menu-toggle {
  display: none;
}

.main-nav {
  display: flex;
  gap: 20px;
}

.nav-link {
  color: #333;
  text-decoration: none;
  transition: color 0.2s;
  padding: 8px 16px;
  border-radius: 4px;
}

.nav-link:hover {
  background-color: #f5f5f5;
}

.nav-link.active {
  font-weight: bold;
  background-color: #eee;
}

.handbook-header {
  margin-bottom: 20px;
}

.handbook-header h1 {
  font-size: 2rem;
  margin-bottom: 10px;
  color: #fff;
}

.handbook-header p {
  font-size: 1.2rem;
  color: #ccc;
}

.update-info {
  font-size: 0.8rem;
  color: #888;
}

footer {
  background-color: #000;
  padding: 40px 0;
  color: #fff;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.footer-info {
  flex: 1;
}

.footer-info p {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
  max-width: 600px;
}

.footer-links {
  display: flex;
  gap: 20px;
}

.social-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  gap: 20px;
}

.social-link {
  position: relative;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: color 0.3s ease;
}

.social-link i {
  font-size: 24px;
}

.social-link span {
  display: none;
}

.qr-tooltip {
  position: absolute;
  top: -120px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #fff;
  padding: 8px;
  border-radius: 8px;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
}

.social-link:hover .qr-tooltip {
  opacity: 1;
  visibility: visible;
}

.qr-tooltip img {
  width: 100px;
  height: 100px;
  display: block;
}

.qr-tooltip p {
  display: none;
}

.footer-bottom {
  margin-top: 40px;
  text-align: center;
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.8rem;
}

/* 修改主内容区域背景色 */
.main-content {
  background-color: #000;
  color: #fff;
  min-height: 100vh;
  padding: 40px 0;
}

/* 仅在移动端显示菜单按钮 */
@media (max-width: 768px) {
  .menu-toggle {
    display: block;
  }
  
  .header-right {
    display: none;
  }
  
  .header-right.menu-open {
    display: block;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  
  .main-nav {
    flex-direction: column;
    gap: 10px;
  }
}
</style> 