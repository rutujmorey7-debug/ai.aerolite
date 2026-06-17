import wikipedia

def search_wikipedia(query):

    try:
        result = wikipedia.summary(query, sentences=3)
        return {
            "text": result,
            "source": "wiki"
        }

    except:
        return None