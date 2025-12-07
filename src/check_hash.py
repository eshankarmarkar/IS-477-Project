import hashlib
from pathlib import Path

def sha256sum(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(8192), b""):
            h.update(block)
    return h.hexdigest()

if __name__ == "__main__":
    file_path = Path("data/raw/incomedata.csv")
    print("SHA-256:", sha256sum(file_path))
