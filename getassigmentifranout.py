import os
import random
import string

TARGET_BYTES = 3 * 1024 * 1024      # 3 MB
CHUNK = 1024 * 1024                 # 1 MB

alphabet = string.ascii_letters

def make_chunk(n):
    return ''.join(random.choice(alphabet) for _ in range(n)).encode()
def write_3mb(id):
    with open(f"three_mb.txt{id}", "wb") as f:
        written = 0
        while written < TARGET_BYTES:
            size = min(CHUNK, TARGET_BYTES - written)
            f.write(make_chunk(size))
            written += size
id=1
while True:
    write_3mb(id)
    id+=1
    print(f"wrote {3*id} mb")

