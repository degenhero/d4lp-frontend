<template>
    <div 
      class="glass-card p-6 rounded-xl shadow-lg backdrop-blur-lg bg-white/10 border border-white/10 relative">
      <slot />
    </div>
  </template>
  
  <style scoped>
  .glass-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    border-radius: 16px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    transition: all 0.3s ease-in-out;
  }
  
  .glass-card:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-5px);
  }
  </style>
  