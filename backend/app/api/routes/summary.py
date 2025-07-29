from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models import SummaryResponse
from app.services.jsonplaceholder_service import jsonplaceholder_service
from app.services.text_analyzer import text_analyzer
from app.utils.logger import logger

router = APIRouter(prefix="/summary", tags=["summary"])


@router.get("/", response_model=SummaryResponse)
async def get_summary(
    limit: Optional[int] = Query(None, description="Limit number of posts to analyze"),
    top_users: Optional[int] = Query(3, description="Number of top users to return"),
    top_words: Optional[int] = Query(20, description="Number of top words to return"),
):
    """
    Get summary analysis of posts including word frequency and user insights

    Args:
        limit: Optional limit on number of posts to analyze
        top_users: Number of top users to return (default: 3)
        top_words: Number of top words to return (default: 20)

    Returns:
        SummaryResponse with top users, word frequencies, and statistics
    """
    try:
        logger.info(
            f"Getting summary with limit: {limit}, top_users: {top_users}, top_words: {top_words}"
        )

        # Fetch posts
        posts = await jsonplaceholder_service.get_posts(limit=limit)

        if not posts:
            return SummaryResponse(
                topUsers=[], mostFrequentWords=[], totalPosts=0, totalUsers=0
            )

        # Calculate word frequency
        word_frequencies = text_analyzer.calculate_word_frequency(posts)
        top_word_frequencies = word_frequencies[:top_words]

        # Get top users by unique words
        top_users_list = text_analyzer.get_top_users_by_unique_words(posts, top_users)

        # Calculate total unique users
        unique_users = len(set(post.userId for post in posts))

        return SummaryResponse(
            topUsers=top_users_list,
            mostFrequentWords=top_word_frequencies,
            totalPosts=len(posts),
            totalUsers=unique_users,
        )

    except Exception as e:
        logger.error(f"Error getting summary: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get summary: {str(e)}")
