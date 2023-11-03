# Chat with Avatar
```bash
git clone https://github.com/Drwaish/TalkingAvatar
cd TalkingAvatar
```
## Install Dependencies

```bash
pip install -r requirements.txt
```
- Python 3.10.12 , Pytorch >= 1.6 and ffmpeg

#### Pretrained Checkpoint
```bash
cd checkpoints
wget https://github.com/Drwaish/TalkingAvatar/releases/download/v1/audio2head.pth.tar
cd ..
```

## Change Avatar
If you want to change the avatar repalce image with desired avatar image in avatar folder.
Note : Keep name same as previous image.
```
avatar
    |---- image.jpg
```
## Example
I ask to openai "How are you?"

OPENAI reply : <h3><b>I am AI Assistant I don't have feelings. How can I assist you today? </b></h3>


Video is in assets.


![Video](assets/image_input.gif)



# ----------------------------- OR ---------------------------------------------------
### You can simply run Avatar_chatbot.ipynb.


#### Acknowledgement

This codebase is based on [Audio2head](https://github.com/wangsuzhen/Audio2Head.git), thanks for their contribution.





