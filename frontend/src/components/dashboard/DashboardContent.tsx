import { AlertTriangle } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import type { AnomaliesResponse, SummaryResponse } from '@/types'
import { AnomaliesTable } from './AnomaliesTable'
import { SummaryPanel } from './SummaryPanel'

type DashboardContentProps = {
  anomalies: AnomaliesResponse | null
  summary: SummaryResponse | null
  selectedUserId: number | null
  onUserFilter: (userId: number | null) => void
}

export function DashboardContent({
  anomalies,
  summary,
  selectedUserId,
  onUserFilter,
}: DashboardContentProps) {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
      {/* Anomalies Table */}
      <div className="lg:col-span-2">
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center space-x-2">
              <AlertTriangle className="h-5 w-5" />
              <span>Anomalies Detection</span>
            </CardTitle>
          </CardHeader>
          <CardContent>
            <AnomaliesTable
              anomalies={anomalies?.anomalies || []}
              onUserFilter={onUserFilter}
              selectedUserId={selectedUserId}
            />
          </CardContent>
        </Card>
      </div>

      {/* Summary Panel */}
      <div className="lg:col-span-1">
        <SummaryPanel summary={summary} />
      </div>
    </div>
  )
}
