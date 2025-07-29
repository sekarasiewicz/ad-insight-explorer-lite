import { useEffect, useState } from 'react'
import { ApiService } from '@/services/api'
import type { AnomaliesResponse, SummaryResponse } from '@/types'
import { DashboardContent } from './DashboardContent'
import { DashboardHeader } from './DashboardHeader'
import { ErrorState } from './ErrorState'
import { LoadingState } from './LoadingState'
import { StatsCards } from './StatsCards'

export function Dashboard() {
  const [anomalies, setAnomalies] = useState<AnomaliesResponse | null>(null)
  const [summary, setSummary] = useState<SummaryResponse | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [selectedUserId, setSelectedUserId] = useState<number | null>(null)

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true)
      setError(null)

      try {
        const [anomaliesData, summaryData] = await Promise.all([
          ApiService.getAnomalies(undefined, selectedUserId ?? undefined),
          ApiService.getSummary(),
        ])

        setAnomalies(anomaliesData)
        setSummary(summaryData)
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An error occurred')
      } finally {
        setLoading(false)
      }
    }

    fetchData()
  }, [selectedUserId])

  const handleUserFilter = (userId: number | null) => {
    setSelectedUserId(userId)
  }

  const handleRefresh = async () => {
    setLoading(true)
    setError(null)

    try {
      const [anomaliesData, summaryData] = await Promise.all([
        ApiService.getAnomalies(undefined, selectedUserId ?? undefined),
        ApiService.getSummary(),
      ])

      setAnomalies(anomaliesData)
      setSummary(summaryData)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <LoadingState />
  }

  if (error) {
    return <ErrorState error={error} onRetry={handleRefresh} />
  }

  return (
    <div className="min-h-screen bg-background text-foreground">
      <div className="container mx-auto px-4 py-8">
        <DashboardHeader onRefresh={handleRefresh} />
        <StatsCards summary={summary} anomalies={anomalies} />
        <DashboardContent
          anomalies={anomalies}
          summary={summary}
          selectedUserId={selectedUserId}
          onUserFilter={handleUserFilter}
        />
      </div>
    </div>
  )
}
