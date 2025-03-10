<template>
    <div class="absolute top-24 right-10 w-72 bg-gray-900/90 backdrop-blur-md rounded-lg p-4 shadow-lg floating-panel border border-orange-500/40">
      <h3 class="text-lg font-semibold text-orange-500 flex items-center">
        🔥 Trending Auction
      </h3>
      <p class="text-gray-300 mt-1 text-sm">Highest Bid:</p>
      <p class="text-white text-2xl font-bold">${{ highestBid }}</p>
      <div class="mt-2 flex items-center justify-between text-gray-300 text-xs">
        <span>Top Bidder:</span>
        <span class="text-white font-semibold">{{ topBidder }}</span>
      </div>
      <div class="mt-4">
        <p class="text-gray-400 text-sm">Recent Bids:</p>
        <ul class="mt-2 text-gray-300 text-xs space-y-1">
          <li v-for="(bid, index) in recentBids" :key="index" class="flex justify-between">
            <span>{{ bid.user }}</span>
            <span class="text-white font-semibold">${{ bid.amount }}</span>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import gsap from 'gsap'
  
  const highestBid = ref("12,500")
  const topBidder = ref("0x9A7...F3C")
  const recentBids = ref([
    { user: "0xA3C...B1D", amount: "12,200" },
    { user: "0xF8E...91A", amount: "11,800" },
    { user: "0xD42...7F3", amount: "11,500" }
  ])
  
  onMounted(() => {
    gsap.to(".floating-panel", {
      y: 8,
      repeat: -1,
      yoyo: true,
      duration: 2.5,
      ease: "power1.inOut"
    })
  })
  </script>
  
  <style scoped>
  .floating-panel {
    animation: float 3s ease-in-out infinite;
  }
  @keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(10px); }
    100% { transform: translateY(0px); }
  }
  </style>
  