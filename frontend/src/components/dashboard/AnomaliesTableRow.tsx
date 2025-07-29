import { AlertTriangle, FileText } from 'lucide-react'
import { Button } from '@/components/ui/button'
import type { Anomaly } from '@/types'

type AnomaliesTableRowProps = {
  anomaly: Anomaly
  onUserFilter: (userId: number) => void
  getReasonLabel: (reason: string) => string
}

export function AnomaliesTableRow({
  anomaly,
  onUserFilter,
  getReasonLabel,
}: AnomaliesTableRowProps) {
  const getReasonIcon = (reason: string) => {
    switch (reason) {
      case 'short_title':
        return <FileText className="h-4 w-4 text-orange-500" />
      case 'duplicate_title':
        return <AlertTriangle className="h-4 w-4 text-red-500" />
      case 'bot_like_behavior':
        return <AlertTriangle className="h-4 w-4 text-purple-500" />
      default:
        return <AlertTriangle className="h-4 w-4 text-gray-500" />
    }
  }

  return (
    <tr className="hover:bg-muted/50">
      <td className="px-4 py-3 text-sm font-mono">#{anomaly.id}</td>
      <td className="px-4 py-3 text-sm">
        <Button
          variant="ghost"
          size="sm"
          onClick={() => onUserFilter(anomaly.userId)}
          className="h-auto p-0 text-sm"
        >
          User {anomaly.userId}
        </Button>
      </td>
      <td className="px-4 py-3 text-sm max-w-xs truncate" title={anomaly.title}>
        {anomaly.title}
      </td>
      <td className="px-4 py-3 text-sm">
        <div className="flex items-center space-x-2">
          {getReasonIcon(anomaly.reason)}
          <span>{getReasonLabel(anomaly.reason)}</span>
        </div>
        {anomaly.details && (
          <p className="text-xs text-muted-foreground mt-1">
            {anomaly.details}
          </p>
        )}
      </td>
    </tr>
  )
}
