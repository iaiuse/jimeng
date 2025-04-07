<template>
  <div class="app" :class="{ 'dark-mode': isDarkMode }">
    <header>
      <div class="header-container container">
        <a href="#" class="logo">
          <img src="/vite.svg" alt="Logo" class="logo-img">
          即梦图片3.0
        </a>
        <button class="menu-toggle" :class="{ 'menu-open': isMenuOpen }" @click="toggleMenu">
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
            <button 
              class="theme-toggle"
              @click="toggleTheme"
              :title="isDarkMode ? '切换到亮色模式' : '切换到暗色模式'"
            >
              <i class="fas" :class="isDarkMode ? 'fa-sun' : 'fa-moon'"></i>
            </button>
          </nav>
        </div>
      </div>
    </header>

    <main class="main-content">
      <div class="container">
        <div class="handbook-header">
          <h1>即梦图片3.0模型 提示词攻略手册</h1>
          <p>探索新一代AI图像生成模型，实现真实、高清、专业的视觉创作。立即<a href="https://jimeng.jianying.com/" target="_blank" rel="noopener noreferrer">体验即梦</a></p>
          <div class="update-info">最新更新时间: 2025年4月1日</div>
          <div class="feedback-link">
            <a href="https://github.com/iaiuse/jimeng/issues/new" target="_blank" rel="noopener noreferrer">
              有意见或想法？欢迎提交反馈 →
            </a>
          </div>
        </div>

        <component :is="currentComponent"></component>
      </div>
    </main>

    <footer>
      <div class="footer-content">
        <div class="footer-info">
          <p>即梦图片3.0模型是由ByteDance开发的新一代AI图像生成技术，提供真实、高清、专业的图像创作体验。</p>
          <p class="reference-info">参考文档：<a href="https://bytedance.larkoffice.com/docx/EVYXdpdmhoVc0sxXR6dcsOu6nXc" target="_blank" rel="noopener noreferrer">即梦图片3.0模型 提示词攻略手册</a></p>
        </div>
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
      <div class="footer-bottom">
        <p>© 2025 大雨@waytoagi. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
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
const isDarkMode = ref(false)

// 从 localStorage 读取主题设置
onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme) {
    isDarkMode.value = savedTheme === 'dark'
  } else {
    // 如果没有保存的主题，则根据系统偏好设置
    isDarkMode.value = window.matchMedia('(prefers-color-scheme: dark)').matches
  }
  updateTheme()
})

// 切换主题
const toggleTheme = () => {
  isDarkMode.value = !isDarkMode.value
  updateTheme()
}

// 更新主题
const updateTheme = () => {
  localStorage.setItem('theme', isDarkMode.value ? 'dark' : 'light')
  document.documentElement.classList.toggle('dark-mode', isDarkMode.value)
}

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
:root {
  --bg-color: #fff;
  --text-color: #333;
  --header-bg: #fff;
  --header-shadow: rgba(0, 0, 0, 0.1);
  --nav-hover-bg: #f5f5f5;
  --nav-active-bg: #eee;
  --link-color: #0066cc;
  --border-color: #eee;
}

.dark-mode {
  --bg-color: #1a1a1a;
  --text-color: #fff;
  --header-bg: #242424;
  --header-shadow: rgba(0, 0, 0, 0.3);
  --nav-hover-bg: #333;
  --nav-active-bg: #404040;
  --link-color: #66b3ff;
  --border-color: #333;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
  transition: background-color 0.3s ease, color 0.3s ease;
}

header {
  background-color: var(--header-bg);
  box-shadow: 0 1px 3px var(--header-shadow);
  position: sticky;
  top: 0;
  z-index: 100;
  height: 80px;
  display: flex;
  align-items: center;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 600;
  font-size: 1.5rem;
  color: var(--text-color);
  text-decoration: none;
  transition: opacity 0.3s ease;
}

.logo-img {
  width: 32px;
  height: 32px;
}

.logo:hover {
  opacity: 0.8;
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
  color: var(--text-color);
  text-decoration: none;
  transition: color 0.2s;
  padding: 8px 16px;
  border-radius: 4px;
}

.nav-link:hover {
  background-color: var(--nav-hover-bg);
}

.nav-link.active {
  font-weight: bold;
  background-color: var(--nav-active-bg);
}

.handbook-header {
  margin-bottom: 20px;
}

.handbook-header h1 {
  font-size: 2rem;
  margin-bottom: 10px;
  color: var(--text-color);
}

.handbook-header p {
  font-size: 1.2rem;
  color: var(--text-color);
}

.update-info {
  font-size: 0.8rem;
  color: var(--text-color);
}

.feedback-link {
  margin-top: 10px;
}

.feedback-link a {
  color: var(--text-color);
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.3s ease;
}

.feedback-link a:hover {
  color: var(--link-color);
  text-decoration: underline;
}

footer {
  background-color: #000;
  padding: 40px 0;
  color: #fff;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  text-align: center;
}

.footer-info {
  margin-bottom: 30px;
}

.footer-info p {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
  max-width: 800px;
  margin: 0 auto;
}

.reference-info {
  margin-top: 10px;
}

.reference-info a {
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  transition: color 0.3s ease;
}

.reference-info a:hover {
  color: #fff;
  text-decoration: underline;
}

.footer-links {
  margin: 30px auto;
  text-align: center;
}

.social-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.social-link {
  position: relative;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: color 0.3s ease;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
}

.social-link i {
  font-size: 24px;
}

.social-link span {
  display: block;
  font-size: 12px;
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
  width: 120px;
  height: 120px;
}

.social-link:hover {
  color: #fff;
}

.social-link:hover .qr-tooltip {
  opacity: 1;
  visibility: visible;
}

.qr-tooltip img {
  width: 100%;
  height: 100%;
  display: block;
}

.footer-bottom {
  text-align: center;
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.8rem;
  margin-top: 20px;
}

/* 修改主内容区域背景色 */
.main-content {
  background-color: var(--bg-color);
  color: var(--text-color);
  min-height: 100vh;
  padding: 40px 0;
}

/* 仅在移动端显示菜单按钮 */
@media (max-width: 768px) {
  .menu-toggle {
    display: block;
    background: none;
    border: none;
    padding: 10px;
    cursor: pointer;
    position: relative;
    width: 30px;
    height: 30px;
  }
  
  .menu-toggle span {
    display: block;
    width: 100%;
    height: 2px;
    background-color: var(--text-color);
    margin: 6px 0;
    transition: all 0.3s ease;
    position: absolute;
    left: 0;
  }

  .menu-toggle span:first-child {
    top: 0;
  }

  .menu-toggle span:nth-child(2) {
    top: 50%;
    transform: translateY(-50%);
  }

  .menu-toggle span:last-child {
    bottom: 0;
  }

  /* 菜单打开时的动画效果 */
  .menu-toggle.menu-open span:first-child {
    transform: rotate(45deg);
    top: 50%;
  }

  .menu-toggle.menu-open span:nth-child(2) {
    opacity: 0;
  }

  .menu-toggle.menu-open span:last-child {
    transform: rotate(-45deg);
    bottom: 50%;
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
    background: var(--bg-color);
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  
  .main-nav {
    flex-direction: column;
    gap: 10px;
  }

  .social-list {
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .social-link {
    margin: 10px;
  }
}

.theme-toggle {
  background: none;
  border: none;
  color: var(--text-color);
  cursor: pointer;
  padding: 8px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s ease;
}

.theme-toggle:hover {
  background-color: var(--nav-hover-bg);
}

.theme-toggle i {
  font-size: 1.2rem;
}
</style> 