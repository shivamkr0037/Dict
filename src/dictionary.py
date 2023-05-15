from nltk.corpus import wordnet

def define_word(word):
    synsets = wordnet.synsets(word)
    if synsets:
        return ', '.join([syn.definition() for syn in synsets])
    return "No definition found."

def find_synonyms(word):
    synsets = wordnet.synsets(word)
    synonyms = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    if synonyms:
        return list(synonyms)
    return ["No synonyms found."]

def find_antonyms(word):
    synsets = wordnet.synsets(word)
    antonyms = set()
    for synset in synsets:
        for lemma in synset.lemmas():
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    if antonyms:
        return list(antonyms)
    return ["No antonyms found."]
