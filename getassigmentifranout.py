import os
import random
import string
import subprocess

CHUNK_MB = 3
CHUNK_BYTES = CHUNK_MB * 1024 * 1024
alphabet = string.ascii_letters

def make_chunk_str(n):
    return ''.join(random.choice(alphabet) for _ in range(n))

while True:
    # generate gibberish as a string
    chunk_str = make_chunk_str(CHUNK_BYTES)
    chunk_bytes = chunk_str.encode()

    # filename = first 100 characters, sanitized
    raw_name = chunk_str[:100]
    safe_name = "".join(c for c in raw_name if c.isalnum())
    if not safe_name:
        safe_name = "emptyname"
    name = safe_name + ".txt"

    print(f"Generating {name} ({CHUNK_MB} MB)")

    # write file
    with open(name, "wb") as f:
        f.write(chunk_bytes)

    # git add / commit / push
    subprocess.run(["git", "add", name])
    subprocess.run(["git", "commit", "-m", f"Add {name}"])
    subprocess.run(["git", "push"])

    print(f"Pushed {name}, deleting local copy")

    # delete local file
    os.remove(name)
