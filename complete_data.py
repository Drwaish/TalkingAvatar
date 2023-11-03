import os
import openai
from text_to_audio import text_to_audio
from inference import audio2head

openai.api_key = os.getenv('OPENAI_API_KEY') # When not running on colab 
def question_answer(messages):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response['choices'][0]['message']['content']

def complete_data(my_text):
    # messages[1]['content'] = text
    # my_text = question_answer(messages)
    print(my_text)
    if my_text is not None:
        check = text_to_audio(my_text)
        if check:
          os.system("rm -rf results/image_input.mp4")  # if file already exist , delete this file
          audio2head("audio/input.wav", "avatar/image.jpg" , "checkpoints/audio2head.pth.tar","results")
          # var = subprocess.call("python inference.py --audio_path audio/input.wav --img_path avatar/image.jpg", shell = True)
          return "results/image_input.mp4"