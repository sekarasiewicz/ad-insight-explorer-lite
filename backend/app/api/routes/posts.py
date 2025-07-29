from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.models import PostsResponse
from app.services.jsonplaceholder_service import jsonplaceholder_service
from app.utils.logger import logger

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/", response_model=PostsResponse)
async def get_posts(
    limit: Optional[int] = Query(None, description="Limit number of posts to fetch"),
):
    """
    Fetch posts from JSONPlaceholder API

    Args:
        limit: Optional limit on number of posts to fetch

    Returns:
        PostsResponse with list of posts and total count
    """
    try:
        logger.info(f"Fetching posts with limit: {limit}")
        posts = await jsonplaceholder_service.get_posts(limit=limit)

        return PostsResponse(posts=posts, total=len(posts))

    except Exception as e:
        logger.error(f"Error fetching posts: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch posts: {str(e)}")


@router.get("/{user_id}", response_model=PostsResponse)
async def get_posts_by_user(user_id: int):
    """
    Fetch posts for a specific user

    Args:
        user_id: The user ID to fetch posts for

    Returns:
        PostsResponse with list of posts for the user and total count
    """
    try:
        logger.info(f"Fetching posts for user {user_id}")
        posts = await jsonplaceholder_service.get_posts_by_user(user_id)

        return PostsResponse(posts=posts, total=len(posts))

    except Exception as e:
        logger.error(f"Error fetching posts for user {user_id}: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch posts for user {user_id}: {str(e)}",
        )
