from spellchecker import SpellChecker

# turn off loading a built language dictionary, case sensitive on (if desired)
spell = SpellChecker(language="fr")

# CE SITE CONTIENT QUATRE TOMBEAUX DE LA DYNASTIE ACHÉMÉNIDE ET SEPT DES SASSANIDES.
words = "CE SITE CONTIENT QUATRE TOMBEAUX DE LA DYNASTIE ASHÉMÉNIDE ET SEPT DES SASANNIDES".split()

for word in words:
    word = word.lower()
    if word in spell:
        print(f"'{word}' is spelled correctly!")
    else:
        cor = spell.correction(word)
        print(f"The best spelling for '{word}' is '{cor}'")

        print("If that is not enough; here are all possible candidate words:")
        print(spell.candidates(word))