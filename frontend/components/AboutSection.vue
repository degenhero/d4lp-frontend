<template>
  <section class="relative flex items-center justify-center min-h-screen px-6" id="about">
    <!-- Dark Overlay for Contrast -->
    <div class="absolute inset-0 bg-black/50 backdrop-blur-lg"></div>

    <GlassCard class="relative max-w-3xl mx-auto text-center text-white py-12 px-8 shadow-lg">
      <h2 class="text-4xl font-bold mb-4 text-orange-500">
        What is D4L? 🦊
      </h2>
      
      <p class="text-lg text-gray-300 leading-relaxed">
        <strong>D4L</strong> is a <strong>revolutionary DeFi platform</strong> designed to blend 
        <strong>advanced trading, automated strategies, and NFT-backed liquidity</strong> 
        with a <em>seamless user experience</em>. 
        Our mission? <strong>Redefine decentralized finance</strong> with a system that's 
        <span class="text-orange-400">powerful, fair, and easy to use.</span>
      </p>
      
      <p class="text-lg text-gray-300 mt-4">
        With <strong>HydraCurve™ AMM, Social Trading, AI-powered analytics,</strong> 
        and <strong>risk management tools</strong>, we’re making DeFi 
        <span class="text-orange-400">smarter, safer, and more rewarding.</span>
      </p>

      <!-- Call to Action -->
      <div class="mt-6">
        <NuxtLink to="#features" 
          class="px-6 py-3 bg-orange-500 hover:bg-orange-600 text-white rounded-lg shadow-lg transition flex items-center justify-center gap-2">
          <TrendingUp class="w-5 h-5" /> Explore Features
        </NuxtLink>
      </div>
    </GlassCard>
  </section>
</template>

<script setup>
import GlassCard from "@/components/GlassCard.vue";
import { TrendingUp } from "lucide-vue-next";
</script>
