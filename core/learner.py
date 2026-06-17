import json
import os

WEIGHTS_FILE = "memory/weights.json"
FEEDBACK_FILE = "memory/feedback.json"


def store_feedback(q, a, rating):

    data = []

    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "r") as f:
            data = json.load(f)

    data.append({
        "question": q,
        "answer": a,
        "rating": rating
    })

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(data, f, indent=4)
