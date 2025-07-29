// API Response Types

// Post-related types
export type Post = {
  userId: number
  id: number
  title: string
  body: string
}

export type PostsResponse = {
  posts: Post[]
  total: number
}

// Anomaly-related types
export type Anomaly = {
  userId: number
  id: number
  title: string
  reason: string
  details?: string
}

export type AnomaliesResponse = {
  anomalies: Anomaly[]
  total: number
  summary: {
    total_anomalies: number
    by_reason: Record<string, number>
    by_user: Record<string, number>
    unique_users_affected: number
  }
}

// Summary-related types
export type UserSummary = {
  userId: number
  uniqueWordCount: number
  totalPosts: number
  uniqueWords: string[]
}

export type WordFrequency = {
  word: string
  count: number
}

export type SummaryResponse = {
  topUsers: UserSummary[]
  mostFrequentWords: WordFrequency[]
  totalPosts: number
  totalUsers: number
}

// Error Types
export type ErrorResponse = {
  error: string
  message: string
}

export type ApiError = {
  detail: ErrorResponse
}

// Theme Types
export type Theme = 'light' | 'dark' | 'system'

export type ThemeState = {
  theme: Theme
  isDark: boolean
}

// Loading State Types
export type LoadingState = 'idle' | 'loading' | 'success' | 'error'

// Component Props Types
export type BaseComponentProps = {
  className?: string
  'data-testid'?: string
}

export type ButtonVariant =
  | 'default'
  | 'destructive'
  | 'outline'
  | 'secondary'
  | 'ghost'
  | 'link'

export type ButtonSize = 'default' | 'sm' | 'lg' | 'icon'

// Utility Types
export type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>
export type RequiredFields<T, K extends keyof T> = T & Required<Pick<T, K>>

// Event Handler Types
export type EventHandler<T = Event> = (event: T) => void
export type AsyncEventHandler<T = Event> = (event: T) => Promise<void>

// Storage Types
export type StorageKey = 'theme' | 'userPreferences'
export type StorageValue = string | number | boolean | object
