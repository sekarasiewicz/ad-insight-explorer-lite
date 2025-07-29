import type { AnomaliesResponse, PostsResponse, SummaryResponse } from '@/types'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export const ApiService = {
  async getPosts(limit?: number): Promise<PostsResponse> {
    try {
      const params = new URLSearchParams()
      if (limit) {
        params.append('limit', limit.toString())
      }

      const url = `${API_BASE_URL}/api/posts/?${params.toString()}`
      const response = await fetch(url)

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }

      const data: PostsResponse = await response.json()
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

  async getPostsByUser(userId: number): Promise<PostsResponse> {
    try {
      const response = await fetch(`${API_BASE_URL}/api/posts/${userId}`)

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }

      const data: PostsResponse = await response.json()
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

  async getAnomalies(
    limit?: number,
    userId?: number
  ): Promise<AnomaliesResponse> {
    try {
      const params = new URLSearchParams()
      if (limit) {
        params.append('limit', limit.toString())
      }
      if (userId) {
        params.append('user_id', userId.toString())
      }

      const url = `${API_BASE_URL}/api/anomalies/?${params.toString()}`
      const response = await fetch(url)

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }

      const data: AnomaliesResponse = await response.json()
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

  async getSummary(
    limit?: number,
    topUsers: number = 3,
    topWords: number = 20
  ): Promise<SummaryResponse> {
    try {
      const params = new URLSearchParams()
      if (limit) {
        params.append('limit', limit.toString())
      }
      params.append('top_users', topUsers.toString())
      params.append('top_words', topWords.toString())

      const url = `${API_BASE_URL}/api/summary/?${params.toString()}`
      const response = await fetch(url)

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`)
      }

      const data: SummaryResponse = await response.json()
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
