import os
from typing import Optional, List, Dict, Any, Iterator
from openai import OpenAI


class ChatGPT:
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key must be provided either as an argument or "
                "via the OPENAI_API_KEY environment variable"
            )

        self.model = model
        self.client = OpenAI(api_key=self.api_key)
        self.conversation_history: List[Dict[str, Any]] = []

    def chat(
        self,
        message: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
    ) -> str:
        if system_prompt and not self.conversation_history:
            self.conversation_history.append(
                {"role": "system", "content": system_prompt}
            )

        self.conversation_history.append({"role": "user", "content": message})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,  # type: ignore
                temperature=temperature,
                max_tokens=max_tokens,
            )

            assistant_message = response.choices[0].message.content
            if assistant_message is None:
                assistant_message = ""

            self.conversation_history.append(
                {"role": "assistant", "content": assistant_message}
            )

            return assistant_message

        except Exception as e:
            self.conversation_history.pop()
            raise Exception(f"Error communicating with OpenAI API: {str(e)}")

    def stream_chat(
        self,
        message: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
    ) -> Iterator[str]:
        if system_prompt and not self.conversation_history:
            self.conversation_history.append(
                {"role": "system", "content": system_prompt}
            )

        self.conversation_history.append({"role": "user", "content": message})

        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,  # type: ignore
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True,
            )

            full_response = ""
            for chunk in stream:  # type: ignore
                if chunk.choices[0].delta.content is not None:  # type: ignore
                    content = chunk.choices[0].delta.content  # type: ignore
                    full_response += content
                    yield content

            self.conversation_history.append(
                {"role": "assistant", "content": full_response}
            )

        except Exception as e:
            self.conversation_history.pop()
            raise Exception(f"Error streaming from OpenAI API: {str(e)}")

    def reset_conversation(self) -> None:
        self.conversation_history = []

    def get_conversation_history(self) -> List[Dict[str, Any]]:
        return self.conversation_history.copy()

    def set_model(self, model: str) -> None:
        self.model = model
