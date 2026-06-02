import os
import random
import string

TARGET_BYTES = 1 * 1024 * 1024 * 1024   # 1 GB
CHUNK_SIZE = 1024 * 1024               # 1 MB per write

alphabet = string.ascii_lowercase + string.ascii_uppercase

def make_chunk(n):
    return ''.join(random.choice(alphabet) for _ in range(n)).encode()

with open("gibberish_1GB.txt", "wb") as f:
    written = 0
    while written < TARGET_BYTES:
        chunk = make_chunk(CHUNK_SIZE)
        f.write(chunk)
        written += len(chunk)

print("Done: wrote 1 GB of gibberish.")
