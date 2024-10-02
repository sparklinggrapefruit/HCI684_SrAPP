import openai

from openai.types import Completion, CompletionChoice, CompletionUsage
from openai.types import ChatModel

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionChunk,
    ChatCompletionContentPartParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionContentPartRefusalParam,
    ChatCompletionContentPartTextParam,
    ChatCompletionFunctionCallOptionParam,
    ChatCompletionFunctionMessageParam,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCall,
    ChatCompletionNamedToolChoiceParam,
    ChatCompletionRole,
    ChatCompletionStreamOptionsParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionTokenLogprob,
    ChatCompletionToolParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
)

import os
from openai import OpenAI

client = openai.Client(api_key="your-api-key")

# Create a chat completion using the client
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test"
        }
    ]
)

# Print the response from the assistant
print(response['choices'][0]['message']['content'])