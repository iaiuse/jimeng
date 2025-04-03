<template>
  <div class="app">
    <header>
      <div class="header-container container">
        <a href="#" class="logo">
          <img src="https://placehold.co/120x30" alt="ByteDance Logo">
          即梦图片3.0
        </a>
        <div class="header-right">
          <div class="main-nav">
            <button 
              v-for="tab in tabs" 
              :key="tab.id"
              class="nav-button"
              :class="{ active: currentTab === tab.id }"
              @click="currentTab = tab.id"
            >
              {{ tab.name }}
            </button>
          </div>
          <div class="social-links">
            <a href="#" class="social-link">
              <img src="/icons/wechat.svg" alt="公众号" class="social-icon">
              <div class="social-tooltip">
                <div class="social-tooltip-title">关注我们</div>
                <div class="social-tooltip-links">
                  <a href="https://github.com/your-username" target="_blank" class="social-tooltip-link">
                    <img src="/icons/github.svg" alt="GitHub">
                    GitHub
                  </a>
                  <a href="https://mp.weixin.qq.com" target="_blank" class="social-tooltip-link">
                    <img src="/icons/wechat.svg" alt="公众号">
                    公众号
                  </a>
                  <a href="https://xiaohongshu.com" target="_blank" class="social-tooltip-link">
                    <img src="/icons/xiaohongshu.svg" alt="小红书">
                    小红书
                  </a>
                  <a href="https://jike.xyz" target="_blank" class="social-tooltip-link">
                    <img src="/icons/jike.svg" alt="即刻">
                    即刻
                  </a>
                </div>
              </div>
            </a>
          </div>
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
      <div class="container">
        <div class="footer-content">
          <div class="footer-info">
            <div class="footer-logo">
              <img src="https://placehold.co/120x40" alt="ByteDance Logo">
            </div>
            <p>即梦图片3.0模型是由ByteDance开发的新一代AI图像生成技术，提供真实、高清、专业的图像创作体验。</p>
          </div>
          <div class="footer-links">
            <div class="footer-column">
              <h4>关注我们</h4>
              <ul>
                <li>
                  <a href="https://jike.xyz" target="_blank" class="social-link">
                    <img src="/icons/jike.svg" alt="即刻" class="social-icon">
                    即刻
                  </a>
                </li>
                <li>
                  <a href="https://xiaohongshu.com" target="_blank" class="social-link">
                    <img src="/icons/xiaohongshu.svg" alt="小红书" class="social-icon">
                    小红书
                  </a>
                </li>
                <li>
                  <a href="https://mp.weixin.qq.com" target="_blank" class="social-link">
                    <img src="/icons/wechat.svg" alt="公众号" class="social-icon">
                    公众号
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>© 2025 ByteDance. All rights reserved.</p>
        </div>
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
</script>

<style>
/* Global styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

body {
  background-color: #fafafa;
  color: #333;
  line-height: 1.6;
  font-size: 16px;
}

.container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 30px;
}

/* Header styles */
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
  padding: 20px 30px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 15px;
  font-weight: 500;
  font-size: 1.4rem;
  color: #333;
  text-decoration: none;
}

.logo img {
  height: 32px;
}

.header-right {
  display: flex;
  align-items: center;
  gap: 30px;
}

.social-links {
  display: flex;
  align-items: center;
  margin-left: 20px;
}

.social-link {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #666;
  text-decoration: none;
  font-size: 0.9rem;
  padding: 6px 12px;
  border-radius: 6px;
  transition: all 0.2s ease;
  position: relative;
}

.social-link:hover {
  background: #f5f9ff;
  color: #0066cc;
}

.social-link:hover .social-tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.social-icon {
  width: 20px;
  height: 20px;
}

.social-tooltip {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(10px);
  background: white;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  width: 200px;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 1000;
}

.social-tooltip::before {
  content: '';
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 0;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-bottom: 6px solid white;
}

.social-tooltip-title {
  font-weight: 500;
  color: #333;
  margin-bottom: 8px;
  font-size: 0.95rem;
}

.social-tooltip-links {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.social-tooltip-link {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #666;
  text-decoration: none;
  font-size: 0.85rem;
  padding: 4px 8px;
  border-radius: 4px;
  transition: all 0.2s ease;
}

.social-tooltip-link:hover {
  background: #f5f9ff;
  color: #0066cc;
}

.social-tooltip-link img {
  width: 16px;
  height: 16px;
}

.main-nav {
  display: flex;
  align-items: center;
  gap: 20px;
}

.nav-button {
  padding: 12px 25px;
  background-color: white;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  color: #333;
  font-weight: 500;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.nav-button:hover {
  background-color: #f5f9ff;
  border-color: #0066cc;
  color: #0066cc;
}

.nav-button.active {
  background-color: #0066cc;
  color: white;
  border-color: #0066cc;
}

/* Main content styles */
.main-content {
  padding: 50px 0;
}

.handbook-header {
  padding: 30px 0 50px;
  text-align: center;
}

.handbook-header h1 {
  font-size: 2.8rem;
  color: #333;
  margin-bottom: 20px;
  font-weight: 600;
}

.handbook-header p {
  font-size: 1.3rem;
  color: #666;
  max-width: 800px;
  margin: 0 auto 20px;
}

.handbook-header .update-info {
  font-size: 1rem;
  color: #777;
}

/* Footer styles */
footer {
  background-color: #1a1a1a;
  color: #ddd;
  padding: 40px 0 20px;
  margin-top: 60px;
}

.footer-content {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 30px;
}

.footer-info {
  max-width: 300px;
}

.footer-logo img {
  height: 30px;
  margin-bottom: 15px;
}

.footer-links {
  display: flex;
  gap: 50px;
  flex-wrap: wrap;
}

.footer-column h4 {
  color: white;
  margin-bottom: 15px;
  font-size: 1rem;
  font-weight: 500;
}

.footer-column ul {
  list-style: none;
}

.footer-column ul li {
  margin-bottom: 8px;
}

.footer-column ul li a {
  color: #aaa;
  font-size: 0.9rem;
  text-decoration: none;
  transition: color 0.2s;
}

.footer-column ul li a:hover {
  color: white;
}

.footer-bottom {
  text-align: center;
  padding-top: 30px;
  margin-top: 30px;
  border-top: 1px solid #333;
  color: #888;
  font-size: 0.85rem;
}

/* Responsive styles */
@media (max-width: 1200px) {
  .social-link span {
    display: none;
  }
  
  .social-links {
    gap: 10px;
  }
  
  .social-link {
    padding: 6px;
  }
}

@media (max-width: 960px) {
  .header-right {
    gap: 15px;
  }
  
  .social-links {
    margin-left: 10px;
  }
}

@media (max-width: 768px) {
  .social-links {
    display: none;
  }
}

@media (max-width: 768px) {
  .section-title {
    font-size: 1.3rem;
  }
  
  .handbook-header h1 {
    font-size: 1.8rem;
  }
}
</style> 