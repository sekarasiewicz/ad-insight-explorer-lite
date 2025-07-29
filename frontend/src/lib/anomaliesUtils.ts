import type { Anomaly } from '@/types'

type SortColumn = 'id' | 'userId' | 'title' | 'reason'
type SortOrder = 'asc' | 'desc'

export function getReasonLabel(reason: string): string {
  switch (reason) {
    case 'short_title':
      return 'Short Title'
    case 'duplicate_title':
      return 'Duplicate Title'
    case 'bot_like_behavior':
      return 'Bot-like Behavior'
    default:
      return reason
  }
}

export function filterAndSortAnomalies(
  anomalies: Anomaly[],
  searchTerm: string,
  sortBy: SortColumn,
  sortOrder: SortOrder
): Anomaly[] {
  let filtered = anomalies

  // Filter by search term
  if (searchTerm) {
    const searchLower = searchTerm.toLowerCase()
    filtered = filtered.filter((anomaly) => {
      // Check title
      if (anomaly.title.toLowerCase().includes(searchLower)) return true

      // Check reason code and label
      if (anomaly.reason.toLowerCase().includes(searchLower)) return true
      if (getReasonLabel(anomaly.reason).toLowerCase().includes(searchLower))
        return true

      // Check user ID (handle "User 1", "user 1", "1", etc.)
      const userText = `user ${anomaly.userId}`
      if (userText.includes(searchLower)) return true
      if (anomaly.userId.toString().includes(searchLower)) return true

      // Check post ID
      if (anomaly.id.toString().includes(searchLower)) return true

      return false
    })
  }

  // Sort
  filtered.sort((a, b) => {
    let aValue: string | number
    let bValue: string | number

    switch (sortBy) {
      case 'id':
        aValue = a.id
        bValue = b.id
        break
      case 'userId':
        aValue = a.userId
        bValue = b.userId
        break
      case 'title':
        aValue = a.title
        bValue = b.title
        break
      case 'reason':
        aValue = a.reason
        bValue = b.reason
        break
      default:
        aValue = a.id
        bValue = b.id
    }

    if (sortOrder === 'asc') {
      return aValue > bValue ? 1 : -1
    } else {
      return aValue < bValue ? 1 : -1
    }
  })

  return filtered
}
