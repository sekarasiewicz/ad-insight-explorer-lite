import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import type { SummaryResponse } from '@/types'
import { MostFrequentWordsCard } from './MostFrequentWordsCard'
import { StatisticsCard } from './StatisticsCard'
import { TopUsersCard } from './TopUsersCard'

type SummaryPanelProps = {
  summary: SummaryResponse | null
}

export function SummaryPanel({ summary }: SummaryPanelProps) {
  if (!summary) {
    return (
      <Card>
        <CardHeader>
          <CardTitle>Summary</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-muted-foreground">No data available</p>
        </CardContent>
      </Card>
    )
  }

  return (
    <div className="space-y-6">
      <TopUsersCard topUsers={summary.topUsers} />
      <MostFrequentWordsCard mostFrequentWords={summary.mostFrequentWords} />
      <StatisticsCard summary={summary} />
    </div>
  )
}
