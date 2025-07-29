import { Award } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import type { SummaryResponse } from '@/types'
import { TopUserItem } from './TopUserItem'

type TopUsersCardProps = {
  topUsers: SummaryResponse['topUsers']
}

export function TopUsersCard({ topUsers }: TopUsersCardProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Award className="h-5 w-5" />
          <span>Top Users by Unique Words</span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {topUsers.map((user, index) => (
            <TopUserItem key={user.userId} user={user} index={index} />
          ))}
        </div>
      </CardContent>
    </Card>
  )
}
