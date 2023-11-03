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

OPENAI reply 

<video width="320" height="240" controls>
  <source src="assets/image_input.mp4" type="video/mp4">
</video>


# ----------------------------- OR ---------------------------------------------------
### You can simply run Avatar_chatbot.ipynb.


#### Acknowledgement

This codebase is based on [Audio2head](https://github.com/wangsuzhen/Audio2Head.git), thanks for their contribution.





