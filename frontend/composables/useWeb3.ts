import { ref, computed } from 'vue'
import { ethers } from 'ethers'

export function useWeb3() {
  const provider = ref<ethers.BrowserProvider | null>(null)
  const signer = ref<ethers.JsonRpcSigner | null>(null)
  const address = ref<string | null>(null)
  const chainId = ref<number | null>(null)

  const isConnected = computed(() => !!address.value)

  const connect = async () => {
    if (!window.ethereum) {
      throw new Error('MetaMask not installed')
    }

    try {
      const browserProvider = new ethers.BrowserProvider(window.ethereum)
      const accounts = await browserProvider.send('eth_requestAccounts', [])
      
      provider.value = browserProvider
      signer.value = await browserProvider.getSigner()
      address.value = accounts[0]
      
      const network = await browserProvider.getNetwork()
      chainId.value = Number(network.chainId)

      // Listen for account changes
      window.ethereum.on('accountsChanged', handleAccountsChanged)
      window.ethereum.on('chainChanged', handleChainChanged)
    } catch (error) {
      console.error('Failed to connect:', error)
      throw error
    }
  }

  const handleAccountsChanged = (accounts: string[]) => {
    if (accounts.length === 0) {
      disconnect()
    } else {
      address.value = accounts[0]
    }
  }

  const handleChainChanged = (newChainId: string) => {
    chainId.value = Number(newChainId)
  }

  const disconnect = () => {
    provider.value = null
    signer.value = null
    address.value = null
    chainId.value = null
  }

  return {
    provider,
    signer,
    address,
    chainId,
    isConnected,
    connect,
    disconnect
  }
}