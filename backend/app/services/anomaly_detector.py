from collections import defaultdict
from typing import List, Dict, Set
from app.models import Post, Anomaly
from app.services.text_analyzer import text_analyzer
from app.utils.logger import logger


class AnomalyDetector:
    """Service for detecting anomalies in posts"""

    def __init__(self):
        self.short_title_threshold = 15
        self.bot_detection_threshold = 5
        self.similarity_threshold = 0.8

    def detect_anomalies(self, posts: List[Post]) -> List[Anomaly]:
        """
        Detect all types of anomalies in posts

        Args:
            posts: List of posts to analyze

        Returns:
            List of Anomaly objects
        """
        anomalies = []

        # Detect short titles
        short_title_anomalies = self._detect_short_titles(posts)
        anomalies.extend(short_title_anomalies)

        # Detect duplicate titles
        duplicate_anomalies = self._detect_duplicate_titles(posts)
        anomalies.extend(duplicate_anomalies)

        # Detect bot-like behavior
        bot_anomalies = self._detect_bot_like_behavior(posts)
        anomalies.extend(bot_anomalies)

        logger.info(f"Detected {len(anomalies)} total anomalies")
        return anomalies

    def _detect_short_titles(self, posts: List[Post]) -> List[Anomaly]:
        """
        Detect posts with titles shorter than the threshold

        Args:
            posts: List of posts to analyze

        Returns:
            List of Anomaly objects for short titles
        """
        anomalies = []

        for post in posts:
            if len(post.title) < self.short_title_threshold:
                anomaly = Anomaly(
                    userId=post.userId,
                    id=post.id,
                    title=post.title,
                    reason="short_title",
                    details=f"Title length ({len(post.title)}) is below threshold ({self.short_title_threshold})",
                )
                anomalies.append(anomaly)

        logger.info(f"Detected {len(anomalies)} posts with short titles")
        return anomalies

    def _detect_duplicate_titles(self, posts: List[Post]) -> List[Anomaly]:
        """
        Detect posts with duplicate titles by the same user

        Args:
            posts: List of posts to analyze

        Returns:
            List of Anomaly objects for duplicate titles
        """
        anomalies = []
        user_titles: Dict[int, Set[str]] = defaultdict(set)

        # First pass: collect all titles per user
        for post in posts:
            user_titles[post.userId].add(post.title)

        # Second pass: find posts with duplicate titles
        for post in posts:
            # Check if this user has multiple posts with the same title
            user_posts_with_same_title = [
                p for p in posts if p.userId == post.userId and p.title == post.title
            ]

            if len(user_posts_with_same_title) > 1:
                # This post has a duplicate title
                anomaly = Anomaly(
                    userId=post.userId,
                    id=post.id,
                    title=post.title,
                    reason="duplicate_title",
                    details=f"User has {len(user_posts_with_same_title)} posts with identical title",
                )
                anomalies.append(anomaly)

        logger.info(f"Detected {len(anomalies)} posts with duplicate titles")
        return anomalies

    def _detect_bot_like_behavior(self, posts: List[Post]) -> List[Anomaly]:
        """
        Detect users with more than threshold posts having similar titles

        Args:
            posts: List of posts to analyze

        Returns:
            List of Anomaly objects for bot-like behavior
        """
        anomalies = []
        user_posts: Dict[int, List[Post]] = defaultdict(list)

        # Group posts by user
        for post in posts:
            user_posts[post.userId].append(post)

        # Analyze each user's posts for similar titles
        for user_id, user_post_list in user_posts.items():
            if len(user_post_list) < self.bot_detection_threshold:
                continue

            # Find similar titles within this user's posts
            similar_groups = self._find_similar_title_groups(user_post_list)

            for group in similar_groups:
                if len(group) >= self.bot_detection_threshold:
                    # This user has bot-like behavior
                    for post in group:
                        anomaly = Anomaly(
                            userId=post.userId,
                            id=post.id,
                            title=post.title,
                            reason="bot_like_behavior",
                            details=f"User has {len(group)} posts with similar titles (similarity >= {self.similarity_threshold})",
                        )
                        anomalies.append(anomaly)

        logger.info(f"Detected {len(anomalies)} posts with bot-like behavior")
        return anomalies

    def _find_similar_title_groups(self, posts: List[Post]) -> List[List[Post]]:
        """
        Find groups of posts with similar titles

        Args:
            posts: List of posts to analyze

        Returns:
            List of groups, where each group contains posts with similar titles
        """
        if len(posts) < 2:
            return []

        # Use the text analyzer to find similar pairs
        similar_pairs = text_analyzer.find_similar_titles(
            posts, self.similarity_threshold
        )

        # Group posts by similarity
        groups = []
        processed_posts = set()

        for post1, post2, similarity in similar_pairs:
            # Find or create group for post1
            group1 = None
            for group in groups:
                if post1 in group:
                    group1 = group
                    break

            # Find or create group for post2
            group2 = None
            for group in groups:
                if post2 in group:
                    group2 = group
                    break

            if group1 is None and group2 is None:
                # Create new group
                new_group = [post1, post2]
                groups.append(new_group)
            elif group1 is None:
                # Add post1 to group2
                group2.append(post1)
            elif group2 is None:
                # Add post2 to group1
                group1.append(post2)
            elif group1 != group2:
                # Merge groups
                group1.extend(group2)
                groups.remove(group2)

        # Add posts that weren't part of any similar pair
        for post in posts:
            if not any(post in group for group in groups):
                groups.append([post])

        # Filter groups that meet the threshold
        threshold_groups = [
            group for group in groups if len(group) >= self.bot_detection_threshold
        ]

        return threshold_groups

    def get_anomaly_summary(self, anomalies: List[Anomaly]) -> Dict:
        """
        Generate summary statistics for anomalies

        Args:
            anomalies: List of anomalies to summarize

        Returns:
            Dictionary with summary statistics
        """
        summary = {
            "total_anomalies": len(anomalies),
            "by_reason": defaultdict(int),
            "by_user": defaultdict(int),
            "unique_users_affected": len(set(anomaly.userId for anomaly in anomalies)),
        }

        for anomaly in anomalies:
            summary["by_reason"][anomaly.reason] += 1
            summary["by_user"][anomaly.userId] += 1

        # Convert defaultdict to regular dict for JSON serialization
        summary["by_reason"] = dict(summary["by_reason"])
        summary["by_user"] = dict(summary["by_user"])

        return summary


# Global service instance
anomaly_detector = AnomalyDetector()
