<template>
  <section id="response-dictionary">
    <div class="section-header">
      <div class="section-number">3</div>
      <h2 class="section-title">响应词典</h2>
    </div>
    
    <!-- 添加浮动导航菜单 -->
    <div class="floating-nav" :class="{ 'is-visible': showFloatingNav }">
      <div class="nav-items">
        <div v-for="feature in features" 
             :key="feature.id" 
             class="nav-item"
             :class="{ 'active': activeSection === `feature-${feature.id}` }"
             @click="scrollToSection(`feature-${feature.id}`)">
          <div class="nav-item-content">
            <div class="nav-item-title">{{ feature.title }}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="feature-grid">
      <div v-for="feature in features" 
           :key="feature.id" 
           class="feature-card"
           :id="`feature-${feature.id}`">
        <h3><span>{{ feature.title }}</span></h3>
        <p>{{ feature.description }}</p>
        
        <div class="image-grid">
          <div v-for="(item, index) in feature.items" 
               :key="index" 
               class="image-item"
               @click="openPreview(feature.items, index)">
            <div class="category-label">{{ item.name }}</div>
            <div class="image-wrapper">
              <img :src="getImageUrl(item.filename)" 
                   :alt="item.name" 
                   loading="lazy">
              <div class="image-overlay">
                <div class="image-title">{{ item.name }}</div>
                <div class="image-description">{{ item.description }}</div>
              </div>
            </div>
            <div class="image-caption">
              <div class="image-title">{{ item.name }}</div>
              <div class="image-description">{{ item.description }}</div>
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
import { ref, onMounted, onUnmounted } from 'vue'
import ImagePreview from './ImagePreview.vue'

const getImageUrl = (filename: string) => {
  return `https://jimeng-image.iaiuse.com/3.0/response-directonary/${filename}`
}

// 图片预览相关状态
const isPreviewVisible = ref(false)
const previewImages = ref([])
const previewIndex = ref(0)

// 打开预览
const openPreview = (items: any[], index: number) => {
  previewImages.value = items.map(item => ({
    src: getImageUrl(item.filename),
    title: item.name,
    description: item.description,
    alt: item.alt
  }))
  previewIndex.value = index
  isPreviewVisible.value = true
}

// 关闭预览
const closePreview = () => {
  isPreviewVisible.value = false
}

// 浮动导航相关
const showFloatingNav = ref(false)
const activeSection = ref('')

// 滚动到指定区域
const scrollToSection = (sectionId: string) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

// 检查滚动位置并更新导航状态
const checkScroll = () => {
  // 显示/隐藏浮动导航
  showFloatingNav.value = window.scrollY > 200

  // 更新当前激活的区域
  const sections = features.map(f => `feature-${f.id}`)
  for (const sectionId of sections) {
    const element = document.getElementById(sectionId)
    if (element) {
      const rect = element.getBoundingClientRect()
      if (rect.top <= 100 && rect.bottom >= 100) {
        activeSection.value = sectionId
        break
      }
    }
  }
}

// 监听滚动事件
onMounted(() => {
  window.addEventListener('scroll', checkScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', checkScroll)
})

const features = [
  {
    id: 1,
    title: '热门词',
    description: '当前最受欢迎的响应词，适合快速生成高质量图像',
    items: [
      { 
        name: '胶片闪光', 
        description: '胶片，闪光灯拍摄，过曝，压暗周围颜色，明影加重',
        filename: 'hot/1.webp',  // 兔子割草图
        alt: '胶片闪光效果'
      },
      { 
        name: '过曝强光', 
        description: '过曝，强对比，胶片摄影，闪光灯拍摄，极简',
        filename: 'hot/2.webp',  // 白猫图
        alt: '过曝强光效果'
      },
      { 
        name: '冷色光影', 
        description: '过曝，冷色调，光影氛围，强对比',
        filename: 'hot/3.webp',  // 橙子图
        alt: '冷色光影效果'
      },
      { 
        name: '蓝调胶片', 
        description: '蓝色调，胶片质感，氛围感，极简',
        filename: 'hot/4.webp',  // 雪地小树图
        alt: '蓝调胶片风格'
      },
      { 
        name: '液态金属', 
        description: '液态金属',
        filename: 'hot/5.webp',  // 金属橙子图
        alt: '液态金属效果'
      },
      { 
        name: '水晶光效', 
        description: '水晶xx，由冰晶雕琢而成，电影级光线',
        filename: 'hot/6.webp',  // 粉色水晶球图
        alt: '水晶光效'
      },
      { 
        name: 'INS风格', 
        description: 'ins风',
        filename: 'hot/7.webp',  // 女孩抱狗图
        alt: 'INS风格'
      },
      { 
        name: '90s动画', 
        description: '90s Japanese anime',
        filename: 'hot/8.webp',  // 水手服动画女孩图
        alt: '90年代动画风格'
      },
      { 
        name: '古早日漫', 
        description: '古早日漫风格',
        filename: 'hot/9.webp',  // 粉色蝴蝶结动漫女孩图
        alt: '古早日漫风格'
      },
      { 
        name: '强对比氛围', 
        description: '强对比，氛围感',
        filename: 'hot/10.webp',  // 金发女孩图
        alt: '强对比氛围效果'
      },
      { 
        name: '昭和复古', 
        description: '昭和复古',
        filename: 'hot/11.webp',  // 和服女性图
        alt: '昭和复古风格'
      },
      { 
        name: '生命力', 
        description: '生命力，高饱和度，高对比，胶片',
        filename: 'hot/12.webp',  // 笑容女孩图
        alt: '生命力效果'
      },
      { 
        name: '抓拍', 
        description: '抓拍',
        filename: 'hot/13.webp',  // 夜景人物图
        alt: '抓拍效果'
      },
      { 
        name: '老照片', 
        description: '老照片，胶片感，褪色，低饱和度',
        filename: 'hot/14.webp',  // 鳄鱼墨镜图
        alt: '老照片效果'
      },
      { 
        name: '舞蹈美学', 
        description: '拍摄模糊 失焦美学',
        filename: 'hot/15.webp',  // 舞者模糊图
        alt: '舞蹈美学效果'
      },
      { 
        name: 'Retro Snapshot', 
        description: 'Retro Snapshot',
        filename: 'hot/16.webp',  // 复古女孩照片
        alt: 'Retro Snapshot效果'
      },
      { 
        name: '美式叛逆风', 
        description: '美式叛逆青春风格',
        filename: 'hot/17.webp',  // 
        alt: '美式叛逆青春风格'
      },
      { 
        name: 'X光片', 
        description: 'X光片风格',
        filename: 'hot/18.webp',  // X光片兔子图
        alt: 'X光片风格，骨骼透视效果'
      },
      { 
        name: '美式复古儿童书籍', 
        description: '美式复古儿童书籍封面风格',
        filename: 'hot/19.webp',  // 可爱女孩吹泡泡图
        alt: '可爱萌系风格'
      },
      { 
        name: '可爱萌系', 
        description: '可爱萌系插画风格',
        filename: 'hot/20.webp',  // 少女漫画风格图
        alt: '可爱萌系插画风格'
      },
      { 
        name: '少女漫画', 
        description: '少女漫画风格，清新唯美',
        filename: 'hot/21.webp',  // 美式叛逆风格图
        alt: '少女漫画风格'
      },
      { 
        name: 'Nakada Ikumi', 
        description: 'Nakada Ikumi',
        filename: 'hot/22.webp',  // 泡泡女孩水彩图
        alt: 'Nakada Ikumi风格'
      },
      { 
        name: '老式绘本', 
        description: '老式绘本 欧美绘本',
        filename: 'hot/23.webp',  // 爱丽丝梦游仙境图
        alt: '老式绘本风格'
      },
      { 
        name: '卡哇伊', 
        description: '卡哇伊',
        filename: 'hot/24.webp',  // 粉色女孩图
        alt: '卡哇伊风格'
      },
      { 
        name: '扁平插画', 
        description: '高饱和度，扁平画面风格，粗线条',
        filename: 'hot/25.webp',  // 橙色猫咪图
        alt: '扁平插画风格'
      },
      { 
        name: '互联网怀旧风', 
        description: '互联网怀旧风',
        filename: 'hot/26.webp',  // 蓝色喷泉图
        alt: '互联网怀旧风格'
      },
      { 
        name: '复古亮闪闪', 
        description: '复古亮闪闪',
        filename: 'hot/27.webp',  // 牛角面包图
        alt: '复古亮闪效果'
      },
      { 
        name: '九宫格表情包', 
        description: '九宫格表情包',
        filename: 'hot/28.webp',  // 猫咪表情包图
        alt: '九宫格表情包'
      },
      { 
        name: '绘本手稿风', 
        description: '绘本手稿风',
        filename: 'hot/29.webp',  // 商务人士图
        alt: '绘本手稿风格'
      },
      { 
        name: '古早四格漫画风', 
        description: '古早四格漫画风',
        filename: 'hot/30.webp',  // 商务人士走路图
        alt: '古早四格漫画风格'
      }
    ]
  },
  {
    id: 2,
    title: '美学词',
    description: '不同美学风格的响应词，适合特定艺术风格创作',
    items: [
      // 色调类
      { 
        name: '冷色调', 
        description: '偏冷色系的色调效果',
        filename: 'aesthetic/image001.webp',
        alt: '冷色调效果'
      },
      { 
        name: '暖色调', 
        description: '偏暖色系的色调效果',
        filename: 'aesthetic/image002.webp',
        alt: '暖色调效果'
      },
      { 
        name: '亮调', 
        description: '明亮的色调效果',
        filename: 'aesthetic/image003.webp',
        alt: '亮调效果'
      },
      { 
        name: '暗调', 
        description: '暗沉的色调效果',
        filename: 'aesthetic/image004.webp',
        alt: '暗调效果'
      },
      { 
        name: '高对比', 
        description: '强烈的明暗对比效果',
        filename: 'aesthetic/image005.webp',
        alt: '高对比效果'
      },
      { 
        name: '低对比', 
        description: '柔和的明暗对比效果',
        filename: 'aesthetic/image006.webp',
        alt: '低对比效果'
      },
      { 
        name: '青橙色调', 
        description: '青色和橙色的互补色调',
        filename: 'aesthetic/image007.webp',
        alt: '青橙色调效果'
      },
      { 
        name: '黄绿色调', 
        description: '黄色和绿色的过渡色调',
        filename: 'aesthetic/image008.webp',
        alt: '黄绿色调效果'
      },
      { 
        name: '绿色调', 
        description: '以绿色为主的色调效果',
        filename: 'aesthetic/image009.webp',
        alt: '绿色调效果'
      },
      { 
        name: '低饱和', 
        description: '颜色饱和度较低的效果',
        filename: 'aesthetic/image010.webp',
        alt: '低饱和效果'
      },
      { 
        name: '高饱和', 
        description: '颜色饱和度较高的效果',
        filename: 'aesthetic/image011.webp',
        alt: '高饱和效果'
      },
      { 
        name: '橙蓝色调', 
        description: '橙色和蓝色的互补色调',
        filename: 'aesthetic/image012.webp',
        alt: '橙蓝色调效果'
      },
      { 
        name: '青绿色调', 
        description: '青色和绿色的过渡色调',
        filename: 'aesthetic/image013.webp',
        alt: '青绿色调效果'
      },
      { 
        name: '蓝绿色调', 
        description: '蓝色和绿色的过渡色调',
        filename: 'aesthetic/image014.webp',
        alt: '蓝绿色调效果'
      },
      { 
        name: '粉蓝色调', 
        description: '粉色和蓝色的梦幻色调',
        filename: 'aesthetic/image015.webp',
        alt: '粉蓝色调效果'
      },
      { 
        name: '青色调', 
        description: '以青色为主的色调效果',
        filename: 'aesthetic/image016.webp',
        alt: '青色调效果'
      },
      { 
        name: '红色调', 
        description: '以红色为主的色调效果',
        filename: 'aesthetic/image017.webp',
        alt: '红色调效果'
      },
      { 
        name: '紫色调', 
        description: '以紫色为主的色调效果',
        filename: 'aesthetic/image018.webp',
        alt: '紫色调效果'
      },
      // 光线类
      { 
        name: '晨光', 
        description: '清晨柔和的自然光线',
        filename: 'aesthetic/image019.webp',
        alt: '晨光效果'
      },
      { 
        name: '夕阳光', 
        description: '黄昏温暖的自然光线',
        filename: 'aesthetic/image020.webp',
        alt: '夕阳光效果'
      },
      { 
        name: '黄金时段光线', 
        description: '日出日落时的黄金光线',
        filename: 'aesthetic/image021.webp',
        alt: '黄金时段光线效果'
      },
      { 
        name: '发丝光', 
        description: '透过发丝的柔和光线',
        filename: 'aesthetic/image022.webp',
        alt: '发丝光效果'
      },
      { 
        name: '高调照明', 
        description: '明亮的高调光线效果',
        filename: 'aesthetic/image023.webp',
        alt: '高调照明效果'
      },
      { 
        name: '暗光/低调照明', 
        description: '暗沉的低调光线效果',
        filename: 'aesthetic/image024.webp',
        alt: '暗光效果'
      },
      // 构图类
      { 
        name: '浅景深/背景虚化', 
        description: '主体清晰，背景虚化的效果',
        filename: 'aesthetic/image025.webp',
        alt: '浅景深效果'
      },
      { 
        name: '侧逆光', 
        description: '侧面打来的逆光效果',
        filename: 'aesthetic/image026.webp',
        alt: '侧逆光效果'
      },
      { 
        name: '轮廓光', 
        description: '突出主体轮廓的光线效果',
        filename: 'aesthetic/image027.webp',
        alt: '轮廓光效果'
      },
      { 
        name: '丁达尔光', 
        description: '光线散射形成的光束效果',
        filename: 'aesthetic/image028.webp',
        alt: '丁达尔光效果'
      },
      { 
        name: 'dappled light', 
        description: '斑驳的光影效果',
        filename: 'aesthetic/image029.webp',
        alt: '斑驳光影效果'
      },
      { 
        name: '光斑', 
        description: '光线形成的斑点效果',
        filename: 'aesthetic/image030.webp',
        alt: '光斑效果'
      },
      // 特殊光效
      { 
        name: '水底光效', 
        description: '水下的光线效果',
        filename: 'aesthetic/image031.webp',
        alt: '水底光效'
      },
      { 
        name: '冷光源', 
        description: '冷色调的光源效果',
        filename: 'aesthetic/image032.webp',
        alt: '冷光源效果'
      },
      { 
        name: '暖光源', 
        description: '暖色调的光源效果',
        filename: 'aesthetic/image033.webp',
        alt: '暖光源效果'
      },
      { 
        name: '火光', 
        description: '火焰的光线效果',
        filename: 'aesthetic/image034.webp',
        alt: '火光效果'
      },
      { 
        name: '烛光', 
        description: '蜡烛的光线效果',
        filename: 'aesthetic/image035.webp',
        alt: '烛光效果'
      },
      { 
        name: '霓虹灯', 
        description: '霓虹灯的光线效果',
        filename: 'aesthetic/image036.webp',
        alt: '霓虹灯效果'
      },
      // 构图和拍摄手法
      { 
        name: '动态模糊', 
        description: '运动产生的模糊效果',
        filename: 'aesthetic/image037.webp',
        alt: '动态模糊效果'
      },
      { 
        name: '低角度摄影', 
        description: '从低处向上拍摄的视角',
        filename: 'aesthetic/image038.webp',
        alt: '低角度摄影效果'
      },
      { 
        name: 'vintage color', 
        description: '复古怀旧的色彩风格',
        filename: 'aesthetic/image039.webp',
        alt: '复古色彩效果'
      },
      { 
        name: '水平线构图', 
        description: '以水平线为主的构图方式',
        filename: 'aesthetic/image040.webp',
        alt: '水平线构图效果'
      },
      { 
        name: '消失点构图', 
        description: '强调透视感的构图方式',
        filename: 'aesthetic/image041.webp',
        alt: '消失点构图效果'
      },
      { 
        name: '对角线构图', 
        description: '以对角线为主的构图方式',
        filename: 'aesthetic/image042.webp',
        alt: '对角线构图效果'
      },
      // 镜头效果
      { 
        name: '鱼眼镜头', 
        description: '广角畸变的鱼眼效果',
        filename: 'aesthetic/image043.webp',
        alt: '鱼眼镜头效果'
      },
      { 
        name: '猫眼镜头', 
        description: '通过圆形镜头拍摄的效果',
        filename: 'aesthetic/image044.webp',
        alt: '猫眼镜头效果'
      },
      { 
        name: '显微镜', 
        description: '微观世界的特写效果',
        filename: 'aesthetic/image045.webp',
        alt: '显微镜效果'
      },
      { 
        name: '柔焦镜头', 
        description: '柔和虚化的焦点效果',
        filename: 'aesthetic/image046.webp',
        alt: '柔焦镜头效果'
      },
      { 
        name: '留白', 
        description: '简约留白的构图效果',
        filename: 'aesthetic/image047.webp',
        alt: '留白效果'
      },
      { 
        name: '微光', 
        description: '微弱光线营造的氛围效果',
        filename: 'aesthetic/image048.webp',
        alt: '微光效果'
      },
      // 拍摄角度
      { 
        name: '正面', 
        description: '正面拍摄的视角',
        filename: 'aesthetic/image049.webp',
        alt: '正面视角'
      },
      { 
        name: '四分之三侧', 
        description: '45度侧面拍摄的视角',
        filename: 'aesthetic/image050.webp',
        alt: '四分之三侧视角'
      },
      { 
        name: '正侧', 
        description: '90度侧面拍摄的视角',
        filename: 'aesthetic/image051.webp',
        alt: '正侧视角'
      },
      { 
        name: '背面', 
        description: '背面拍摄的视角',
        filename: 'aesthetic/image052.webp',
        alt: '背面视角'
      },
      { 
        name: '俯视视角', 
        description: '从上往下拍摄的视角',
        filename: 'aesthetic/image053.webp',
        alt: '俯视视角'
      },
      { 
        name: '仰视视角', 
        description: '从下往上拍摄的视角',
        filename: 'aesthetic/image054.webp',
        alt: '仰视视角'
      },
      // 景别
      { 
        name: '大特写镜头', 
        description: '极近距离拍摄的特写',
        filename: 'aesthetic/image055.webp',
        alt: '大特写镜头'
      },
      { 
        name: '特写', 
        description: '近距离拍摄的特写',
        filename: 'aesthetic/image056.webp',
        alt: '特写镜头'
      },
      { 
        name: '近景', 
        description: '近距离拍摄的场景',
        filename: 'aesthetic/image057.webp',
        alt: '近景镜头'
      },
      { 
        name: '中景', 
        description: '中等距离拍摄的场景',
        filename: 'aesthetic/image058.webp',
        alt: '中景镜头'
      },
      { 
        name: 'full shot', 
        description: '完整拍摄的全身场景',
        filename: 'aesthetic/image059.webp',
        alt: '全身镜头'
      },
      { 
        name: '大远景', 
        description: '远距离拍摄的宽阔场景',
        filename: 'aesthetic/image060.webp',
        alt: '大远景镜头'
      }
    ]
  },
  {
    id: 3,
    title: '潮流风格',
    description: '当前流行的艺术和插画风格，适合创作不同类型的视觉作品',
    items: [
      { 
        name: '绘本风格', 
        description: '温暖可爱的儿童绘本风格，柔和的色彩和简单的造型设计',
        filename: 'trend/image001.webp',
        alt: '绘本风格'
      },
      { 
        name: '古风插画', 
        description: '传统东方美学的现代演绎，优雅细腻的线条和意境表现',
        filename: 'trend/image002.webp',
        alt: '古风插画风格'
      },
      { 
        name: 'lo-fi插画', 
        description: '慵懒随性的生活日常风格，温柔细腻的氛围表现',
        filename: 'trend/image003.webp',
        alt: 'lo-fi插画风格'
      },
      { 
        name: '宫崎骏动漫风格', 
        description: '充满诗意和想象力的动画风格，自然与人文的和谐表现',
        filename: 'trend/image004.webp',
        alt: '宫崎骏动漫风格'
      },
      { 
        name: '日漫风格', 
        description: '典型的日本动漫画风，精致的人物设计和场景表现',
        filename: 'trend/image005.webp',
        alt: '日漫风格'
      },
      { 
        name: '赛璐璐风格', 
        description: '经典动画片的视觉风格，清新明快的色彩和造型',
        filename: 'trend/image006.webp',
        alt: '赛璐璐风格'
      },
      { 
        name: '儿童画', 
        description: '天真烂漫的儿童画风格，充满童趣和想象力',
        filename: 'trend/image007.webp',
        alt: '儿童画风格'
      },
      { 
        name: '2D Cartoon Animation', 
        description: '现代2D卡通动画风格，活泼生动的角色设计',
        filename: 'trend/image008.webp',
        alt: '2D卡通动画风格'
      },
      { 
        name: '欧美动画', 
        description: '欧美主流动画风格，富有表现力的角色设计',
        filename: 'trend/image009.webp',
        alt: '欧美动画风格'
      },
      { 
        name: 'Character design', 
        description: '专业的角色设计风格，注重人物个性和细节表现',
        filename: 'trend/image010.webp',
        alt: '角色设计风格'
      },
      { 
        name: 'chibi', 
        description: 'Q版可爱的迷你角色风格，夸张有趣的造型设计',
        filename: 'trend/image011.webp',
        alt: 'Q版角色风格'
      },
      { 
        name: '2D动画风格', 
        description: '现代2D动画制作风格，流畅的线条和动态表现',
        filename: 'trend/image012.webp',
        alt: '2D动画风格'
      },
      { 
        name: 'Riso', 
        description: '独特的印刷艺术风格，粗糙质感和色彩叠加效果',
        filename: 'trend/image013.webp',
        alt: 'Riso印刷风格'
      },
      { 
        name: '渐变风格', 
        description: '现代渐变设计风格，柔和的色彩过渡和氛围营造',
        filename: 'trend/image014.webp',
        alt: '渐变设计风格'
      },
      { 
        name: '国漫风格', 
        description: '中国动画的艺术风格，融合传统与现代的视觉表现',
        filename: 'trend/image015.webp',
        alt: '国漫风格'
      },
      { 
        name: 'pixel', 
        description: '像素艺术风格，复古游戏视觉的现代演绎',
        filename: 'trend/image016.webp',
        alt: '像素艺术风格'
      },
      { 
        name: '我的世界风格', 
        description: '独特的游戏场景风格，梦幻般的色彩和光效',
        filename: 'trend/image017.webp',
        alt: '我的世界风格'
      },
      { 
        name: '中国风', 
        description: '传统中国艺术的现代诠释，水墨意境的优雅表现',
        filename: 'trend/image018.webp',
        alt: '中国风格'
      },
      { 
        name: '3D卡通', 
        description: '现代3D动画风格，立体感强的角色和场景设计',
        filename: 'trend/image019.webp',
        alt: '3D卡通风格'
      },
      { 
        name: '定格动画风格', 
        description: '独特的定格动画效果，精细的模型和材质表现',
        filename: 'trend/image020.webp',
        alt: '定格动画风格'
      },
      { 
        name: '90年代游戏', 
        description: '复古游戏视觉风格，像素化的画面和氛围营造',
        filename: 'trend/image021.webp',
        alt: '90年代游戏风格'
      },
      { 
        name: 'voxel art style', 
        description: '体素艺术风格，方块化的3D视觉效果',
        filename: 'trend/image022.webp',
        alt: '体素艺术风格'
      },
      { 
        name: '盲盒风格', 
        description: '潮玩玩具设计风格，可爱简约的角色造型',
        filename: 'trend/image023.webp',
        alt: '盲盒风格'
      },
      { 
        name: 'low poly', 
        description: '低面数3D风格，几何化的造型和现代感表现',
        filename: 'trend/image024.webp',
        alt: 'low poly风格'
      },
      { 
        name: '美漫风格', 
        description: '美式漫画风格，夸张的动作和强烈的视觉冲击',
        filename: 'trend/image025.webp',
        alt: '美漫风格'
      },
      { 
        name: '皮克斯动画风格', 
        description: 'Pixar动画风格，温暖细腻的情感表达',
        filename: 'trend/image026.webp',
        alt: '皮克斯动画风格'
      },
      { 
        name: '3D cartoon', 
        description: '现代3D卡通风格，活泼可爱的角色设计',
        filename: 'trend/image027.webp',
        alt: '3D卡通风格'
      },
      { 
        name: '厚涂风格', 
        description: '浓重的笔触和色彩，富有质感的绘画效果',
        filename: 'trend/image028.webp',
        alt: '厚涂风格'
      },
      { 
        name: '半厚涂风格', 
        description: '介于写实和厚涂之间的绘画风格，细腻的明暗过渡',
        filename: 'trend/image029.webp',
        alt: '半厚涂风格'
      },
      { 
        name: '奇幻风', 
        description: '奇幻题材的视觉风格，魔法和幻想元素的展现',
        filename: 'trend/image030.webp',
        alt: '奇幻风格'
      },
      { 
        name: 'Ancient China Illustration', 
        description: '中国古代场景插画，传统建筑和人文元素的表现',
        filename: 'trend/image031.webp',
        alt: '中国古代插画'
      },
      { 
        name: '新艺术派风格', 
        description: '新艺术运动风格，优雅流畅的线条和装饰图案',
        filename: 'trend/image032.webp',
        alt: '新艺术派风格'
      },
      { 
        name: '言情小说', 
        description: '言情小说插画风格，浪漫唯美的氛围营造',
        filename: 'trend/image033.webp',
        alt: '言情小说风格'
      },
      { 
        name: 'Barbie style', 
        description: '芭比娃娃风格，明亮活泼的色彩和时尚元素',
        filename: 'trend/image034.webp',
        alt: '芭比风格'
      },
      { 
        name: '概念艺术', 
        description: '游戏和电影概念设计，宏大场景和氛围的构建',
        filename: 'trend/image035.webp',
        alt: '概念艺术风格'
      },
      { 
        name: '奇幻风', 
        description: '奇幻世界的视觉呈现，神秘梦幻的场景设计',
        filename: 'trend/image036.webp',
        alt: '奇幻风格'
      },
      { 
        name: '池核', 
        description: '后现代审美的游泳池场景，独特的氛围营造',
        filename: 'trend/image037.webp',
        alt: '池核风格'
      },
      { 
        name: '怪核', 
        description: '怪诞风格的视觉表现，超现实的场景设计',
        filename: 'trend/image038.webp',
        alt: '怪核风格'
      },
      { 
        name: '分子化', 
        description: '分子结构的视觉效果，科技感的图形设计',
        filename: 'trend/image039.webp',
        alt: '分子化风格'
      },
      { 
        name: '工业设计风', 
        description: '工业产品设计风格，简洁现代的造型语言',
        filename: 'trend/image040.webp',
        alt: '工业设计风格'
      },
      { 
        name: '侘寂风', 
        description: '日本侘寂美学，简约质朴的空间设计',
        filename: 'trend/image041.webp',
        alt: '侘寂风格'
      },
      { 
        name: '中式恐怖', 
        description: '中国传统元素的恐怖风格，阴森诡异的氛围',
        filename: 'trend/image042.webp',
        alt: '中式恐怖风格'
      },
      { 
        name: '视错觉', 
        description: '视觉错觉艺术，令人惊叹的空间错觉效果',
        filename: 'trend/image043.webp',
        alt: '视错觉风格'
      },
      { 
        name: '日系风', 
        description: '日本摄影风格，柔和自然的光线效果',
        filename: 'trend/image044.webp',
        alt: '日系风格'
      },
      { 
        name: '拍摄模糊 失焦美学', 
        description: '艺术性的模糊效果，朦胧梦幻的视觉表现',
        filename: 'trend/image045.webp',
        alt: '失焦美学风格'
      },
      { 
        name: 'Out-of-Focus Aesthetic', 
        description: '失焦摄影美学，柔和朦胧的艺术效果',
        filename: 'trend/image046.webp',
        alt: '失焦美学风格'
      },
      { 
        name: '渐变美学', 
        description: '渐变色彩的艺术表现，优雅流畅的色彩过渡',
        filename: 'trend/image047.webp',
        alt: '渐变美学风格'
      },
      { 
        name: '宝利来', 
        description: '宝丽来相机风格，复古怀旧的照片效果',
        filename: 'trend/image048.webp',
        alt: '宝利来风格'
      },
      { 
        name: 'Atmospheric Vibe', 
        description: '氛围感摄影，营造特定情绪的视觉效果',
        filename: 'trend/image049.webp',
        alt: '氛围感风格'
      },
      { 
        name: '中式梦核', 
        description: '中国传统元素的梦幻演绎，朦胧意境的表现',
        filename: 'trend/image050.webp',
        alt: '中式梦核风格'
      },
      { 
        name: '禅意新中式', 
        description: '现代禅意美学，简约淡雅的东方韵味',
        filename: 'trend/image051.webp',
        alt: '禅意新中式风格'
      },
      { 
        name: 'Zen-inspired New Chinese Style', 
        description: '禅意启发的新中式设计，现代与传统的融合',
        filename: 'trend/image052.webp',
        alt: '禅意新中式风格'
      },
      { 
        name: '清冷感', 
        description: '冷色调的视觉风格，清冷疏离的情绪表达',
        filename: 'trend/image053.webp',
        alt: '清冷感风格'
      },
      { 
        name: 'Cool and Detached', 
        description: '冷静疏离的视觉风格，理性克制的设计语言',
        filename: 'trend/image054.webp',
        alt: '冷静疏离风格'
      },
      { 
        name: '野性美', 
        description: '自然野性的视觉风格，粗犷自由的表现手法',
        filename: 'trend/image055.webp',
        alt: '野性美风格'
      },
      { 
        name: '民国风', 
        description: '民国时期的复古风格，典雅含蓄的艺术表现',
        filename: 'trend/image056.webp',
        alt: '民国风格'
      },
      { 
        name: '老钱风', 
        description: '复古奢华风格，典雅精致的视觉效果',
        filename: 'trend/image057.webp',
        alt: '老钱风格'
      },
      { 
        name: '森系', 
        description: '自然森林系风格，清新自然的氛围营造',
        filename: 'trend/image058.webp',
        alt: '森系风格'
      },
      { 
        name: '欧美杂志封面插画', 
        description: '欧美杂志风格的插画设计，时尚现代的视觉表现',
        filename: 'trend/image059.webp',
        alt: '欧美杂志插画风格'
      },
      { 
        name: '拼贴风', 
        description: '艺术拼贴风格，多元素组合的创意表现',
        filename: 'trend/image060.webp',
        alt: '拼贴风格'
      },
      { 
        name: '小清新', 
        description: '清新淡雅的视觉风格，温柔细腻的情感表达',
        filename: 'trend/image061.webp',
        alt: '小清新风格'
      },
      { 
        name: 'Springtime Aesthetic', 
        description: '春日氛围的视觉美学，明媚温暖的季节表现',
        filename: 'trend/image062.webp',
        alt: '春日美学风格'
      },
      { 
        name: '生命力摄影', 
        description: '充满活力的摄影风格，捕捉生命力量的瞬间',
        filename: 'trend/image063.webp',
        alt: '生命力摄影风格'
      },
      { 
        name: '蜜桃系', 
        description: '粉嫩甜美的视觉风格，温柔可爱的色彩搭配',
        filename: 'trend/image064.webp',
        alt: '蜜桃系风格'
      },
      { 
        name: '奶平平', 
        description: '奶油般柔和的色调，温暖舒适的视觉效果',
        filename: 'trend/image065.webp',
        alt: '奶平平风格'
      },
      { 
        name: '糯叽叽', 
        description: '柔软细腻的视觉效果，温暖治愈的风格表现',
        filename: 'trend/image066.webp',
        alt: '糯叽叽风格'
      },
      { 
        name: '渐变美学', 
        description: '渐变色彩的艺术表现，柔和流畅的视觉效果',
        filename: 'trend/image067.webp',
        alt: '渐变美学风格'
      },
      { 
        name: '宝利来', 
        description: '复古宝丽来相机效果，怀旧温暖的影像风格',
        filename: 'trend/image068.webp',
        alt: '宝利来风格'
      },
      { 
        name: 'Out-of-Focus Aesthetic', 
        description: '艺术性失焦效果，朦胧梦幻的视觉表现',
        filename: 'trend/image069.webp',
        alt: '失焦美学风格'
      },
      { 
        name: '果冻系', 
        description: '透明清新的视觉效果，晶莹剔透的质感表现',
        filename: 'trend/image070.webp',
        alt: '果冻系风格'
      },
      { 
        name: '甜酷辣妹风', 
        description: '潮流街头风格，甜美与酷炫的混搭效果',
        filename: 'trend/image071.webp',
        alt: '甜酷辣妹风格'
      },
      { 
        name: '复古风', 
        description: '怀旧复古风格，经典年代感的艺术表现',
        filename: 'trend/image072.webp',
        alt: '复古风格'
      },
      { 
        name: '小清新', 
        description: '清新淡雅的视觉风格，温柔细腻的情感表达',
        filename: 'trend/image073.webp',
        alt: '小清新风格'
      },
      { 
        name: 'Springtime Aesthetic', 
        description: '春日氛围的视觉美学，明媚温暖的季节表现',
        filename: 'trend/image074.webp',
        alt: '春日美学风格'
      },
      { 
        name: '生命力摄影', 
        description: '充满活力的摄影风格，捕捉生命力量的瞬间',
        filename: 'trend/image075.webp',
        alt: '生命力摄影风格'
      },
      { 
        name: '蜜桃系', 
        description: '粉嫩甜美的视觉风格，温柔可爱的色彩搭配',
        filename: 'trend/image076.webp',
        alt: '蜜桃系风格'
      },
      { 
        name: '奶平平', 
        description: '奶油般柔和的色调，温暖舒适的视觉效果',
        filename: 'trend/image077.webp',
        alt: '奶平平风格'
      },
      { 
        name: '糯叽叽', 
        description: '柔软细腻的视觉效果，温暖治愈的风格表现',
        filename: 'trend/image078.webp',
        alt: '糯叽叽风格'
      },
      { 
        name: '渐变美学', 
        description: '渐变色彩的艺术表现，柔和流畅的视觉效果',
        filename: 'trend/image079.webp',
        alt: '渐变美学风格'
      },
      { 
        name: '宝利来', 
        description: '复古宝丽来相机效果，怀旧温暖的影像风格',
        filename: 'trend/image080.webp',
        alt: '宝利来风格'
      },
      { 
        name: 'Out-of-Focus Aesthetic', 
        description: '艺术性失焦效果，朦胧梦幻的视觉表现',
        filename: 'trend/image081.webp',
        alt: '失焦美学风格'
      },
      { 
        name: '果冻系', 
        description: '透明清新的视觉效果，晶莹剔透的质感表现',
        filename: 'trend/image082.webp',
        alt: '果冻系风格'
      },
      { 
        name: '甜酷辣妹风', 
        description: '潮流街头风格，甜美与酷炫的混搭效果',
        filename: 'trend/image083.webp',
        alt: '甜酷辣妹风格'
      },
      { 
        name: '复古风', 
        description: '怀旧复古风格，经典年代感的艺术表现',
        filename: 'trend/image084.webp',
        alt: '复古风格'
      },
      { 
        name: '电影感', 
        description: '电影级别的视觉效果，富有故事性的画面表现',
        filename: 'trend/image085.webp',
        alt: '电影感风格'
      },
      { 
        name: '赛博朋克', 
        description: '未来科技与复古元素的碰撞，霓虹与金属的视觉冲击',
        filename: 'trend/image086.webp',
        alt: '赛博朋克风格'
      },
      { 
        name: '蒸汽波', 
        description: '复古未来主义风格，怀旧与科技的混搭美学',
        filename: 'trend/image087.webp',
        alt: '蒸汽波风格'
      },
      { 
        name: '极简主义', 
        description: '简约至上的设计理念，纯粹的形式美感',
        filename: 'trend/image088.webp',
        alt: '极简主义风格'
      },
      { 
        name: '未来主义', 
        description: '面向未来的设计风格，科技感与动态美学的结合',
        filename: 'trend/image089.webp',
        alt: '未来主义风格'
      },
      { 
        name: '后现代', 
        description: '打破传统的设计语言，混搭与解构的艺术表现',
        filename: 'trend/image090.webp',
        alt: '后现代风格'
      },
      { 
        name: '新浪漫主义', 
        description: '当代浪漫主义风格，情感与美学的深度表达',
        filename: 'trend/image091.webp',
        alt: '新浪漫主义风格'
      },
      { 
        name: '超现实主义', 
        description: '打破现实逻辑的艺术风格，梦境与现实的交织',
        filename: 'trend/image092.webp',
        alt: '超现实主义风格'
      },
      { 
        name: '波普艺术', 
        description: '流行文化艺术风格，大胆鲜艳的色彩表现',
        filename: 'trend/image093.webp',
        alt: '波普艺术风格'
      },
      { 
        name: '新表现主义', 
        description: '强烈个人情感表达的艺术风格，自由奔放的创作手法',
        filename: 'trend/image094.webp',
        alt: '新表现主义风格'
      },
      { 
        name: '解构主义', 
        description: '打破常规结构的设计风格，重组与创新的视觉效果',
        filename: 'trend/image095.webp',
        alt: '解构主义风格'
      },
      { 
        name: '新古典主义', 
        description: '传统与现代的融合，优雅庄重的艺术表现',
        filename: 'trend/image096.webp',
        alt: '新古典主义风格'
      },
      { 
        name: '工业风', 
        description: '工业元素的艺术化表现，粗犷与精致的平衡',
        filename: 'trend/image097.webp',
        alt: '工业风格'
      },
      { 
        name: '生态艺术', 
        description: '自然与环保主题的艺术表现，生态与美学的结合',
        filename: 'trend/image098.webp',
        alt: '生态艺术风格'
      },
      { 
        name: '数字艺术', 
        description: '数字技术创作的艺术形式，科技与创意的完美融合',
        filename: 'trend/image099.webp',
        alt: '数字艺术风格'
      },
      { 
        name: '新媒体艺术', 
        description: '多媒体技术的艺术表现，交互与创新的视觉体验',
        filename: 'trend/image100.webp',
        alt: '新媒体艺术风格'
      },
      { 
        name: '装置艺术', 
        description: '空间与物件的艺术组合，概念与形式的创意表达',
        filename: 'trend/image101.webp',
        alt: '装置艺术风格'
      },
      { 
        name: '街头艺术', 
        description: '城市文化的艺术表现，自由不羁的创作风格',
        filename: 'trend/image102.webp',
        alt: '街头艺术风格'
      },
      { 
        name: '光影艺术', 
        description: '光与影的艺术效果，氛围与情感的视觉营造',
        filename: 'trend/image103.webp',
        alt: '光影艺术风格'
      },
      { 
        name: '几何艺术', 
        description: '几何形态的艺术表现，规律与变化的视觉美感',
        filename: 'trend/image104.webp',
        alt: '几何艺术风格'
      },
      { 
        name: '有机艺术', 
        description: '自然有机形态的艺术表现，流动与生长的视觉效果',
        filename: 'trend/image105.webp',
        alt: '有机艺术风格'
      },
      { 
        name: '纹理艺术', 
        description: '材质纹理的艺术表现，触感与视觉的双重体验',
        filename: 'trend/image106.webp',
        alt: '纹理艺术风格'
      },
      { 
        name: '抽象艺术', 
        description: '非具象的艺术表现，形式与情感的纯粹表达',
        filename: 'trend/image107.webp',
        alt: '抽象艺术风格'
      },
      { 
        name: '观念艺术', 
        description: '概念与思想的艺术表达，理念与形式的统一',
        filename: 'trend/image108.webp',
        alt: '观念艺术风格'
      },
      { 
        name: '环境艺术', 
        description: '空间环境的艺术设计，场域与体验的整体营造',
        filename: 'trend/image109.webp',
        alt: '环境艺术风格'
      },
      { 
        name: '声音艺术', 
        description: '听觉与视觉的艺术结合，多感官的艺术体验',
        filename: 'trend/image110.webp',
        alt: '声音艺术风格'
      },
      { 
        name: '互动艺术', 
        description: '观众参与的艺术形式，互动与体验的创意表达',
        filename: 'trend/image111.webp',
        alt: '互动艺术风格'
      },
      { 
        name: '混合媒材', 
        description: '多种材料的艺术组合，材质与技法的创新表现',
        filename: 'trend/image112.webp',
        alt: '混合媒材风格'
      },
      { 
        name: '实验艺术', 
        description: '创新探索的艺术形式，突破与实验的创作精神',
        filename: 'trend/image113.webp',
        alt: '实验艺术风格'
      },
      { 
        name: '科技艺术', 
        description: '科技与艺术的融合，创新与美学的结合表达',
        filename: 'trend/image114.webp',
        alt: '科技艺术风格'
      },
      { 
        name: '生物艺术', 
        description: '生命科学与艺术的结合，自然与创造的艺术表现',
        filename: 'trend/image115.webp',
        alt: '生物艺术风格'
      },
      { 
        name: '数据艺术', 
        description: '数据可视化的艺术表现，信息与美学的创意呈现',
        filename: 'trend/image116.webp',
        alt: '数据艺术风格'
      },
      { 
        name: '网络艺术', 
        description: '互联网文化的艺术表现，虚拟与现实的创意融合',
        filename: 'trend/image117.webp',
        alt: '网络艺术风格'
      },
      { 
        name: '游戏艺术', 
        description: '游戏文化的艺术表现，互动与娱乐的创意设计',
        filename: 'trend/image118.webp',
        alt: '游戏艺术风格'
      },
      { 
        name: '时尚艺术', 
        description: '时尚文化的艺术表现，潮流与美学的创意融合',
        filename: 'trend/image119.webp',
        alt: '时尚艺术风格'
      },
      { 
        name: '建筑艺术', 
        description: '建筑空间的艺术表现，结构与美学的完美统一',
        filename: 'trend/image120.webp',
        alt: '建筑艺术风格'
      },
      { 
        name: '舞台艺术', 
        description: '表演空间的艺术设计，戏剧与视觉的创意呈现',
        filename: 'trend/image121.webp',
        alt: '舞台艺术风格'
      },
      { 
        name: '展览艺术', 
        description: '展示空间的艺术策划，陈列与体验的整体设计',
        filename: 'trend/image122.webp',
        alt: '展览艺术风格'
      },
      { 
        name: '商业艺术', 
        description: '商业创意的艺术表现，营销与美学的策略结合',
        filename: 'trend/image123.webp',
        alt: '商业艺术风格'
      },
      { 
        name: '公共艺术', 
        description: '城市空间的艺术创作，环境与人文的和谐统一',
        filename: 'trend/image124.webp',
        alt: '公共艺术风格'
      },
      { 
        name: '民俗艺术', 
        description: '传统文化的艺术表现，民间智慧的创意传承',
        filename: 'trend/image125.webp',
        alt: '民俗艺术风格'
      },
      { 
        name: '手工艺术', 
        description: '手工制作的艺术表现，工艺与创意的完美结合',
        filename: 'trend/image126.webp',
        alt: '手工艺术风格'
      },
      { 
        name: '文字艺术', 
        description: 'typography艺术表现，字体与设计的创意融合',
        filename: 'trend/image127.webp',
        alt: '文字艺术风格'
      },
      { 
        name: '图案艺术', 
        description: '重复图案的艺术设计，规律与变化的视觉韵律',
        filename: 'trend/image128.webp',
        alt: '图案艺术风格'
      },
      { 
        name: '符号艺术', 
        description: '视觉符号的艺术创作，象征与意义的创意表达',
        filename: 'trend/image129.webp',
        alt: '符号艺术风格'
      },
      { 
        name: '空间艺术', 
        description: '三维空间的艺术设计，立体与平面的创意构成',
        filename: 'trend/image130.webp',
        alt: '空间艺术风格'
      },
      { 
        name: '光线艺术', 
        description: '光影效果的艺术表现，明暗与色彩的视觉体验',
        filename: 'trend/image131.webp',
        alt: '光线艺术风格'
      },
      { 
        name: '动态艺术', 
        description: '运动效果的艺术表现，时间与空间的创意演绎',
        filename: 'trend/image132.webp',
        alt: '动态艺术风格'
      },
      { 
        name: '静物艺术', 
        description: '物件构图的艺术表现，质感与光影的细致刻画',
        filename: 'trend/image133.webp',
        alt: '静物艺术风格'
      },
      { 
        name: '人像艺术', 
        description: '人物形象的艺术表现，个性与情感的深入刻画',
        filename: 'trend/image134.webp',
        alt: '人像艺术风格'
      },
      { 
        name: '风景艺术', 
        description: '自然景观的艺术表现，空间与氛围的完美营造',
        filename: 'trend/image135.webp',
        alt: '风景艺术风格'
      },
      { 
        name: '城市艺术', 
        description: '都市景观的艺术表现，现代与人文的视觉记录',
        filename: 'trend/image136.webp',
        alt: '城市艺术风格'
      },
      { 
        name: '水墨艺术', 
        description: '东方水墨的艺术表现，传统与创新的美学融合',
        filename: 'trend/image137.webp',
        alt: '水墨艺术风格'
      },
      { 
        name: '油画艺术', 
        description: '西方油画的艺术表现，色彩与肌理的细腻处理',
        filename: 'trend/image138.webp',
        alt: '油画艺术风格'
      },
      { 
        name: '版画艺术', 
        description: '印刷艺术的创作表现，技法与创意的独特魅力',
        filename: 'trend/image139.webp',
        alt: '版画艺术风格'
      },
      { 
        name: '雕塑艺术', 
        description: '立体造型的艺术表现，形态与空间的三维创作',
        filename: 'trend/image140.webp',
        alt: '雕塑艺术风格'
      },
      { 
        name: '陶艺', 
        description: '陶瓷创作的艺术表现，材质与工艺的完美结合',
        filename: 'trend/image141.webp',
        alt: '陶艺风格'
      },
      { 
        name: '玻璃艺术', 
        description: '玻璃材质的艺术表现，透明与光影的视觉效果',
        filename: 'trend/image142.webp',
        alt: '玻璃艺术风格'
      },
      { 
        name: '金属艺术', 
        description: '金属材质的艺术表现，质感与造型的工艺创作',
        filename: 'trend/image143.webp',
        alt: '金属艺术风格'
      },
      { 
        name: '织物艺术', 
        description: '纺织品的艺术表现，材质与图案的创意设计',
        filename: 'trend/image144.webp',
        alt: '织物艺术风格'
      },
      { 
        name: 'American retro style', 
        description: '美式复古风格，50-60年代美国流行文化的视觉表现',
        filename: 'trend/image145.webp',
        alt: '美式复古风格'
      },
      { 
        name: '波西米亚风', 
        description: '自由波西米亚风格，民族与艺术的混搭美学',
        filename: 'trend/image146.webp',
        alt: '波西米亚风格'
      },
      { 
        name: '像素风，宫崎骏', 
        description: '宫崎骏动画风格的像素艺术演绎',
        filename: 'trend/image147.webp',
        alt: '像素宫崎骏风格'
      },
      { 
        name: '京剧风格', 
        description: '中国京剧艺术的现代演绎，戏曲元素的创新表达',
        filename: 'trend/image148.webp',
        alt: '京剧风格'
      },
      { 
        name: '乐高风格', 
        description: '乐高积木的视觉风格，趣味性与创意性的结合',
        filename: 'trend/image149.webp',
        alt: '乐高风格'
      },
      { 
        name: 'Lowbrow art', 
        description: '低俗艺术风格，街头文化与波普艺术的融合',
        filename: 'trend/image150.webp',
        alt: 'Lowbrow艺术风格'
      },
      { 
        name: '轻酸性设计，扁平渐变风格', 
        description: '清新简约的设计风格，柔和的色彩过渡效果',
        filename: 'trend/image151.webp',
        alt: '轻酸性设计风格'
      },
      { 
        name: '手机壁纸', 
        description: '适合移动设备的壁纸设计，简约现代的视觉效果',
        filename: 'trend/image152.webp',
        alt: '手机壁纸风格'
      },
      { 
        name: 'riso印刷，粗线条', 
        description: 'Risograph印刷效果，粗犷线条的艺术表现',
        filename: 'trend/image153.webp',
        alt: 'riso印刷风格'
      },
      { 
        name: 'flat style', 
        description: '扁平化设计风格，简约清晰的视觉语言',
        filename: 'trend/image154.webp',
        alt: '扁平设计风格'
      },
      { 
        name: '爆炸效果', 
        description: '动态爆炸效果，强烈视觉冲击的艺术表现',
        filename: 'trend/image155.webp',
        alt: '爆炸效果风格'
      },
      { 
        name: '丁丁历险记', 
        description: '经典漫画丁丁历险记的艺术风格，清晰明快的线条表现',
        filename: 'trend/image156.webp',
        alt: '丁丁历险记风格'
      }
    ]
  },
  {
    id: 4,
    title: '影像',
    description: '专业摄影和电影镜头语言，适合影视风格创作',
    items: [
      { 
        name: '大特写', 
        description: '突出细节表情，强调主体特征',
        filename: 'image/close-up.webp',
        alt: '大特写镜头'
      },
      { 
        name: '特写', 
        description: '刻画人物情绪，展现细节特征',
        filename: 'image/close.webp',
        alt: '特写镜头'
      },
      { 
        name: '近景', 
        description: '强调主体特征，突出人物表情',
        filename: 'image/near.webp',
        alt: '近景镜头'
      },
      { 
        name: '中景', 
        description: '展现人物动作，突出场景氛围',
        filename: 'image/medium.webp',
        alt: '中景镜头'
      },
      { 
        name: '全景', 
        description: '完整场景呈现，突出环境氛围',
        filename: 'image/full.webp',
        alt: '全景镜头'
      },
      { 
        name: '大远景', 
        description: '宏大场面展示，突出空间感',
        filename: 'image/wide.webp',
        alt: '大远景镜头'
      }
    ]
  },
  {
    id: 5,
    title: '设计',
    description: '专业设计领域的风格和技巧，适合设计类创作',
    items: [
      { 
        name: '平面设计', 
        description: '视觉传达的艺术表现',
        filename: 'design/graphic.webp',
        alt: '平面设计'
      },
      { 
        name: 'UI设计', 
        description: '用户界面的交互设计',
        filename: 'design/ui.webp',
        alt: 'UI设计'
      },
      { 
        name: '包装设计', 
        description: '产品包装的视觉设计',
        filename: 'design/packaging.webp',
        alt: '包装设计'
      },
      { 
        name: '品牌设计', 
        description: '品牌形象的视觉传达',
        filename: 'design/brand.webp',
        alt: '品牌设计'
      },
      { 
        name: '海报设计', 
        description: '宣传海报的创意设计',
        filename: 'design/poster.webp',
        alt: '海报设计'
      }
    ]
  },
  {
    id: 6,
    title: '艺术',
    description: '传统和现代艺术风格，适合艺术类创作',
    items: [
      { 
        name: '油画', 
        description: '传统油画的艺术表现',
        filename: 'art/oil.webp',
        alt: '油画风格'
      },
      { 
        name: '水彩', 
        description: '水彩画的艺术表现',
        filename: 'art/watercolor.webp',
        alt: '水彩风格'
      },
      { 
        name: '素描', 
        description: '素描的艺术表现',
        filename: 'art/sketch.webp',
        alt: '素描风格'
      },
      { 
        name: '插画', 
        description: '插画的艺术表现',
        filename: 'art/illustration.webp',
        alt: '插画风格'
      },
      { 
        name: '漫画', 
        description: '漫画的艺术表现',
        filename: 'art/comic.webp',
        alt: '漫画风格'
      }
    ]
  },
  {
    id: 7,
    title: '材质',
    description: '不同材质的表现效果，适合材质渲染创作',
    items: [
      { 
        name: '金属', 
        description: '金属材质的表现效果',
        filename: 'material/metal.webp',
        alt: '金属材质'
      },
      { 
        name: '玻璃', 
        description: '玻璃材质的表现效果',
        filename: 'material/glass.webp',
        alt: '玻璃材质'
      },
      { 
        name: '木材', 
        description: '木材材质的表现效果',
        filename: 'material/wood.webp',
        alt: '木材材质'
      },
      { 
        name: '布料', 
        description: '布料材质的表现效果',
        filename: 'material/fabric.webp',
        alt: '布料材质'
      },
      { 
        name: '塑料', 
        description: '塑料材质的表现效果',
        filename: 'material/plastic.webp',
        alt: '塑料材质'
      }
    ]
  }
]
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

.feature-grid {
  display: flex;
  flex-direction: column;
  gap: 40px;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background-color: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  padding: 35px;
  width: 100%;
}

.feature-card h3 {
  font-size: 1.8rem;
  margin-bottom: 20px;
  color: #333;
  display: flex;
  align-items: center;
}

.feature-card h3 span {
  color: #0066cc;
  margin-right: 12px;
  font-weight: 600;
}

.feature-card p {
  color: #666;
  margin-bottom: 25px;
  font-size: 1.2rem;
  line-height: 1.6;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 25px;
  margin-top: 20px;
}

.image-item {
  position: relative;
  cursor: pointer;
  overflow: visible;
  border-radius: 8px;
  background-color: white;
  transition: transform 0.3s ease;
}

.image-wrapper {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  aspect-ratio: 16/9;
  background-color: #f5f5f5;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.image-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.image-item:hover {
  transform: translateY(-2px);
}

.image-item:hover img {
  transform: scale(1.05);
}

.image-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  padding: 20px;
  color: white;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.image-item:hover .image-overlay {
  opacity: 1;
}

.image-caption {
  padding: 12px 0;
  text-align: center;
}

.image-title {
  font-size: 1rem;
  font-weight: 500;
  color: #333;
  margin-bottom: 4px;
}

.image-description {
  font-size: 0.9rem;
  color: #666;
  line-height: 1.4;
}

.category-label {
  position: absolute;
  top: 10px;
  left: 10px;
  background: rgba(0,0,0,0.6);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  z-index: 1;
}

/* 浮动导航样式 */
.floating-nav {
  position: fixed;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  padding: 15px 0;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s ease;
  z-index: 100;
  min-width: 200px;
}

.floating-nav.is-visible {
  opacity: 1;
  visibility: visible;
}

.nav-items {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.nav-item {
  padding: 12px 20px;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
  border-left: 3px solid transparent;
}

.nav-item-content {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.nav-item-title {
  color: #333;
  font-size: 1rem;
  font-weight: 500;
  transition: color 0.2s ease;
}

.nav-item:hover {
  background: #f5f9ff;
  border-left-color: #0066cc;
}

.nav-item:hover .nav-item-title {
  color: #0066cc;
}

.nav-item.active {
  background: #f5f9ff;
  border-left-color: #0066cc;
}

.nav-item.active .nav-item-title {
  color: #0066cc;
}

/* 响应式调整 */
@media (max-width: 1200px) {
  .feature-grid {
    padding: 0 20px;
  }
  
  .image-grid {
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 20px;
  }
}

@media (max-width: 768px) {
  .feature-card {
    padding: 25px;
  }
  
  .image-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
  }
  
  .image-caption {
    padding: 8px 0;
  }

  .image-title {
    font-size: 0.95rem;
  }

  .image-description {
    font-size: 0.85rem;
  }
}

@media (max-width: 480px) {
  .image-grid {
    grid-template-columns: 1fr;
  }
  
  .feature-card h3 {
    font-size: 1.5rem;
  }
}

@media (max-width: 1400px) {
  .floating-nav {
    right: 10px;
    min-width: 180px;
  }
  
  .nav-item {
    padding: 10px 15px;
  }

  .nav-item-title {
    font-size: 0.95rem;
  }
}

@media (max-width: 768px) {
  .floating-nav {
    display: none;
  }
}
</style> 