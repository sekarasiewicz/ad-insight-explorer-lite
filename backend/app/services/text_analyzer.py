import re
from collections import Counter, defaultdict
from typing import List, Dict, Set, Tuple
from difflib import SequenceMatcher
from app.models import Post, WordFrequency, UserSummary
from app.utils.logger import logger


class TextAnalyzer:
    """Service for text analysis and processing"""

    def __init__(self):
        # Common words to exclude from analysis
        self.stop_words = {
            "a",
            "an",
            "and",
            "are",
            "as",
            "at",
            "be",
            "by",
            "for",
            "from",
            "has",
            "he",
            "in",
            "is",
            "it",
            "its",
            "of",
            "on",
            "that",
            "the",
            "to",
            "was",
            "will",
            "with",
            "the",
            "this",
            "but",
            "they",
            "have",
            "had",
            "what",
            "said",
            "each",
            "which",
            "she",
            "do",
            "how",
            "their",
            "if",
            "up",
            "out",
            "many",
            "then",
            "them",
            "these",
            "so",
            "some",
            "her",
            "would",
            "make",
            "like",
            "into",
            "him",
            "time",
            "two",
            "more",
            "go",
            "no",
            "way",
            "could",
            "my",
            "than",
            "first",
            "been",
            "call",
            "who",
            "its",
            "now",
            "find",
            "long",
            "down",
            "day",
            "did",
            "get",
            "come",
            "made",
            "may",
            "part",
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

        logger.info(f"Calculated word frequency for {len(posts)} posts")
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

        logger.info(f"Calculated unique words for {len(user_summaries)} users")
        return user_summaries

    def calculate_text_similarity(self, text1: str, text2: str) -> float:
        """
        Calculate similarity between two texts using SequenceMatcher

        Args:
            text1: First text
            text2: Second text

        Returns:
            Similarity score between 0 and 1
        """
        return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()

    def find_similar_titles(
        self, posts: List[Post], similarity_threshold: float = 0.8
    ) -> List[Tuple[Post, Post, float]]:
        """
        Find pairs of posts with similar titles

        Args:
            posts: List of posts to analyze
            similarity_threshold: Minimum similarity score (0-1)

        Returns:
            List of tuples containing (post1, post2, similarity_score)
        """
        similar_pairs = []

        for i, post1 in enumerate(posts):
            for j, post2 in enumerate(posts[i + 1 :], i + 1):
                similarity = self.calculate_text_similarity(post1.title, post2.title)
                if similarity >= similarity_threshold:
                    similar_pairs.append((post1, post2, similarity))

        logger.info(f"Found {len(similar_pairs)} pairs of similar titles")
        return similar_pairs

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
