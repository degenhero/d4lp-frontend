<template>
  <section id="auction" class="relative py-24">
    <!-- Background with blur effect -->
    <div class="absolute inset-0 bg-black/40 backdrop-blur-xl"></div>
    
    <div class="container mx-auto px-6 relative z-10">
      <!-- Header Section -->
      <div class="text-center mb-16">
        <h2 class="text-5xl font-bold text-orange-500 mb-6">Dutch Auction Presale</h2>
        <p class="text-xl text-gray-300 max-w-2xl mx-auto">
          Our Dutch auction presale is designed for fair, market-driven token distribution. 
          <span class="text-orange-400 font-semibold">Get whitelisted</span> to secure your early access.
        </p>
      </div>

      <!-- Steps Grid -->
      <div class="grid md:grid-cols-3 gap-8 mb-16">
        <div class="glass-card p-6 text-left transform hover:scale-105 transition-transform duration-300">
          <div class="flex items-center mb-4">
            <div class="w-12 h-12 bg-orange-500/20 rounded-full flex items-center justify-center">
              <span class="text-2xl font-bold text-orange-500">1</span>
            </div>
            <h3 class="text-xl font-bold text-white ml-4">Prelaunch & Whitelisting</h3>
          </div>
          <p class="text-gray-300">
            Apply for whitelisting to secure your guaranteed slot for the presale. Early supporters get additional benefits.
          </p>
        </div>

        <div class="glass-card p-6 text-left transform hover:scale-105 transition-transform duration-300">
          <div class="flex items-center mb-4">
            <div class="w-12 h-12 bg-orange-500/20 rounded-full flex items-center justify-center">
              <span class="text-2xl font-bold text-orange-500">2</span>
            </div>
            <h3 class="text-xl font-bold text-white ml-4">Premium Start Price</h3>
          </div>
          <p class="text-gray-300">
            Auction begins at a higher price point, ensuring fair value discovery and preventing initial FOMO.
          </p>
        </div>

        <div class="glass-card p-6 text-left transform hover:scale-105 transition-transform duration-300">
          <div class="flex items-center mb-4">
            <div class="w-12 h-12 bg-orange-500/20 rounded-full flex items-center justify-center">
              <span class="text-2xl font-bold text-orange-500">3</span>
            </div>
            <h3 class="text-xl font-bold text-white ml-4">Dynamic Price Drop</h3>
          </div>
          <p class="text-gray-300">
            Price gradually decreases until reaching the reserve price or tokens are sold out.
          </p>
        </div>
      </div>

      <!-- Stats Section -->
      <div class="grid md:grid-cols-4 gap-6">
        <div class="glass-card p-6 text-center">
          <h4 class="text-orange-400 text-lg font-semibold mb-2">Starting Price</h4>
          <p class="text-3xl font-bold text-white">2.5 ETH</p>
        </div>

        <div class="glass-card p-6 text-center">
          <h4 class="text-orange-400 text-lg font-semibold mb-2">Reserve Price</h4>
          <p class="text-3xl font-bold text-white">0.5 ETH</p>
        </div>

        <div class="glass-card p-6 text-center">
          <h4 class="text-orange-400 text-lg font-semibold mb-2">Duration</h4>
          <p class="text-3xl font-bold text-white">48 hrs</p>
        </div>

        <div class="glass-card p-6 text-center">
          <h4 class="text-orange-400 text-lg font-semibold mb-2">Total Tokens</h4>
          <p class="text-3xl font-bold text-white">1,000,000</p>
        </div>
      </div>

      <!-- CTA Button -->
      <div class="text-center mt-16">
        <button class="bg-orange-500 hover:bg-orange-600 text-white px-8 py-4 rounded-lg font-bold text-lg transform hover:scale-105 transition-all duration-300 shadow-lg">
          Get Whitelisted Now
        </button>
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
  
