import { RefreshCw } from 'lucide-react'
import { Button } from '@/components/ui/button'

type DashboardHeaderProps = {
  onRefresh: () => void
}

export function DashboardHeader({ onRefresh }: DashboardHeaderProps) {
  return (
    <header className="mb-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight mb-2">
            Ad Insights Explorer
          </h1>
          <p className="text-lg text-muted-foreground">
            Analyze ad content and detect anomalies for fraud prevention
          </p>
        </div>
        <Button onClick={onRefresh} variant="outline">
          <RefreshCw className="h-4 w-4 mr-2" />
          Refresh
        </Button>
      </div>
    </header>
  )
}
