
```
# newest youtube-dl
git clone https://github.com/ytdl-org/youtube-dl.git
cd youtube-dl
pip install -e .
# you can use playlist url
# download audio only
youtube-dl -x https://www.youtube.com/watch?v=UbqUYnYQY0M
# convert to wav
parallel "ffmpeg -i {1} -ar 16000 {1.}.wav" ::: *.m4a 
# decode
../../whisper.cpp/main -t 7 -otxt -osrt -m ../../whisper.cpp/models/ggml-large.bin -f *.wav
```
