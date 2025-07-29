import { FileText, Filter, Hash, User } from 'lucide-react'
import { Button } from '@/components/ui/button'

type SortColumn = 'id' | 'userId' | 'title' | 'reason'
type SortOrder = 'asc' | 'desc'

type AnomaliesTableHeaderProps = {
  sortBy: SortColumn
  sortOrder: SortOrder
  onSort: (column: SortColumn) => void
}

export function AnomaliesTableHeader({
  sortBy,
  sortOrder,
  onSort,
}: AnomaliesTableHeaderProps) {
  return (
    <thead className="bg-muted/50">
      <tr>
        <th className="px-4 py-3 text-left text-sm font-medium">
          <Button
            variant="ghost"
            size="sm"
            onClick={() => onSort('id')}
            className="h-auto p-0 font-medium"
          >
            <Hash className="h-4 w-4 mr-1" />
            Post ID
            {sortBy === 'id' && (
              <span className="ml-1">{sortOrder === 'asc' ? '↑' : '↓'}</span>
            )}
          </Button>
        </th>
        <th className="px-4 py-3 text-left text-sm font-medium">
          <Button
            variant="ghost"
            size="sm"
            onClick={() => onSort('userId')}
            className="h-auto p-0 font-medium"
          >
            <User className="h-4 w-4 mr-1" />
            User ID
            {sortBy === 'userId' && (
              <span className="ml-1">{sortOrder === 'asc' ? '↑' : '↓'}</span>
            )}
          </Button>
        </th>
        <th className="px-4 py-3 text-left text-sm font-medium">
          <Button
            variant="ghost"
            size="sm"
            onClick={() => onSort('title')}
            className="h-auto p-0 font-medium"
          >
            <FileText className="h-4 w-4 mr-1" />
            Title
            {sortBy === 'title' && (
              <span className="ml-1">{sortOrder === 'asc' ? '↑' : '↓'}</span>
            )}
          </Button>
        </th>
        <th className="px-4 py-3 text-left text-sm font-medium">
          <Button
            variant="ghost"
            size="sm"
            onClick={() => onSort('reason')}
            className="h-auto p-0 font-medium"
          >
            <Filter className="h-4 w-4 mr-1" />
            Reason
            {sortBy === 'reason' && (
              <span className="ml-1">{sortOrder === 'asc' ? '↑' : '↓'}</span>
            )}
          </Button>
        </th>
      </tr>
    </thead>
  )
}
