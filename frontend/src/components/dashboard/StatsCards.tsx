import { AlertTriangle, BarChart3 } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import type { AnomaliesResponse, SummaryResponse } from '@/types'

type StatsCardsProps = {
  summary: SummaryResponse | null
  anomalies: AnomaliesResponse | null
}

export function StatsCards({ summary, anomalies }: StatsCardsProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium">Total Posts</CardTitle>
          <BarChart3 className="h-4 w-4 text-muted-foreground" />
        </CardHeader>
        <CardContent>
          <div className="text-2xl font-bold">{summary?.totalPosts || 0}</div>
          <p className="text-xs text-muted-foreground">
            Analyzed from JSONPlaceholder API
          </p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium">Total Users</CardTitle>
          <BarChart3 className="h-4 w-4 text-muted-foreground" />
        </CardHeader>
        <CardContent>
          <div className="text-2xl font-bold">{summary?.totalUsers || 0}</div>
          <p className="text-xs text-muted-foreground">
            Unique users with posts
          </p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium">
            Anomalies Detected
          </CardTitle>
          <AlertTriangle className="h-4 w-4 text-muted-foreground" />
        </CardHeader>
        <CardContent>
          <div className="text-2xl font-bold">{anomalies?.total || 0}</div>
          <p className="text-xs text-muted-foreground">
            Suspicious posts flagged
          </p>
        </CardContent>
      </Card>
    </div>
  )
}
