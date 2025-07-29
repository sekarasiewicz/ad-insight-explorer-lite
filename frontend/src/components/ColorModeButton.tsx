import { Moon, Sun } from 'lucide-react'
import { useEffect, useState } from 'react'
import type { Theme, ThemeState } from '@/types'
import { Button } from './ui/button'

// Simple theme storage using localStorage
const themeStorage = {
  get: (): Theme | null => {
    try {
      const stored = localStorage.getItem('theme')
      return (stored as Theme) || null
    } catch {
      return null
    }
  },
  set: (theme: Theme): void => {
    try {
      localStorage.setItem('theme', theme)
    } catch {
      // Ignore localStorage errors
    }
  },
}

export function ColorModeButton() {
  const [themeState, setThemeState] = useState<ThemeState>({
    theme: 'system',
    isDark: false,
  })

  useEffect(() => {
    // Check if user has a saved preference
    const savedTheme = themeStorage.get()
    const prefersDark = window.matchMedia(
      '(prefers-color-scheme: dark)'
    ).matches

    const currentTheme: Theme = savedTheme || 'system'
    const isDark =
      currentTheme === 'dark' || (currentTheme === 'system' && prefersDark)

    setThemeState({ theme: currentTheme, isDark })

    if (isDark) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
  }, [])

  const toggleColorMode = (): void => {
    const newTheme: Theme = themeState.isDark ? 'light' : 'dark'
    const newIsDark = !themeState.isDark

    setThemeState({ theme: newTheme, isDark: newIsDark })

    if (newIsDark) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }

    themeStorage.set(newTheme)
  }

  return (
    <Button
      type="button"
      variant="ghost"
      size="icon"
      onClick={toggleColorMode}
      className="fixed top-4 right-4 z-50"
      aria-label={
        themeState.isDark ? 'Switch to light mode' : 'Switch to dark mode'
      }
    >
      {themeState.isDark ? <Sun size={20} /> : <Moon size={20} />}
    </Button>
  )
}
