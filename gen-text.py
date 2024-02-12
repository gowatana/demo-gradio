#Note: This code sample requires openai 0.28.1 or lower.
import os
import openai

aoai_instance = "demo-aoia-01"
deployment_id = "gpt35-tarbo-01"

openai.api_type = "azure"
openai.api_version = "2023-07-01-preview"
openai.api_base = "https://" + aoai_instance + ".openai.azure.com/"
#openai.api_base = "https://demo-aoia-01.openai.azure.com/"
openai.api_key = os.getenv("OPENAI_API_KEY")


prompt = "Private AIは、我々のビジネスにどのような利益をもたらしますか？"

message_text = [
  {"role":"system","content":"可能な限り、VMwareに関連する用語として回答します。40文字以内で回答します。「Private AI」については、VMware Private AIを指すものとして説明します。"},
  {"role":"user","content": prompt}
]

completion = openai.ChatCompletion.create(
  engine="gpt35-tarbo-01",
  messages = message_text,
  temperature=0.7,
  max_tokens=200,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion.choices[0].message.content)
