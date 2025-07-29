import { Hash } from 'lucide-react'
import type { SummaryResponse } from '@/types'

type WordItemProps = {
  word: SummaryResponse['mostFrequentWords'][0]
  index: number
}

export function WordItem({ word, index }: WordItemProps) {
  return (
    <div className="flex items-center justify-between">
      <div className="flex items-center space-x-2">
        <span className="text-sm font-mono text-muted-foreground w-4">
          {index + 1}.
        </span>
        <span className="font-medium">{word.word}</span>
      </div>
      <div className="flex items-center space-x-1">
        <Hash className="h-3 w-3 text-muted-foreground" />
        <span className="text-sm font-bold">{word.count}</span>
      </div>
    </div>
  )
}
