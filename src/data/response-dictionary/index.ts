import { hotItems } from './hot'
import { aestheticItems } from './aesthetic'
import { trendItems } from './trend'
import { imageItems } from './image'
import { designItems } from './design'
import { artItems } from './art'
import { materialItems } from './material'

export const features = [
  {
    id: 1,
    title: '热门词',
    subtitle: '当前最受欢迎的响应词，适合快速生成高质量图像',
    items: hotItems
  },
  {
    id: 2,
    title: '美学词',
    subtitle: '不同美学风格的响应词，适合特定艺术风格创作',
    items: aestheticItems
  },
  {
    id: 3,
    title: '潮流风格',
    subtitle: '当前流行的艺术和插画风格，适合创作不同类型的视觉作品',
    items: trendItems
  },
  {
    id: 4,
    title: '影像',
    subtitle: '专业摄影和电影镜头语言，适合影视风格创作',
    items: imageItems
  },
  {
    id: 5,
    title: '设计',
    subtitle: '专业设计领域的风格和技巧，适合设计类创作',
    items: designItems
  },
  {
    id: 6,
    title: '艺术',
    subtitle: '传统和现代艺术风格，适合艺术类创作',
    items: artItems
  },
  {
    id: 7,
    title: '材质',
    subtitle: '不同材质的表现效果，适合材质渲染创作',
    items: materialItems
  }
]

export type ResponseItem = {
  name: string
  description: string
  filename: string
  alt: string
}

export type Feature = {
  id: number
  title: string
  description: string
  items: ResponseItem[]
}