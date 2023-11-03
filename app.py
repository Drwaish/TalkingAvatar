import gradio as gr
from complete_data import question_answer, complete_data

messages=[
        {
          "role": "system",
          "content": "Answer the message enter by user."
        },
        {
          "role": "user",
        },
      ]
def respond(message, chat_history):
    messages[1]['content'] = message
    my_text = question_answer(messages)
    print(my_text)
    path = complete_data(my_text)
    chat_history.append((message, my_text))
    print("bot_message", path)
    return "", chat_history, path

with gr.Blocks() as demo:
    with gr.Row():
      chatbot = gr.Chatbot()
      with gr.Column():
        msg = gr.Textbox()
        button = gr.Button("Send")
    with gr.Column():
      video = gr.Video(label = "Avatar", autoplay = True)
    # button.click(fn = respond, inputs = [msg, chatbot], outputs = [msg, chatbot, video])
    msg.submit(fn = respond, inputs = [msg, chatbot], outputs = [msg, chatbot, video])
