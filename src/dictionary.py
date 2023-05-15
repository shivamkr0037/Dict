from PyDictionary import PyDictionary

dictionary = PyDictionary()

def define_word(word):

    definition = dictionary.meaning(word)

    if definition:

        output = ''

        for key, value in definition.items():

            output += f"{key}: {', '.join(value)}\n"

        return output.strip()

    return "No definition found."

def find_synonyms(word):

    synonyms = dictionary.synonym(word)

    if synonyms:

        return synonyms

    return ["No synonyms found."]

def find_antonyms(word):

    antonyms = dictionary.antonym(word)

    if antonyms:

        return antonyms

    return ["No antonyms found."]
