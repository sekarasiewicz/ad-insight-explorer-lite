import { useCallback, useEffect, useState } from 'react'
import { ColorModeButton } from './components/ColorModeButton'
import { Button } from './components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from './components/ui/card'

function App() {
  const [message, setMessage] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(false)
  const [error, setError] = useState<string | null>(null)

  const fetchHelloWorld = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await fetch('/api/hello')
      if (!response.ok) {
        throw new Error('Failed to fetch hello world message')
      }
      const data = await response.json()
      setMessage(data.message)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchHelloWorld()
  }, [fetchHelloWorld])

  return (
    <div className="min-h-screen bg-background text-foreground">
      <ColorModeButton />
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold tracking-tight mb-2">
            FastAPI React Kit
          </h1>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            A simple template for FastAPI and React projects
          </p>
        </header>

        <div className="flex justify-center">
          <Card className="w-full max-w-md">
            <CardHeader>
              <CardTitle className="text-center">Hello World</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              {loading && (
                <p className="text-center text-muted-foreground">Loading...</p>
              )}

              {error && <p className="text-center text-destructive">{error}</p>}

              {message && (
                <p className="text-center text-2xl font-semibold">{message}</p>
              )}

              <div className="flex justify-center">
                <Button onClick={fetchHelloWorld} disabled={loading}>
                  {loading ? 'Loading...' : 'Refresh Message'}
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}

export default App
