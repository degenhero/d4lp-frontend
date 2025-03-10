<template>
  <section class="container mx-auto py-16 px-6" id="features">
    <h2 class="text-4xl font-bold text-center text-white mb-12">🔥 Platform Features</h2>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <FeatureContent 
        title="Decentralized Trading" 
        text="Limit orders, hybrid AMM, & order book mechanics for next-gen trading."
        icon="trending"
      />
      <FeatureContent 
        title="NFT-Backed Liquidity" 
        text="Tradeable LP positions, collateralization, and composable DeFi NFTs."
        icon="layers"
      />
      <FeatureContent 
        title="Risk Management" 
        text="Insurance pools, flash loan protection, and AI-driven risk analysis."
        icon="shield"
      />
      <FeatureContent 
        title="AI-Driven Analytics" 
        text="Real-time market sentiment tracking and automated trading insights."
        icon="ai"
      />
      <FeatureContent 
        title="Privacy-Powered Trading" 
        text="Zero-knowledge proofs and anti-front-running measures."
        icon="privacy"
      />
      <FeatureContent 
        title="Social Trading & Influence" 
        text="Copy trading, strategy sharing, and trader rankings."
        icon="social"
      />
    </div>
  </section>
</template>

<script setup>
import FeatureContent from "@/components/FeatureContent.vue";
</script>
