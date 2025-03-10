<template>
  <section class="relative flex flex-col items-center justify-center h-screen text-center px-6">

    <!-- Background -->
    <div class="absolute inset-0 bg-cover bg-center opacity-40" style="background-image: url('/bg1.jpg');"></div>
    <div class="absolute inset-0 bg-gradient-to-b from-black/60 to-black/90 backdrop-blur-xl"></div>

    <!-- ⏳ Countdown - Moved Closer to the Top -->
    <div class="relative z-10 max-w-3xl mt-[-160px]">
      <div class="flex justify-center space-x-4 bg-white/10 backdrop-blur-xl p-6 rounded-xl shadow-lg border border-white/20">
        <div v-for="(value, label) in countdown" :key="label" class="text-center">
          <div class="text-6xl md:text-8xl font-bold text-orange-400 drop-shadow-lg animate-pulse">
            {{ value }}
          </div>
          <div class="uppercase text-sm md:text-lg text-gray-300 tracking-widest">
            {{ label }}
          </div>
        </div>
      </div>
    </div>

    <!-- ✨ Main Headline -->
    <div class="relative z-10 max-w-3xl mt-12">
      <h1 class="text-5xl font-bold text-white">
        Welcome to <span class="text-orange-500">D4L</span>
      </h1>
      <p class="mt-4 text-lg text-gray-300 leading-relaxed">
        The most innovative <span class="font-semibold text-orange-400">DeFi launchpad</span>, powered by  
        <span class="font-semibold text-orange-400">HydraCurve™ AMM</span>, <span class="font-semibold text-orange-400">AI-driven risk management</span>,  
        and <span class="font-semibold text-orange-400">NFT-backed liquidity.</span>
      </p>

      <!-- 📢 Call-to-Action Buttons -->
      <div class="mt-8 flex flex-wrap justify-center gap-6">
        <!-- CTA 1: Get Whitelisted -->
        <NuxtLink 
          to="/whitelist"
          class="px-6 py-3 bg-gradient-to-r from-purple-500 to-orange-500 hover:scale-105 text-white font-semibold rounded-lg shadow-lg transition flex items-center gap-2"
        >
          <UserPlus class="w-6 h-6" /> BE A VIP – Get Whitelisted
        </NuxtLink>

        <!-- CTA 2: Read Whitepaper -->
        <NuxtLink 
          to="/whitepaper"
          class="px-6 py-3 border border-orange-500 hover:bg-orange-500 hover:text-white text-orange-500 font-semibold rounded-lg shadow-lg transition flex items-center gap-2"
        >
          <FileText class="w-6 h-6" /> Read the Whitepaper
        </NuxtLink>
      </div>
    </div>

    <!-- 🦝 Raccoon (Floating Effect) -->
    <div ref="raccoonContainer" class="absolute bottom-0 left-1/2 transform -translate-x-1/2">
      <img 
        ref="raccoon"
        src="/character.png"
        class="fixed bottom-0 left-1/2 transform -translate-x-1/2 w-[40vw] max-w-[800px] min-w-[400px] drop-shadow-xl"
      />
    </div>

  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { UserPlus, FileText } from 'lucide-vue-next'

// Countdown Timer
const countdown = ref({
  DAYS: "00",
  HOURS: "00",
  MIN: "00",
  SEC: "00"
})

// Set Auction Date
const auctionDate = new Date("2025-03-21T00:00:00Z").getTime()

const updateCountdown = () => {
  const now = new Date().getTime()
  const timeLeft = auctionDate - now

  if (timeLeft > 0) {
    countdown.value.DAYS = String(Math.floor(timeLeft / (1000 * 60 * 60 * 24))).padStart(2, "0")
    countdown.value.HOURS = String(Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))).padStart(2, "0")
    countdown.value.MIN = String(Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60))).padStart(2, "0")
    countdown.value.SEC = String(Math.floor((timeLeft % (1000 * 60)) / 1000)).padStart(2, "0")
  }
}

// GSAP Scroll + Floating Animation
const raccoon = ref(null)
const raccoonContainer = ref(null)
const { $gsap } = useNuxtApp()

onMounted(() => {
  updateCountdown()
  setInterval(updateCountdown, 1000)

  // 🦝 Smooth Fade-in Animation
  $gsap.fromTo(raccoon.value, 
    { opacity: 0, scale: 0.8, y: -30 }, 
    { opacity: 1, scale: 1, y: 0, duration: 1.8, ease: "elastic.out(1, 0.5)" }
  )

  // 🎭 Subtle Raccoon Head Tilting
  $gsap.to(raccoon.value, {
    rotation: 2 + Math.random() * 3, // Random slight tilts
    duration: 3,
    repeat: -1,
    yoyo: true,
    ease: "sine.inOut",
    delay: Math.random() * 2, // Small delay to look organic
  });

  // 📜 Scroll Effect for Smooth Floating
  window.addEventListener("scroll", () => {
    let scrollY = window.scrollY;
    raccoonContainer.value.style.transform = `translateY(${scrollY * 0.1}px)`; 
  })
})
</script>

<style scoped>
@keyframes float {
  0% { transform: translateY(0); }
  50% { transform: translateY(10px); }
  100% { transform: translateY(0); }
}
</style>
