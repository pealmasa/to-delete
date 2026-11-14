"""Tests for app.core.config — SecretStr and StrEnum validation."""

import pytest
from pydantic import SecretStr

from app.core.config import Environment, Settings


class TestEnvironmentEnum:
    """Test Environment StrEnum."""

    def test_values(self) -> None:
        assert Environment.DEVELOPMENT.value == "development"
        assert Environment.TESTING.value == "test"
        assert Environment.STAGING.value == "staging"
        assert Environment.PRODUCTION.value == "production"

    def test_is_str(self) -> None:
        assert isinstance(Environment.DEVELOPMENT, str)


class TestSettingsSecretStr:
    """Test that credentials use SecretStr."""

    def test_secret_key_is_secretstr(self) -> None:
        s = Settings(secret_key="my-secret", database_url="postgresql://x")
        assert isinstance(s.secret_key, SecretStr)
        assert s.secret_key.get_secret_value() == "my-secret"

    def test_database_url_is_secretstr(self) -> None:
        s = Settings(database_url="postgresql://user:pass@localhost/db")
        assert isinstance(s.database_url, SecretStr)
        assert (
            s.database_url.get_secret_value() == "postgresql://user:pass@localhost/db"
        )

    def test_secret_key_not_in_repr(self) -> None:
        s = Settings(secret_key="super-secret-value", database_url="postgresql://x")
        assert "super-secret-value" not in repr(s)

    def test_database_url_not_in_repr(self) -> None:
        s = Settings(database_url="postgresql://user:pass@localhost/db")
        assert "pass" not in repr(s.database_url)

    def test_app_env_default(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("APP_ENV", raising=False)
        s = Settings(database_url="postgresql://x")
        assert s.app_env == Environment.DEVELOPMENT

    def test_app_env_from_string(self) -> None:
        s = Settings(app_env="production", database_url="postgresql://x")
        assert s.app_env == Environment.PRODUCTION
