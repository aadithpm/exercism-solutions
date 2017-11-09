from re import sub

def is_pangram(sentence):
    if sentence == "":
        return False
    sentence = sub(r"[^A-Za-z]", "", sentence.lower())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return not(set(alphabet) != set(sentence))
