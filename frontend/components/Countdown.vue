<template>
    <div class="relative mt-6 flex space-x-4 text-4xl font-mono mt-12 top-12 pt-12">
      <div class="countdown-box">
        <span>{{ countdown.days }}</span><span class="countdown-label">Days</span>
      </div>
      <div class="countdown-box">
        <span>{{ countdown.hours }}</span><span class="countdown-label">Hours</span>
      </div>
      <div class="countdown-box">
        <span>{{ countdown.minutes }}</span><span class="countdown-label">Min</span>
      </div>
      <div class="countdown-box">
        <span>{{ countdown.seconds }}</span><span class="countdown-label">Sec</span>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const countdown = ref({
    days: "00",
    hours: "00",
    minutes: "00",
    seconds: "00"
  })
  
  const auctionDate = new Date("2025-03-15T00:00:00Z").getTime()
  
  const updateCountdown = () => {
    const now = new Date().getTime()
    const timeLeft = auctionDate - now
    if (timeLeft > 0) {
      countdown.value.days = String(Math.floor(timeLeft / (1000 * 60 * 60 * 24))).padStart(2, "0")
      countdown.value.hours = String(Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))).padStart(2, "0")
      countdown.value.minutes = String(Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60))).padStart(2, "0")
      countdown.value.seconds = String(Math.floor((timeLeft % (1000 * 60)) / 1000)).padStart(2, "0")
    }
  }
  
  onMounted(() => {
    updateCountdown()
    setInterval(updateCountdown, 1000)
  })
  </script>
  
  <style scoped>
  .countdown-box {
    @apply flex flex-col items-center justify-center bg-gray-900 rounded-lg px-6 py-4 text-center text-white shadow-md;
    border: 2px solid rgba(255, 165, 0, 0.8);
    box-shadow: 0px 0px 16px rgba(255, 165, 0, 0.5);
    min-width: 90px;
  }
  .countdown-label {
    @apply text-sm font-semibold text-gray-300 uppercase tracking-wide mt-1;
  }
  </style>
  