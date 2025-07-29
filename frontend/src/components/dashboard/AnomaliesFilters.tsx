import { User, X } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'

type AnomaliesFiltersProps = {
  searchTerm: string
  onSearchChange: (value: string) => void
  selectedUserId: number | null
  onClearUserFilter: () => void
  searchId: string
}

export function AnomaliesFilters({
  searchTerm,
  onSearchChange,
  selectedUserId,
  onClearUserFilter,
  searchId,
}: AnomaliesFiltersProps) {
  return (
    <div className="space-y-4">
      <div className="flex flex-col sm:flex-row gap-4">
        <div className="flex-1">
          <Label htmlFor={searchId}>Search Anomalies</Label>
          <Input
            id={searchId}
            placeholder="Search by title, reason, User 1, post ID, etc..."
            value={searchTerm}
            onChange={(e) => onSearchChange(e.target.value)}
            className="mt-1"
          />
        </div>
        {selectedUserId && (
          <div className="flex items-end">
            <Button variant="outline" onClick={onClearUserFilter} size="sm">
              <X className="h-4 w-4 mr-1" />
              Clear User Filter
            </Button>
          </div>
        )}
      </div>
      <div className="flex items-center justify-between">
        <p className="text-sm text-muted-foreground">Showing results...</p>
        {selectedUserId && (
          <div className="flex items-center space-x-2 text-sm">
            <User className="h-4 w-4" />
            <span>Filtered by User {selectedUserId}</span>
          </div>
        )}
      </div>
    </div>
  )
}
