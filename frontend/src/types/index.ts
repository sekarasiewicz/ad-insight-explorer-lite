// API Response Types
export type HelloResponse = {
  message: string
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
