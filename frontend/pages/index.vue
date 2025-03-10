<template>
  <div class="flex flex-col">
    <!-- Hero Section -->
    <HeroSection class="min-h-screen" />
    
    <!-- Stats Banner -->
    <div class="bg-gradient-to-r from-purple-900/50 to-orange-900/50 py-12 backdrop-blur-xl">
      <div class="container mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
        <StatCard 
          number="$12M+" 
          label="Total Value Locked" 
          icon="CircleDollarSign"
        />
        <StatCard 
          number="50k+" 
          label="Active Users" 
          icon="Users"
        />
        <StatCard 
          number="99.9%" 
          label="Uptime" 
          icon="Activity"
        />
        <StatCard 
          number="24/7" 
          label="Support" 
          icon="Headphones"
        />
      </div>
    </div>

    <!-- About Section with Grid Layout -->
    <AboutSection class="py-24 section-gradient">
      <template #features>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-12">
          <FeatureCard
            title="HydraCurve™ AMM"
            description="Advanced automated market maker with dynamic pricing and reduced slippage"
            icon="TrendingUp"
          />
          <FeatureCard
            title="NFT-Backed Liquidity"
            description="Tokenized LP positions with built-in yield optimization"
            icon="Image"
          />
          <FeatureCard
            title="AI Risk Management"
            description="Real-time risk assessment and automated portfolio rebalancing"
            icon="Brain"
          />
          <FeatureCard
            title="Cross-Chain Bridge"
            description="Seamless asset transfer across multiple blockchains"
            icon="Bridge"
          />
        </div>
      </template>
    </AboutSection>

    <!-- Auction Section -->
    <AuctionSection />

    <!-- RoadMap Section -->
    <RoadMapSection />

    <!-- Features Section -->
    <FeaturesSection class="py-24 section-gradient">
      <template #demo>
        <div class="mt-12 relative">
          <DemoTerminal />
        </div>
      </template>
    </FeaturesSection>

    <!-- Community Section -->
    <CommunitySection class="py-24 bg-black/30 backdrop-blur-xl">
      <template #testimonials>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-12">
          <TestimonialCard
            name="Alex Thompson"
            role="DeFi Trader"
            quote="The HydraCurve™ AMM is a game-changer for liquidity provision."
            avatar="/avatars/alex.jpg"
          />
          <TestimonialCard
            name="Sarah Chen"
            role="Protocol Developer"
            quote="Best-in-class security features and innovative NFT integration."
            avatar="/avatars/sarah.jpg"
          />
          <TestimonialCard
            name="Michael Roberts"
            role="Crypto Analyst"
            quote="The AI risk management tools have revolutionized my trading strategy."
            avatar="/avatars/michael.jpg"
          />
        </div>
      </template>
    </CommunitySection>

    <!-- Contact Section -->
    <ContactSection class="py-24 section-gradient">
      <template #form>
        <ContactForm class="max-w-xl mx-auto mt-12" />
      </template>
    </ContactSection>
  </div>
</template>

<script setup>
import { CircleDollarSign, Users, Activity, Headphones, TrendingUp, Image, Brain, Bridge } from 'lucide-vue-next'
import HeroSection from '@/components/HeroSection.vue'
import AboutSection from '@/components/AboutSection.vue'
import AuctionSection from '@/components/AuctionSection.vue'
import FeaturesSection from '@/components/FeaturesSection.vue'
import CommunitySection from '@/components/CommunitySection.vue'
import WhitepaperSection from '@/components/WhitepaperSection.vue'
import ContactSection from '@/components/ContactSection.vue'
import StatCard from '@/components/StatCard.vue'
import FeatureCard from '@/components/FeatureCard.vue'
import AuctionStat from '@/components/AuctionStat.vue'
import DemoTerminal from '@/components/DemoTerminal.vue'
import TestimonialCard from '@/components/TestimonialCard.vue'
import DocumentPreview from '@/components/DocumentPreview.vue'
import ContactForm from '@/components/ContactForm.vue'
import RoadMapSection from '@/components/RoadMapSection.vue'
</script>

<style scoped>
.section-gradient {
  @apply bg-gradient-to-b from-black/30 to-black/50 backdrop-blur-xl;
}

.section-transition {
  @apply transition-all duration-300 ease-in-out;
}
</style>
