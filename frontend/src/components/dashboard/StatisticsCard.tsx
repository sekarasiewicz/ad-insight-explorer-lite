import { Users } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import type { SummaryResponse } from '@/types'

type StatisticsCardProps = {
  summary: SummaryResponse
}

export function StatisticsCard({ summary }: StatisticsCardProps) {
  const totalUniqueWords = summary.mostFrequentWords.reduce(
    (sum, word) => sum + word.count,
    0
  )

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Users className="h-5 w-5" />
          <span>Statistics</span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          <div className="flex justify-between items-center">
            <span className="text-sm">Total Posts Analyzed</span>
            <span className="font-bold">{summary.totalPosts}</span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-sm">Unique Users</span>
            <span className="font-bold">{summary.totalUsers}</span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-sm">Average Posts per User</span>
            <span className="font-bold">
              {summary.totalUsers > 0
                ? Math.round(summary.totalPosts / summary.totalUsers)
                : 0}
            </span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-sm">Total Unique Words</span>
            <span className="font-bold">{totalUniqueWords}</span>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
