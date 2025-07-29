import type { Anomaly } from '@/types'
import { AnomaliesTableRow } from './AnomaliesTableRow'

type AnomaliesTableBodyProps = {
  anomalies: Anomaly[]
  onUserFilter: (userId: number) => void
  getReasonLabel: (reason: string) => string
}

export function AnomaliesTableBody({
  anomalies,
  onUserFilter,
  getReasonLabel,
}: AnomaliesTableBodyProps) {
  if (anomalies.length === 0) {
    return (
      <tbody>
        <tr>
          <td
            colSpan={4}
            className="px-4 py-8 text-center text-muted-foreground"
          >
            No anomalies found
          </td>
        </tr>
      </tbody>
    )
  }

  return (
    <tbody className="divide-y">
      {anomalies.map((anomaly) => (
        <AnomaliesTableRow
          key={anomaly.id}
          anomaly={anomaly}
          onUserFilter={onUserFilter}
          getReasonLabel={getReasonLabel}
        />
      ))}
    </tbody>
  )
}
