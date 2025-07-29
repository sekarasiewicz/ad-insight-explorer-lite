from collections import defaultdict
from typing import List, Dict, Set
from app.models import Post, Anomaly


class AnomalyDetector:
    """Service for detecting anomalies in posts"""

    def __init__(self):
        self.short_title_threshold = 15
        self.bot_detection_threshold = 5

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

        print(f"Detected {len(anomalies)} total anomalies")
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

        print(f"Detected {len(anomalies)} posts with short titles")
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

        print(f"Detected {len(anomalies)} posts with duplicate titles")
        return anomalies

    def _detect_bot_like_behavior(self, posts: List[Post]) -> List[Anomaly]:
        """
        Detect users with more than threshold posts having similar titles
        Simplified: Just check for exact duplicate titles per user

        Args:
            posts: List of posts to analyze

        Returns:
            List of Anomaly objects for bot-like behavior
        """
        anomalies = []
        user_titles: Dict[int, Dict[str, int]] = defaultdict(lambda: defaultdict(int))

        # Count occurrences of each title per user
        for post in posts:
            user_titles[post.userId][post.title] += 1

        # Find users with multiple posts having the same title
        for user_id, title_counts in user_titles.items():
            for title, count in title_counts.items():
                if count >= self.bot_detection_threshold:
                    # Find all posts with this title for this user
                    user_posts_with_title = [
                        p for p in posts if p.userId == user_id and p.title == title
                    ]

                    # Mark all these posts as bot-like behavior
                    for post in user_posts_with_title:
                        anomaly = Anomaly(
                            userId=post.userId,
                            id=post.id,
                            title=post.title,
                            reason="bot_like_behavior",
                            details=f"User has {count} posts with identical title",
                        )
                        anomalies.append(anomaly)

        print(f"Detected {len(anomalies)} posts with bot-like behavior")
        return anomalies

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
