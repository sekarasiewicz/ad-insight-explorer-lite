import { ColorModeButton } from './components/ColorModeButton'
import { Dashboard } from './components/dashboard/Dashboard'

function App() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <ColorModeButton />
      <Dashboard />
    </div>
  )
}

export default App
