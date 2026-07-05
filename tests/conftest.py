"""Test configuration for Fraud Detection Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "fraud-detection-agent", "category": "Finance"}
