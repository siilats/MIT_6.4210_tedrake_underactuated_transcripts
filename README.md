
```
# newest youtube-dl
git clone https://github.com/ytdl-org/youtube-dl.git
cd youtube-dl
pip install -e .
# if that doesnt work download 
./yt-dlp_macos -x https://www.youtube.com/watch?v=cXvMRJazMyM
# you can use playlist url
# download audio only
youtube-dl -x https://www.youtube.com/watch?v=UbqUYnYQY0M
# convert to wav
parallel "ffmpeg -i {1} -ac 2 -ar 16000 {1.}.wav" ::: *.m4a 
ffmpeg -i vaba.opus  -ar 16000 vaba.wav
# decode
../whisper.cpp/main -t 7 -otxt -osrt -m ../whisper.cpp/models/ggml-large-v3-turbo-q5_0.bin -f *.wav
```
for embeddings
```
wget https://huggingface.co/Mozilla/Llama-3.2-3B-Instruct-llamafile/resolve/main/Llama-3.2-3B-Instruct.Q6_K.llamafile --show-progress
chmod +x Llama-3.2-3B-Instruct.Q6_K.llamafile
wget -nv -nc https://huggingface.co/jartine/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile --show-progress
chmod +x TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile
# Alternatively, you can just open a separate terminal outside this notebook and run: 
./TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile --server --nobrowser --embedding
```

