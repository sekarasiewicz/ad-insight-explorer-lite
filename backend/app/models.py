from pydantic import BaseModel
from typing import List, Optional


class ErrorResponse(BaseModel):
    error: str
    message: str


# Post-related models
class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class PostsResponse(BaseModel):
    posts: List[Post]
    total: int


# Anomaly-related models
class AnomalyReason(str):
    SHORT_TITLE = "short_title"
    DUPLICATE_TITLE = "duplicate_title"
    BOT_LIKE_BEHAVIOR = "bot_like_behavior"


class Anomaly(BaseModel):
    userId: int
    id: int
    title: str
    reason: str
    details: Optional[str] = None


class AnomaliesResponse(BaseModel):
    anomalies: List[Anomaly]
    total: int
    summary: dict


# Summary-related models
class UserSummary(BaseModel):
    userId: int
    uniqueWordCount: int
    totalPosts: int
    uniqueWords: List[str]


class WordFrequency(BaseModel):
    word: str
    count: int


class SummaryResponse(BaseModel):
    topUsers: List[UserSummary]
    mostFrequentWords: List[WordFrequency]
    totalPosts: int
    totalUsers: int
