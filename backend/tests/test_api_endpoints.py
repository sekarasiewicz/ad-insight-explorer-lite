import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app
from app.models import Post, Anomaly, WordFrequency, UserSummary

client = TestClient(app)


class TestPostsEndpoint:
    @patch("app.services.jsonplaceholder_service.jsonplaceholder_service.get_posts")
    def test_get_posts_success(self, mock_get_posts):
        """Test successful posts retrieval"""
        mock_posts = [
            Post(userId=1, id=1, title="Test Post", body="Test body"),
            Post(userId=2, id=2, title="Another Post", body="Another body"),
        ]
        mock_get_posts.return_value = mock_posts

        response = client.get("/api/posts/")

        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 2
        assert len(data["posts"]) == 2
        assert data["posts"][0]["title"] == "Test Post"
        assert data["posts"][1]["title"] == "Another Post"

    @patch("app.services.jsonplaceholder_service.jsonplaceholder_service.get_posts")
    def test_get_posts_with_limit(self, mock_get_posts):
        """Test posts retrieval with limit parameter"""
        mock_posts = [
            Post(userId=1, id=1, title="Test Post", body="Test body"),
        ]
        mock_get_posts.return_value = mock_posts

        response = client.get("/api/posts/?limit=1")

        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1
        assert len(data["posts"]) == 1
        mock_get_posts.assert_called_once_with(limit=1)


class TestAnomaliesEndpoint:
    @patch("app.services.jsonplaceholder_service.jsonplaceholder_service.get_posts")
    @patch("app.services.anomaly_detector.anomaly_detector.detect_anomalies")
    @patch("app.services.anomaly_detector.anomaly_detector.get_anomaly_summary")
    def test_get_anomalies_success(self, mock_summary, mock_detect, mock_get_posts):
        """Test successful anomalies detection"""
        mock_posts = [
            Post(userId=1, id=1, title="Short", body="Test body"),
        ]
        mock_anomalies = [
            Anomaly(
                userId=1, id=1, title="Short", reason="short_title", details="Too short"
            ),
        ]
        mock_summary_data = {
            "total_anomalies": 1,
            "by_reason": {"short_title": 1},
            "by_user": {1: 1},
            "unique_users_affected": 1,
        }

        mock_get_posts.return_value = mock_posts
        mock_detect.return_value = mock_anomalies
        mock_summary.return_value = mock_summary_data

        response = client.get("/api/anomalies/")

        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1
        assert len(data["anomalies"]) == 1
        assert data["anomalies"][0]["reason"] == "short_title"
        assert data["summary"]["total_anomalies"] == 1

    @patch("app.services.jsonplaceholder_service.jsonplaceholder_service.get_posts")
    def test_get_anomalies_with_user_filter(self, mock_get_posts):
        """Test anomalies filtering by user ID"""
        mock_posts = [
            Post(userId=1, id=1, title="Short", body="Test body"),
            Post(userId=2, id=2, title="Also short", body="Test body"),
        ]
        mock_get_posts.return_value = mock_posts

        response = client.get("/api/anomalies/?user_id=1")

        assert response.status_code == 200
        # The filtering logic is in the service, so we just verify the endpoint accepts the parameter


class TestSummaryEndpoint:
    @patch("app.services.jsonplaceholder_service.jsonplaceholder_service.get_posts")
    @patch("app.services.text_analyzer.text_analyzer.calculate_word_frequency")
    @patch("app.services.text_analyzer.text_analyzer.get_top_users_by_unique_words")
    def test_get_summary_success(self, mock_top_users, mock_word_freq, mock_get_posts):
        """Test successful summary generation"""
        mock_posts = [
            Post(userId=1, id=1, title="Hello world", body="Test body"),
            Post(userId=2, id=2, title="Another post", body="Another body"),
        ]
        mock_word_frequencies = [
            WordFrequency(word="hello", count=2),
            WordFrequency(word="world", count=1),
        ]
        mock_top_users_data = [
            UserSummary(
                userId=1,
                uniqueWordCount=5,
                totalPosts=1,
                uniqueWords=["hello", "world"],
            ),
            UserSummary(
                userId=2,
                uniqueWordCount=3,
                totalPosts=1,
                uniqueWords=["another", "post"],
            ),
        ]

        mock_get_posts.return_value = mock_posts
        mock_word_freq.return_value = mock_word_frequencies
        mock_top_users.return_value = mock_top_users_data

        response = client.get("/api/summary/")

        assert response.status_code == 200
        data = response.json()
        assert data["totalPosts"] == 2
        assert data["totalUsers"] == 2
        assert len(data["topUsers"]) == 2
        assert len(data["mostFrequentWords"]) == 2
        assert data["topUsers"][0]["userId"] == 1
        assert data["mostFrequentWords"][0]["word"] == "hello"

    @patch("app.services.jsonplaceholder_service.jsonplaceholder_service.get_posts")
    def test_get_summary_with_parameters(self, mock_get_posts):
        """Test summary with custom parameters"""
        mock_posts = [Post(userId=1, id=1, title="Test", body="Test")]
        mock_get_posts.return_value = mock_posts

        response = client.get("/api/summary/?top_users=5&top_words=10")

        assert response.status_code == 200
        # Verify parameters are passed through


class TestErrorHandling:
    @patch("app.services.jsonplaceholder_service.jsonplaceholder_service.get_posts")
    def test_api_error_handling(self, mock_get_posts):
        """Test API error handling"""
        mock_get_posts.side_effect = Exception("API Error")

        response = client.get("/api/posts/")

        assert response.status_code == 500
        data = response.json()
        assert "error" in data or "detail" in data

    def test_invalid_endpoint(self):
        """Test invalid endpoint handling"""
        response = client.get("/api/invalid/")

        assert response.status_code == 404
