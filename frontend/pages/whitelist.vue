<template>
  <div class="min-h-screen py-24">
    <div class="container mx-auto px-4">
      <h1 class="text-4xl font-bold text-center text-white mb-8">
        Apply for Whitelist
      </h1>
      <p class="text-gray-300 text-center max-w-2xl mx-auto mb-12">
        Join our exclusive presale by applying for the whitelist. Early participants will receive special benefits and guaranteed allocation in our Dutch auction.
      </p>
      <WhitelistForm />
    </div>
  </div>
</template>

<script setup>
import WhitelistForm from '@/components/WhitelistForm.vue'
</script>