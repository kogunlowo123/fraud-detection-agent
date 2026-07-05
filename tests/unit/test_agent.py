"""Fraud Detection Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_analyze_transaction():
    """Test Analyze a financial transaction for fraud indicators."""
    tools = AgentTools()
    result = await tools.analyze_transaction(transaction="test", account_history="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_calculate_risk_score():
    """Test Calculate fraud risk score using ML models and rules."""
    tools = AgentTools()
    result = await tools.calculate_risk_score(transaction_id="test", features="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_flag_anomaly():
    """Test Flag a suspicious transaction pattern for investigation."""
    tools = AgentTools()
    result = await tools.flag_anomaly(pattern="test", severity="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_manage_investigation():
    """Test Manage fraud investigation workflow and evidence collection."""
    tools = AgentTools()
    result = await tools.manage_investigation(case_id="test", action="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.fraud_detection_agent_agent import FraudDetectionAgentAgent
    agent = FraudDetectionAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
