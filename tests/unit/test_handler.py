import json
import pytest
from unittest.mock import patch

from resume_function import app

@patch('resume_function.app.table')
def test_counter_increment_logic(mock_table):
    """Test the core business logic: counter increment"""
    mock_table.get_item.return_value = {'Item': {'Counter': '5'}}
    mock_table.put_item.return_value = {}

    result = app.lambda_handler({}, "")

    # Verify: Counter should be incremented to 6
    body = json.loads(result["body"])
    assert body["Counter"] == "6"

    # Verify: Correct DynamoDB calls were made
    mock_table.get_item.assert_called_once_with(Key={'ID': 'Visits'})
    mock_table.put_item.assert_called_once_with(Item={'ID': 'Visits', 'Counter': '6'})

@patch('resume_function.app.table')
def test_response_format(mock_table):
    """Test Lambda response format"""
    mock_table.get_item.return_value = {'Item': {'Counter': '10'}}
    mock_table.put_item.return_value = {}
 
    result = app.lambda_handler({}, "")
  
    # Test response structure
    assert result["statusCode"] == 200
    assert result["headers"]["Access-Control-Allow-Origin"] == "*"
    assert result["headers"]["Content-Type"] == "application/json"

    # Test body content
    body = json.loads(result["body"])
    assert "Counter" in body
    assert body["Counter"] == "11"
