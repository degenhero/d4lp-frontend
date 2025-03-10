<script setup>
import { TrendingUp, Layers, ShieldCheck, Cpu, EyeOff, Share2, Wand, CircleDollarSign } from "lucide-vue-next";

defineProps({
  title: String,
  text: String,
  icon: String
});

const icons = {
  trending: TrendingUp,
  layers: Layers,
  shield: ShieldCheck,
  ai: Cpu,
  privacy: EyeOff,
  social: Share2,
  magic: Wand,
  finance: CircleDollarSign
};

</script>

<template>
  <GlassCard class="flex flex-col items-center text-center p-6">
    <component :is="icons[icon]" class="w-12 h-12 text-orange-500" />
    <h3 class="text-xl font-semibold text-white mt-4">{{ title }}</h3>
    <p class="text-gray-300 text-sm">{{ text }}</p>
  </GlassCard>
</template>
