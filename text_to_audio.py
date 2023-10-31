""" Text to audio using gtts"""
from gtts import gTTS 


def text_to_audio(mytext : str)->bool:
    """
    Convert text to audio.

    Parameters
    ----------
    mytext
        String converted into audio
    
    Retrun 
    ------
    bool
    
    """
    try:
        # Language in which you want to convert 
        language = 'en'

        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed 
        myobj = gTTS(text=mytext, lang=language, slow=False) 

        # Saving the converted audio in a mp3 file named 
        # welcome 
        myobj.save("audio/input.wav") 
        return True
    except FileNotFoundError as error:
        print("Error text to audio", error)
        return False
