import pytest
import os
from unittest.mock import Mock, patch, MagicMock
from chatgpt import ChatGPT


class TestChatGPT:
    def test_init_with_api_key(self):
        client = ChatGPT(api_key="test-key")
        assert client.api_key == "test-key"
        assert client.model == "gpt-3.5-turbo"
    
    def test_init_without_api_key_raises_error(self):
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError):
                ChatGPT()
    
    def test_init_with_env_variable(self):
        with patch.dict(os.environ, {"OPENAI_API_KEY": "env-key"}):
            client = ChatGPT()
            assert client.api_key == "env-key"
    
    def test_init_with_custom_model(self):
        client = ChatGPT(api_key="test-key", model="gpt-4")
        assert client.model == "gpt-4"
    
    @patch('chatgpt.client.OpenAI')
    def test_chat(self, mock_openai):
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Hello! I'm doing well."
        
        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        client = ChatGPT(api_key="test-key")
        response = client.chat("How are you?")
        
        assert response == "Hello! I'm doing well."
        assert len(client.conversation_history) == 2
        assert client.conversation_history[0]["role"] == "user"
        assert client.conversation_history[1]["role"] == "assistant"
    
    @patch('chatgpt.client.OpenAI')
    def test_chat_with_system_prompt(self, mock_openai):
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "I am a helpful assistant."
        
        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        client = ChatGPT(api_key="test-key")
        response = client.chat("Hello", system_prompt="You are a helpful assistant")
        
        assert len(client.conversation_history) == 3
        assert client.conversation_history[0]["role"] == "system"
        assert client.conversation_history[0]["content"] == "You are a helpful assistant"
    
    @patch('chatgpt.client.OpenAI')
    def test_reset_conversation(self, mock_openai):
        mock_openai.return_value = Mock()
        
        client = ChatGPT(api_key="test-key")
        client.conversation_history = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
        
        client.reset_conversation()
        assert len(client.conversation_history) == 0
    
    @patch('chatgpt.client.OpenAI')
    def test_get_conversation_history(self, mock_openai):
        mock_openai.return_value = Mock()
        
        client = ChatGPT(api_key="test-key")
        client.conversation_history = [
            {"role": "user", "content": "Hello"}
        ]
        
        history = client.get_conversation_history()
        assert history == client.conversation_history
        assert history is not client.conversation_history
    
    @patch('chatgpt.client.OpenAI')
    def test_set_model(self, mock_openai):
        mock_openai.return_value = Mock()
        
        client = ChatGPT(api_key="test-key")
        assert client.model == "gpt-3.5-turbo"
        
        client.set_model("gpt-4")
        assert client.model == "gpt-4"
    
    @patch('chatgpt.client.OpenAI')
    def test_chat_error_handling(self, mock_openai):
        mock_client = Mock()
        mock_client.chat.completions.create.side_effect = Exception("API Error")
        mock_openai.return_value = mock_client
        
        client = ChatGPT(api_key="test-key")
        
        with pytest.raises(Exception) as exc_info:
            client.chat("Hello")
        
        assert "Error communicating with OpenAI API" in str(exc_info.value)
        assert len(client.conversation_history) == 0
    
    @patch('chatgpt.client.OpenAI')
    def test_stream_chat(self, mock_openai):
        mock_chunk1 = Mock()
        mock_chunk1.choices = [Mock()]
        mock_chunk1.choices[0].delta.content = "Hello"
        
        mock_chunk2 = Mock()
        mock_chunk2.choices = [Mock()]
        mock_chunk2.choices[0].delta.content = " there"
        
        mock_chunk3 = Mock()
        mock_chunk3.choices = [Mock()]
        mock_chunk3.choices[0].delta.content = None
        
        mock_client = Mock()
        mock_client.chat.completions.create.return_value = iter([
            mock_chunk1,
            mock_chunk2,
            mock_chunk3
        ])
        mock_openai.return_value = mock_client
        
        client = ChatGPT(api_key="test-key")
        chunks = list(client.stream_chat("Hi"))
        
        assert chunks == ["Hello", " there"]
        assert len(client.conversation_history) == 2
        assert client.conversation_history[1]["content"] == "Hello there"
