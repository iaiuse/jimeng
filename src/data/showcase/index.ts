import { imageItems } from './image'
import { designItems } from './design'
import { artItems } from './art'

export const features = [
  {
    id: 1,
    title: '影像',
    subtitle: '专业摄影和电影镜头语言，适合影视风格创作',
    items: imageItems
  },
  {
    id: 2,
    title: '艺术',
    subtitle: '传统和现代艺术风格，适合艺术类创作',
    items: artItems
  },
  {
    id: 3,
    title: '设计',
    subtitle: '专业设计领域的风格和技巧，适合设计类创作',
    items: designItems
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