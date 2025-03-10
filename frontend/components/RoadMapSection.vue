<template>
  <section class="relative py-24 overflow-hidden" id="roadmap">
    <!-- Background with blur effect -->
    <div class="absolute inset-0 bg-black/40 backdrop-blur-xl"></div>
    
    <div class="container mx-auto px-6 relative z-10">
      <!-- Header -->
      <div class="text-center mb-16">
        <h2 class="text-5xl font-bold text-orange-500 mb-6">Roadmap</h2>
        <p class="text-xl text-gray-300 max-w-2xl mx-auto">
          Our journey to revolutionize DeFi through strategic milestones and continuous innovation
        </p>
      </div>

      <!-- Timeline -->
      <div class="relative">
        <!-- Timeline Line -->
        <div class="absolute left-1/2 transform -translate-x-1/2 h-full w-1 bg-orange-500/30"></div>

        <!-- Timeline Items -->
        <div class="space-y-24">
          <!-- Q1 2024 -->
          <div class="relative">
            <div class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2">
              <div class="w-6 h-6 bg-orange-500 rounded-full"></div>
            </div>
            <div class="w-1/2 pr-16 text-right md:float-left">
              <div class="glass-card p-6 hover:scale-105 transition-transform duration-300">
                <h3 class="text-2xl font-bold text-orange-400 mb-3">Q1 2024</h3>
                <ul class="text-gray-300 space-y-2">
                  <li>🚀 Platform Launch</li>
                  <li>💎 Initial Token Distribution</li>
                  <li>🔄 HydraCurve™ AMM Beta</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Q2 2024 -->
          <div class="relative">
            <div class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2">
              <div class="w-6 h-6 bg-orange-500 rounded-full"></div>
            </div>
            <div class="w-1/2 pl-16 md:float-right">
              <div class="glass-card p-6 hover:scale-105 transition-transform duration-300">
                <h3 class="text-2xl font-bold text-orange-400 mb-3">Q2 2024</h3>
                <ul class="text-gray-300 space-y-2">
                  <li>🎨 NFT-Backed Liquidity Pools</li>
                  <li>🤖 AI Risk Management Suite</li>
                  <li>🌉 Cross-Chain Bridge Integration</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Q3 2024 -->
          <div class="relative">
            <div class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2">
              <div class="w-6 h-6 bg-orange-500 rounded-full"></div>
            </div>
            <div class="w-1/2 pr-16 text-right md:float-left">
              <div class="glass-card p-6 hover:scale-105 transition-transform duration-300">
                <h3 class="text-2xl font-bold text-orange-400 mb-3">Q3 2024</h3>
                <ul class="text-gray-300 space-y-2">
                  <li>📊 Advanced Analytics Dashboard</li>
                  <li>🔐 Institutional Features</li>
                  <li>🤝 Strategic Partnerships</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Q4 2024 -->
          <div class="relative">
            <div class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2">
              <div class="w-6 h-6 bg-orange-500 rounded-full"></div>
            </div>
            <div class="w-1/2 pl-16 md:float-right">
              <div class="glass-card p-6 hover:scale-105 transition-transform duration-300">
                <h3 class="text-2xl font-bold text-orange-400 mb-3">Q4 2024</h3>
                <ul class="text-gray-300 space-y-2">
                  <li>🌟 Mobile App Launch</li>
                  <li>💫 DAO Governance</li>
                  <li>🎮 Gamification Features</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Future Vision -->
      <div class="mt-24 text-center">
        <div class="glass-card p-8 max-w-2xl mx-auto">
          <h3 class="text-2xl font-bold text-orange-400 mb-4">Future Vision</h3>
          <p class="text-gray-300">
            Beyond 2024, we're committed to expanding the D4L ecosystem through innovative DeFi products, 
            enhanced cross-chain capabilities, and deeper integration with traditional finance.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.glass-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
}

.glass-card:hover {
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}
</style>