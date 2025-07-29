import os
from app.config import Settings, load_config


class TestSettings:
    def test_default_settings(self):
        """Test default settings values"""
        settings = Settings()
        assert settings.server_port == 8000
        assert settings.server_host == "0.0.0.0"
        assert settings.log_level == "INFO"

    def test_custom_settings(self):
        """Test custom settings values"""
        settings = Settings(
            server_port=9000, server_host="127.0.0.1", log_level="DEBUG"
        )
        assert settings.server_port == 9000
        assert settings.server_host == "127.0.0.1"
        assert settings.log_level == "DEBUG"


class TestLoadConfig:
    def test_load_config_defaults(self):
        """Test loading config with default values"""
        # Clear any existing environment variables
        env_vars = ["SERVER_PORT", "SERVER_HOST", "LOG_LEVEL"]
        original_values = {}

        for var in env_vars:
            original_values[var] = os.getenv(var)
            if var in os.environ:
                del os.environ[var]

        try:
            settings = load_config()
            assert settings.server_port == 8000
            assert settings.server_host == "0.0.0.0"
            assert settings.log_level == "INFO"
        finally:
            # Restore original environment variables
            for var, value in original_values.items():
                if value is not None:
                    os.environ[var] = value

    def test_load_config_with_env_vars(self):
        """Test loading config with environment variables"""
        # Set environment variables
        os.environ["SERVER_PORT"] = "9000"
        os.environ["SERVER_HOST"] = "127.0.0.1"
        os.environ["LOG_LEVEL"] = "DEBUG"

        try:
            settings = load_config()
            assert settings.server_port == 9000
            assert settings.server_host == "127.0.0.1"
            assert settings.log_level == "DEBUG"
        finally:
            # Clean up environment variables
            for var in ["SERVER_PORT", "SERVER_HOST", "LOG_LEVEL"]:
                if var in os.environ:
                    del os.environ[var]

    def test_load_config_invalid_port(self):
        """Test loading config with invalid port"""
        os.environ["SERVER_PORT"] = "invalid"

        try:
            settings = load_config()
            # Should fall back to default
            assert settings.server_port == 8000
        finally:
            if "SERVER_PORT" in os.environ:
                del os.environ["SERVER_PORT"]

    def test_load_config_invalid_log_level(self):
        """Test loading config with invalid log level"""
        os.environ["LOG_LEVEL"] = "INVALID"

        try:
            settings = load_config()
            # Should fall back to default
            assert settings.log_level == "INFO"
        finally:
            if "LOG_LEVEL" in os.environ:
                del os.environ["LOG_LEVEL"]
