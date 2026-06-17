import json
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("all-MiniLM-L6-v2")

VECTOR_FILE = "memory/vector_store.json"


def train_txt():

    with open("knowledge/data.txt", "r", encoding="utf-8") as f:
        data = f.readlines()

    vectors = []

    for line in data:

        line = line.strip()

        if not line:
            continue

        vec = MODEL.encode(line).tolist()

        vectors.append({
            "text": line,
            "vector": vec
        })

    with open(VECTOR_FILE, "w") as f:
        json.dump(vectors, f, indent=4)

    return len(vectors)
