<template>
  <section id="model-highlights">
    <div class="section-header">
      <div class="section-number">1</div>
      <h2 class="section-title">模型亮点</h2>
    </div>
    <div class="feature-grid">
      <div class="feature-card">
        <h3><span>真实:</span> 去虚饰、以假乱真</h3>
        <p>3.0模型能够精准还原真实细节和质感，去除AI图像常见的虚饰感和假脸感。</p>
        <div class="feature-examples">
          <strong>示例:</strong> 原画真实、情绪真实，支持去伪饰，AI油腻感
        </div>
      </div>
      <div class="feature-card">
        <h3><span>高清:</span> 默认1k，可支持2K</h3>
        <p>图像渲染质量和细节构成更精准，2k时画面结构更稳定，支持超高清输出。</p>
        <div class="feature-examples">
          <strong>示例:</strong> 高分辨率，清晰度提升，细节丰富，纹理清晰
        </div>
      </div>
      <div class="feature-card">
        <h3><span>专业:</span> 专业级的画面效果</h3>
        <p>提供专业的商业设计质量，满足各种商业创意和设计需求。</p>
        <div class="feature-examples">
          <strong>示例:</strong> 专业摄影效果，广告级质感，商业品质输出
        </div>
      </div>
      <div class="feature-card">
        <h3><span>文字准确:</span> 更准确的字体响应</h3>
        <p>更准确的字体响应与排版设计，支持不同字体，专业的设计排版。</p>
        <div class="feature-examples">
          <strong>示例:</strong> 排版美观，字体清晰，多语言支持，设计感强
        </div>
      </div>
    </div>
  </section>
</template>

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
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 35px;
}

.feature-card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  padding: 30px;
  transition: transform 0.2s, box-shadow 0.2s;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.feature-card h3 {
  font-size: 1.5rem;
  margin-bottom: 15px;
  color: #333;
  display: flex;
  align-items: center;
}

.feature-card h3 span {
  color: #0066cc;
  margin-right: 10px;
  font-weight: 600;
}

.feature-card p {
  color: #666;
  margin-bottom: 20px;
  font-size: 1.1rem;
}

.feature-examples {
  margin-top: 20px;
  background-color: #f5f9ff;
  padding: 15px;
  border-radius: 6px;
  font-size: 1rem;
}

@media (max-width: 960px) {
  .feature-grid {
    grid-template-columns: 1fr;
  }
}
</style> 