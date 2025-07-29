import { TrendingUp } from 'lucide-react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import type { SummaryResponse } from '@/types'
import { WordItem } from './WordItem'

type MostFrequentWordsCardProps = {
  mostFrequentWords: SummaryResponse['mostFrequentWords']
}

export function MostFrequentWordsCard({
  mostFrequentWords,
}: MostFrequentWordsCardProps) {
  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <TrendingUp className="h-5 w-5" />
          <span>Most Frequent Words</span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-2">
          {mostFrequentWords.slice(0, 15).map((word, index) => (
            <WordItem key={word.word} word={word} index={index} />
          ))}
        </div>
        {mostFrequentWords.length > 15 && (
          <p className="text-xs text-muted-foreground mt-3 text-center">
            Showing top 15 of {mostFrequentWords.length} words
          </p>
        )}
      </CardContent>
    </Card>
  )
}
