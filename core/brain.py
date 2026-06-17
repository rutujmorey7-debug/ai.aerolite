from search.vector_search import search_trained
from search.wikipedia_search import search_wikipedia


def detect_intent(text):

    t = text.lower()

    if "code" in t:
        return "code"

    if "what" in t or "who" in t:
        return "knowledge"

    if "how" in t:
        return "thinking"

    return "general"


def brain(user_input, config):

    mode = config["mode"]

    result = None

    # 1. Try trained memory
    result = search_trained(user_input)

    # 2. Wikipedia fallback
    if not result:
        result = search_wikipedia(user_input)

    # 3. Final fallback
    if not result:
        result = {
            "text": "I couldn't find an answer.",
            "source": "system"
        }

    # Mode styling
    if mode == "code":
        result["text"] = "💻 Code Mode:\n\n" + result["text"]

    elif mode == "thinking":
        result["text"] = "🧠 Thinking Mode:\n\n" + result["text"]

    else:
        result["text"] = "🤖 AeroLite:\n\n" + result["text"]

    return result
