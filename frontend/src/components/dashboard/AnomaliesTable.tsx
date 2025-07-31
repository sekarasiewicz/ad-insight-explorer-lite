import { useId, useState } from 'react'
import { filterAndSortAnomalies, getReasonLabel } from '@/lib/anomaliesUtils'
import type { Anomaly, SortColumn, SortOrder } from '@/types'
import { AnomaliesFilters } from './AnomaliesFilters'
import { AnomaliesTableBody } from './AnomaliesTableBody'
import { AnomaliesTableHeader } from './AnomaliesTableHeader'

type AnomaliesTableProps = {
  anomalies: Anomaly[]
  onUserFilter: (userId: number | null) => void
  selectedUserId: number | null
}

export function AnomaliesTable({
  anomalies,
  onUserFilter,
  selectedUserId,
}: AnomaliesTableProps) {
  const [searchTerm, setSearchTerm] = useState('')
  const [sortBy, setSortBy] = useState<SortColumn>('id')
  const [sortOrder, setSortOrder] = useState<SortOrder>('asc')
  const searchId = useId()

  const handleSort = (column: SortColumn) => {
    if (sortBy === column) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc')
    } else {
      setSortBy(column)
      setSortOrder('asc')
    }
  }

  const clearUserFilter = () => {
    onUserFilter(null)
  }

  const filteredAndSortedAnomalies = filterAndSortAnomalies(
    anomalies,
    searchTerm,
    sortBy,
    sortOrder
  )

  return (
    <div className="space-y-4">
      <AnomaliesFilters
        searchTerm={searchTerm}
        onSearchChange={setSearchTerm}
        selectedUserId={selectedUserId}
        onClearUserFilter={clearUserFilter}
        searchId={searchId}
      />
      <div className="flex items-center justify-between">
        <p className="text-sm text-muted-foreground">
          Showing {filteredAndSortedAnomalies.length} of {anomalies.length}{' '}
          anomalies
        </p>
      </div>
      <div className="border rounded-lg overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full">
            <AnomaliesTableHeader
              sortBy={sortBy}
              sortOrder={sortOrder}
              onSort={handleSort}
            />
            <AnomaliesTableBody
              anomalies={filteredAndSortedAnomalies}
              onUserFilter={onUserFilter}
              getReasonLabel={getReasonLabel}
            />
          </table>
        </div>
      </div>
    </div>
  )
}
