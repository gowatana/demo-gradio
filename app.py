import openai
import os
import gradio as gr

aoai_instance = "demo-aoia-01"
deployment_id = "gpt35-tarbo-01"

openai.api_type = "azure"
openai.api_version = "2023-07-01-preview"
openai.api_base = "https://" + aoai_instance + ".openai.azure.com/"
#openai.api_base = "https://demo-aoia-01.openai.azure.com/"
openai.api_key = os.getenv("OPENAI_API_KEY")

# テキスト生成
def generate_text(prompt):
    message_text = [
      {"role":"system","content":"可能な限り、VMwareに関連する用語として回答します。40文字以内で回答します。「Private AI」については、VMware Private AIを指すものとして説明します。"},
      {"role":"user","content": prompt}
    ]
    response = openai.ChatCompletion.create(
      engine = deployment_id,
      messages = message_text,
      temperature=0.7,
      max_tokens=200,
      top_p=0.95,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None
    )

    # 応答メッセージのcontentを取得
    text = response['choices'][0]['message']['content'].strip()
    return text

# Gradioインターフェイスの設定
iface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=3, placeholder="なにか入力してください..."),
    outputs="text",
    #allow_flagging='never',
    title="Azure OpenAI Gen-AI Demo"
)

# Gradioを起動
iface.launch(server_name="0.0.0.0")

