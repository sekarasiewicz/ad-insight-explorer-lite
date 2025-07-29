import httpx
from typing import List, Optional
from app.models import Post
from app.utils.logger import logger


class JSONPlaceholderService:
    """Service for interacting with JSONPlaceholder API"""

    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.cache = {}

    async def get_posts(self, limit: Optional[int] = None) -> List[Post]:
        """
        Fetch posts from JSONPlaceholder API

        Args:
            limit: Optional limit on number of posts to fetch

        Returns:
            List of Post objects
        """
        try:
            async with httpx.AsyncClient() as client:
                url = f"{self.base_url}/posts"
                response = await client.get(url, timeout=10.0)
                response.raise_for_status()

                posts_data = response.json()

                # Apply limit if specified
                if limit:
                    posts_data = posts_data[:limit]

                # Convert to Post objects
                posts = [Post(**post_data) for post_data in posts_data]

                logger.info(
                    f"Successfully fetched {len(posts)} posts from JSONPlaceholder API"
                )
                return posts

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error occurred: {e.response.status_code}")
            raise Exception(f"Failed to fetch posts: HTTP {e.response.status_code}")
        except httpx.RequestError as e:
            logger.error(f"Request error occurred: {e}")
            raise Exception(f"Failed to fetch posts: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            raise Exception(f"Failed to fetch posts: {str(e)}")

    async def get_posts_by_user(self, user_id: int) -> List[Post]:
        """
        Fetch posts for a specific user

        Args:
            user_id: The user ID to fetch posts for

        Returns:
            List of Post objects for the user
        """
        try:
            async with httpx.AsyncClient() as client:
                url = f"{self.base_url}/posts"
                params = {"userId": user_id}
                response = await client.get(url, params=params, timeout=10.0)
                response.raise_for_status()

                posts_data = response.json()
                posts = [Post(**post_data) for post_data in posts_data]

                logger.info(
                    f"Successfully fetched {len(posts)} posts for user {user_id}"
                )
                return posts

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error occurred: {e.response.status_code}")
            raise Exception(
                f"Failed to fetch posts for user {user_id}: HTTP {e.response.status_code}"
            )
        except httpx.RequestError as e:
            logger.error(f"Request error occurred: {e}")
            raise Exception(f"Failed to fetch posts for user {user_id}: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error occurred: {e}")
            raise Exception(f"Failed to fetch posts for user {user_id}: {str(e)}")


# Global service instance
jsonplaceholder_service = JSONPlaceholderService()
