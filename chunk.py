from chonkie import SemanticChunker
from autotiktokenizer import AutoTikTokenizer
from llama_index.core.text_splitter import SentenceSplitter
from llama_index.core import SimpleDirectoryReader

# initialize tokenizer
tokenizer = AutoTikTokenizer.from_pretrained("gpt2")

# create chunker

chunker = SemanticChunker(
    tokenizer=tokenizer,
    initial_sentences=5,
    embedding_model="all-minilm-l6-v2",
    max_chunk_size=2512,
    sentence_mode="spacy",
    similarity_threshold=0.4
)

# chunk your text

file = open("sample.txt", 'r')
text = file.read()

chunks = chunker.chunk(text)

# access chunks
print(len(chunks))
for chunk in chunks:
    print(f"chunk: {chunk.text[:50]}...")
    print(f"tokens: {chunk.token_count}")
