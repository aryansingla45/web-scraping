import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    return text

def count_syllables(word):
    vowels = 'aeiouy'
    word = word.lower()
    syllables = 0
    if word[0] in vowels:
        syllables += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllables += 1
    if word.endswith('e'):
        syllables -= 1
    if syllables == 0:
        syllables += 1
    return syllables

def count_personal_pronouns(text):
    pronouns = ['i', 'we', 'my', 'ours', 'us']
    words = text.split()
    count = sum(1 for word in words if word in pronouns)
    return count
