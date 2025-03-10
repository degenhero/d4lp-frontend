<template>
  <form @submit.prevent="handleSubmit" class="glass-effect p-8 rounded-xl max-w-xl mx-auto">
    <div class="space-y-6">
      <!-- Wallet Connection Status -->
      <div class="flex items-center justify-between p-4 bg-white/5 rounded-lg">
        <span class="text-gray-300">Wallet Status:</span>
        <div class="flex items-center gap-2">
          <span v-if="isConnected" class="text-green-400">Connected</span>
          <span v-else class="text-red-400">Not Connected</span>
          <button 
            @click="connectWallet" 
            v-if="!isConnected"
            class="px-4 py-2 bg-orange-500 rounded-lg hover:bg-orange-600 transition"
          >
            Connect Wallet
          </button>
        </div>
      </div>

      <!-- Email Input -->
      <div>
        <label class="block text-gray-300 mb-2">Email Address</label>
        <input 
          v-model="formData.email"
          type="email"
          class="w-full bg-white/10 border border-white/20 rounded-lg px-4 py-2 text-white focus:border-orange-500 focus:outline-none"
          placeholder="your@email.com"
          required
        />
      </div>

      <!-- Telegram Handle -->
      <div>
        <label class="block text-gray-300 mb-2">Telegram Handle</label>
        <input 
          v-model="formData.telegram"
          type="text"
          class="w-full bg-white/10 border border-white/20 rounded-lg px-4 py-2 text-white focus:border-orange-500 focus:outline-none"
          placeholder="@yourusername"
        />
      </div>

      <!-- Planned Contribution -->
      <div>
        <label class="block text-gray-300 mb-2">Planned Contribution (ETH)</label>
        <input 
          v-model="formData.plannedContribution"
          type="number"
          step="0.01"
          min="0.1"
          class="w-full bg-white/10 border border-white/20 rounded-lg px-4 py-2 text-white focus:border-orange-500 focus:outline-none"
          placeholder="0.00"
          required
        />
      </div>

      <!-- Submit Button -->
      <button 
        type="submit"
        :disabled="!isConnected || isLoading"
        class="w-full bg-gradient-to-r from-purple-500 to-orange-500 text-white py-3 rounded-lg font-semibold hover:opacity-90 transition flex items-center justify-center gap-2 disabled:opacity-50"
      >
        <span v-if="isLoading">
          <LoadingSpinner class="w-5 h-5" />
        </span>
        <span v-else>
          Apply for Whitelist
        </span>
      </button>

      <!-- Status Message -->
      <div v-if="statusMessage" :class="[
        'p-4 rounded-lg text-center',
        statusMessage.type === 'success' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'
      ]">
        {{ statusMessage.text }}
      </div>
    </div>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useWeb3 } from '@/composables/useWeb3'
import { ethers } from 'ethers'
import D4LWhitelistABI from '@/contracts/abis/D4LWhitelist.json'

const { connect, isConnected, signer, provider } = useWeb3()

const formData = ref({
  email: '',
  telegram: '',
  plannedContribution: ''
})

const isLoading = ref(false)
const statusMessage = ref(null)

const CONTRACT_ADDRESS = '0x...' // Add your deployed contract address

const connectWallet = async () => {
  try {
    await connect()
  } catch (error) {
    console.error('Failed to connect wallet:', error)
    statusMessage.value = {
      type: 'error',
      text: 'Failed to connect wallet. Please try again.'
    }
  }
}

const handleSubmit = async () => {
  if (!isConnected.value) {
    statusMessage.value = {
      type: 'error',
      text: 'Please connect your wallet first'
    }
    return
  }

  isLoading.value = true
  statusMessage.value = null

  try {
    const contract = new ethers.Contract(
      CONTRACT_ADDRESS,
      D4LWhitelistABI,
      signer.value
    )

    const tx = await contract.applyForWhitelist(
      formData.value.email,
      formData.value.telegram,
      ethers.parseEther(formData.value.plannedContribution.toString())
    )

    await tx.wait()

    statusMessage.value = {
      type: 'success',
      text: 'Application submitted successfully! Please wait for approval.'
    }

    // Reset form
    formData.value = {
      email: '',
      telegram: '',
      plannedContribution: ''
    }
  } catch (error) {
    console.error('Failed to submit application:', error)
    statusMessage.value = {
      type: 'error',
      text: 'Failed to submit application. Please try again.'
    }
  } finally {
    isLoading.value = false
  }
}
</script>