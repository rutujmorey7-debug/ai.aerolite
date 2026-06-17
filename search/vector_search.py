import json
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("all-MiniLM-L6-v2")

VECTOR_FILE = "memory/vector_store.json"


def cosine(a, b):

    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def search_trained(query):

    try:
        with open(VECTOR_FILE, "r") as f:
            data = json.load(f)

    except:
        return None

    q = MODEL.encode(query).tolist()

    best = None
    best_score = -1

    for item in data:

        score = cosine(q, item["vector"])

        if score > best_score:
            best_score = score
            best = item["text"]

    if not best:
        return None

    return {
        "text": best,
        "source": "trained"
  }
