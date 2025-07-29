from app.services.anomaly_detector import AnomalyDetector
from app.models import Post


class TestAnomalyDetector:
    def setup_method(self):
        self.detector = AnomalyDetector()

    def test_detect_short_titles(self):
        """Test detection of posts with short titles"""
        posts = [
            Post(userId=1, id=1, title="Short", body="Test body"),
            Post(userId=1, id=2, title="This is a longer title", body="Test body"),
            Post(userId=2, id=3, title="Also short", body="Test body"),
        ]

        anomalies = self.detector._detect_short_titles(posts)

        assert len(anomalies) == 2
        assert anomalies[0].reason == "short_title"
        assert anomalies[0].userId == 1
        assert anomalies[0].id == 1
        assert anomalies[1].reason == "short_title"
        assert anomalies[1].userId == 2
        assert anomalies[1].id == 3

    def test_detect_duplicate_titles(self):
        """Test detection of duplicate titles by same user"""
        posts = [
            Post(userId=1, id=1, title="Same Title", body="Body 1"),
            Post(userId=1, id=2, title="Same Title", body="Body 2"),  # Duplicate
            Post(userId=1, id=3, title="Different Title", body="Body 3"),
            Post(userId=2, id=4, title="Same Title", body="Body 4"),  # Different user
        ]

        anomalies = self.detector._detect_duplicate_titles(posts)

        assert len(anomalies) == 2  # Both posts with duplicate title
        assert all(a.reason == "duplicate_title" for a in anomalies)
        assert all(a.userId == 1 for a in anomalies)
        assert {a.id for a in anomalies} == {1, 2}

    def test_detect_bot_like_behavior(self):
        """Test detection of bot-like behavior with similar titles"""
        posts = [
            Post(userId=1, id=1, title="Post about technology", body="Body 1"),
            Post(userId=1, id=2, title="Post about technology", body="Body 2"),
            Post(userId=1, id=3, title="Post about technology", body="Body 3"),
            Post(userId=1, id=4, title="Post about technology", body="Body 4"),
            Post(userId=1, id=5, title="Post about technology", body="Body 5"),
            Post(userId=2, id=6, title="Different content", body="Body 6"),
        ]

        anomalies = self.detector._detect_bot_like_behavior(posts)

        # Should detect all 5 posts from user 1 as bot-like
        assert len(anomalies) == 5
        assert all(a.reason == "bot_like_behavior" for a in anomalies)
        assert all(a.userId == 1 for a in anomalies)

    def test_get_anomaly_summary(self):
        """Test anomaly summary generation"""
        from app.models import Anomaly

        anomalies = [
            Anomaly(userId=1, id=1, title="Short", reason="short_title", details=""),
            Anomaly(
                userId=1, id=2, title="Also short", reason="short_title", details=""
            ),
            Anomaly(
                userId=2, id=3, title="Duplicate", reason="duplicate_title", details=""
            ),
        ]

        summary = self.detector.get_anomaly_summary(anomalies)

        assert summary["total_anomalies"] == 3
        assert summary["by_reason"]["short_title"] == 2
        assert summary["by_reason"]["duplicate_title"] == 1
        assert summary["by_user"][1] == 2
        assert summary["by_user"][2] == 1
        assert summary["unique_users_affected"] == 2

    def test_detect_all_anomalies(self):
        """Test the main detect_anomalies method"""
        posts = [
            Post(userId=1, id=1, title="Short", body="Body"),  # Short title
            Post(userId=1, id=2, title="Same", body="Body"),  # Duplicate
            Post(userId=1, id=3, title="Same", body="Body"),  # Duplicate
        ]

        anomalies = self.detector.detect_anomalies(posts)

        # Should detect: 3 short titles + 2 duplicates = 5 total
        assert len(anomalies) == 5
        reasons = [a.reason for a in anomalies]
        assert "short_title" in reasons
        assert "duplicate_title" in reasons
