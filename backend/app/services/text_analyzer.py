import re
from collections import Counter, defaultdict
from typing import List, Dict, Set, Tuple

from app.models import Post, WordFrequency, UserSummary


class TextAnalyzer:
    """Service for text analysis and processing"""

    def __init__(self):
        # Essential stop words - only the most common ones
        self.stop_words = {
            "the",
            "a",
            "an",
            "and",
            "or",
            "but",
            "in",
            "on",
            "at",
            "to",
            "of",
            "for",
            "with",
            "by",
        }

    def clean_text(self, text: str) -> str:
        """
        Clean and normalize text for analysis

        Args:
            text: Raw text to clean

        Returns:
            Cleaned text
        """
        # Convert to lowercase and remove special characters
        text = re.sub(r"[^\w\s]", "", text.lower())
        return text.strip()

    def extract_words(self, text: str) -> List[str]:
        """
        Extract words from text, excluding stop words

        Args:
            text: Text to extract words from

        Returns:
            List of words
        """
        cleaned_text = self.clean_text(text)
        words = cleaned_text.split()
        # Filter out stop words and short words
        words = [
            word for word in words if word not in self.stop_words and len(word) > 2
        ]
        return words

    def calculate_word_frequency(self, posts: List[Post]) -> List[WordFrequency]:
        """
        Calculate word frequency across all post titles

        Args:
            posts: List of posts to analyze

        Returns:
            List of WordFrequency objects sorted by count
        """
        word_counter = Counter()

        for post in posts:
            words = self.extract_words(post.title)
            word_counter.update(words)

        # Convert to WordFrequency objects and sort by count
        word_frequencies = [
            WordFrequency(word=word, count=count)
            for word, count in word_counter.most_common(50)  # Top 50 words
        ]

        print(f"Calculated word frequency for {len(posts)} posts")
        return word_frequencies

    def calculate_user_unique_words(self, posts: List[Post]) -> List[UserSummary]:
        """
        Calculate unique words per user across their post titles

        Args:
            posts: List of posts to analyze

        Returns:
            List of UserSummary objects sorted by unique word count
        """
        user_words: Dict[int, Set[str]] = defaultdict(set)
        user_posts: Dict[int, int] = defaultdict(int)

        for post in posts:
            words = self.extract_words(post.title)
            user_words[post.userId].update(words)
            user_posts[post.userId] += 1

        # Convert to UserSummary objects
        user_summaries = []
        for user_id, unique_words in user_words.items():
            user_summary = UserSummary(
                userId=user_id,
                uniqueWordCount=len(unique_words),
                totalPosts=user_posts[user_id],
                uniqueWords=list(unique_words),
            )
            user_summaries.append(user_summary)

        # Sort by unique word count (descending)
        user_summaries.sort(key=lambda x: x.uniqueWordCount, reverse=True)

        print(f"Calculated unique words for {len(user_summaries)} users")
        return user_summaries

    def get_top_users_by_unique_words(
        self, posts: List[Post], top_n: int = 3
    ) -> List[UserSummary]:
        """
        Get top N users with most unique words

        Args:
            posts: List of posts to analyze
            top_n: Number of top users to return

        Returns:
            List of top N UserSummary objects
        """
        user_summaries = self.calculate_user_unique_words(posts)
        return user_summaries[:top_n]


# Global service instance
text_analyzer = TextAnalyzer()
