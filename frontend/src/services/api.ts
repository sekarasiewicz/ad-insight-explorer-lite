import type { HelloResponse } from '@/types'

const API_BASE_URL = '/api'

export const ApiService = {
  async getHelloWorld(): Promise<HelloResponse> {
    try {
      const response = await fetch(`${API_BASE_URL}/hello`)

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }

      const data: HelloResponse = await response.json()
      return data
    } catch (error) {
      if (error instanceof TypeError && error.message.includes('fetch')) {
        throw new Error('Network error: Unable to connect to the server')
      }

      throw error instanceof Error
        ? error
        : new Error('An unexpected error occurred')
    }
  },
}
