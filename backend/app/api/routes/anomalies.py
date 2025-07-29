from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models import AnomaliesResponse
from app.services.jsonplaceholder_service import jsonplaceholder_service
from app.services.anomaly_detector import anomaly_detector
from app.utils.logger import logger

router = APIRouter(prefix="/anomalies", tags=["anomalies"])


@router.get("/", response_model=AnomaliesResponse)
async def get_anomalies(
    limit: Optional[int] = Query(None, description="Limit number of posts to analyze"),
    user_id: Optional[int] = Query(None, description="Filter anomalies by user ID"),
):
    """
    Detect anomalies in posts from JSONPlaceholder API

    Args:
        limit: Optional limit on number of posts to analyze
        user_id: Optional user ID to filter anomalies

    Returns:
        AnomaliesResponse with list of anomalies and summary statistics
    """
    try:
        logger.info(f"Detecting anomalies with limit: {limit}, user_id: {user_id}")

        # Fetch posts (always fetch all for proper anomaly detection)
        posts = await jsonplaceholder_service.get_posts(limit=limit)

        # Detect anomalies
        anomalies = anomaly_detector.detect_anomalies(posts)

        # Filter by user_id if specified
        if user_id:
            anomalies = [a for a in anomalies if a.userId == user_id]

        # Generate summary
        summary = anomaly_detector.get_anomaly_summary(anomalies)

        return AnomaliesResponse(
            anomalies=anomalies, total=len(anomalies), summary=summary
        )

    except Exception as e:
        logger.error(f"Error detecting anomalies: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to detect anomalies: {str(e)}"
        )


@router.get("/summary")
async def get_anomaly_summary(
    limit: Optional[int] = Query(None, description="Limit number of posts to analyze"),
):
    """
    Get summary statistics for anomalies

    Args:
        limit: Optional limit on number of posts to analyze

    Returns:
        Dictionary with anomaly summary statistics
    """
    try:
        logger.info(f"Getting anomaly summary with limit: {limit}")

        # Fetch posts
        posts = await jsonplaceholder_service.get_posts(limit=limit)

        # Detect anomalies
        anomalies = anomaly_detector.detect_anomalies(posts)

        # Generate summary
        summary = anomaly_detector.get_anomaly_summary(anomalies)

        return summary

    except Exception as e:
        logger.error(f"Error getting anomaly summary: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to get anomaly summary: {str(e)}"
        )
