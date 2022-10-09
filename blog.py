import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="",
  temperature=0.7,
  max_tokens=25,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)