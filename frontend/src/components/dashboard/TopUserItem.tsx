import type { SummaryResponse } from '@/types'

type TopUserItemProps = {
  user: SummaryResponse['topUsers'][0]
  index: number
}

export function TopUserItem({ user, index }: TopUserItemProps) {
  return (
    <div className="flex items-center justify-between p-3 bg-muted/50 rounded-lg">
      <div className="flex items-center space-x-3">
        <div className="flex items-center justify-center w-8 h-8 bg-primary text-primary-foreground rounded-full text-sm font-bold">
          {index + 1}
        </div>
        <div>
          <p className="font-medium">User {user.userId}</p>
          <p className="text-sm text-muted-foreground">
            {user.totalPosts} posts
          </p>
        </div>
      </div>
      <div className="text-right">
        <p className="font-bold text-lg">{user.uniqueWordCount}</p>
        <p className="text-xs text-muted-foreground">unique words</p>
      </div>
    </div>
  )
}
