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
      <div class="container">
        <div class="footer-content">
          <div class="footer-info">
            <div class="footer-logo">
              <img src="/images/waytoagi.png" alt="WaytoAGI Logo">
            </div>
            <p>即梦图片3.0模型是由ByteDance开发的新一代AI图像生成技术，提供真实、高清、专业的图像创作体验。</p>
          </div>
          <div class="footer-links">
            <div class="footer-column">
              <h4>关注我们</h4>
              <ul class="social-list">
                <li>
                  <a href="https://github.com/iaiuse" target="_blank" class="social-link">
                    <i class="fab fa-github"></i>
                    GitHub
                    <div class="qr-tooltip">
                      <img src="/qr/github-qr.png" alt="GitHub QR Code">
                      <p>扫码关注我们的GitHub</p>
                    </div>
                  </a>
                </li>
                <li>
                  <a href="https://okjk.co/T4JBo0" target="_blank" class="social-link">
                    <i class="fas fa-compass"></i>
                    即刻
                    <div class="qr-tooltip">
                      <img src="/qr/jike-qr.png" alt="即刻 QR Code">
                      <p>扫码关注我们的即刻</p>
                    </div>
                  </a>
                </li>
                <li>
                  <a href="https://www.xiaohongshu.com/user/profile/5b2bc6dbf7e8b97ff70a63b2" target="_blank" class="social-link">
                    <i class="fas fa-book"></i>
                    小红书
                    <div class="qr-tooltip">
                      <img src="/qr/xiaohongshu-qr.png" alt="小红书 QR Code">
                      <p>扫码关注我们的小红书</p>
                    </div>
                  </a>
                </li>
                <li>
                  <a href="https://mp.weixin.qq.com/s/Eh8vlal4L02eToTOlaeFww" target="_blank" class="social-link">
                    <i class="fab fa-weixin"></i>
                    公众号
                    <div class="qr-tooltip">
                      <img src="/qr/wechat-qr.png" alt="公众号 QR Code">
                      <p>扫码关注我们的公众号</p>
                    </div>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>© 2025 大雨@waytoagi. All rights reserved.</p>
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
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  width: 100%;
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
  padding: 15px 20px;
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
}

.main-nav {
  display: flex;
  align-items: center;
  gap: 30px;
}

.nav-link {
  color: #666;
  text-decoration: none;
  font-size: 1.1rem;
  font-weight: 500;
  padding: 5px 0;
  position: relative;
  transition: color 0.2s ease;
}

.nav-link:hover {
  color: #0066cc;
}

.nav-link.active {
  color: #0066cc;
}

.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: #0066cc;
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
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  width: 280px;
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
  border-left: 8px solid transparent;
  border-right: 8px solid transparent;
  border-bottom: 8px solid white;
}

.social-tooltip-title {
  font-weight: 500;
  color: #333;
  margin-bottom: 15px;
  font-size: 1rem;
  text-align: center;
}

.social-tooltip-qrcode {
  width: 180px;
  height: 180px;
  margin: 0 auto 15px;
  border-radius: 8px;
  overflow: hidden;
}

.social-tooltip-qrcode img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.social-tooltip-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.social-tooltip-link {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #666;
  text-decoration: none;
  font-size: 0.9rem;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.social-tooltip-link:hover {
  background: #f5f9ff;
  color: #0066cc;
}

.social-tooltip-link img {
  width: 18px;
  height: 18px;
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
@media (max-width: 768px) {
  .menu-toggle {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 30px;
    height: 20px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 0;
    z-index: 100;
  }

  .header-right {
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    display: none;
  }

  .header-right.menu-open {
    display: block;
  }

  .header-container {
    flex-wrap: wrap;
  }

  .main-nav {
    flex-direction: column;
    align-items: flex-start;
    padding: 20px 0;
  }

  .nav-link {
    width: 100%;
    padding: 10px 0;
  }

  .menu-open .menu-toggle span:first-child {
    transform: rotate(45deg) translate(5px, 5px);
  }

  .menu-open .menu-toggle span:nth-child(2) {
    opacity: 0;
  }

  .menu-open .menu-toggle span:last-child {
    transform: rotate(-45deg) translate(5px, -5px);
  }
}

/* Footer styles */
.social-list {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.social-link {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #aaa;
  text-decoration: none;
  padding: 8px 12px;
  border-radius: 6px;
  transition: all 0.3s ease;
  position: relative;
}

.social-link i {
  font-size: 20px;
  transition: transform 0.3s ease;
}

.social-link:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.1);
}

.social-link:hover i {
  transform: scale(1.1);
}

.qr-tooltip {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%) translateY(-10px);
  background: white;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 1000;
  width: 160px;
  text-align: center;
}

.qr-tooltip img {
  width: 130px;
  height: 130px;
  margin-bottom: 10px;
  border-radius: 4px;
}

.qr-tooltip p {
  color: #333;
  font-size: 12px;
  margin: 0;
}

.social-link:hover .qr-tooltip {
  opacity: 1;
  visibility: visible;
  transform: translateX(-50%) translateY(0);
}

@media (max-width: 768px) {
  .qr-tooltip {
    display: none;
  }
  
  .social-list {
    gap: 10px;
  }
  
  .social-link {
    padding: 6px 10px;
  }
  
  .social-link i {
    font-size: 18px;
  }
}
</style> 