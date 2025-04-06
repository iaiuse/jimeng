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
    description: '当前流行的艺术和设计风格，适合紧跟潮流创作',
    items: [
      { 
        name: '赛博朋克', 
        description: '未来科技与复古元素的碰撞',
        filename: 'trend/cyberpunk.webp',
        alt: '赛博朋克风格'
      },
      { 
        name: '蒸汽朋克', 
        description: '维多利亚时代与蒸汽机械的融合',
        filename: 'trend/steampunk.webp',
        alt: '蒸汽朋克风格'
      },
      { 
        name: '极简主义', 
        description: '简约至上的设计理念',
        filename: 'trend/minimalism.webp',
        alt: '极简主义'
      },
      { 
        name: '波普艺术', 
        description: '流行文化与艺术的结合',
        filename: 'trend/pop.webp',
        alt: '波普艺术'
      },
      { 
        name: '新艺术', 
        description: '自然与装饰艺术的融合',
        filename: 'trend/art-nouveau.webp',
        alt: '新艺术风格'
      },
      { 
        name: '后现代', 
        description: '打破传统，追求创新',
        filename: 'trend/postmodern.webp',
        alt: '后现代风格'
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