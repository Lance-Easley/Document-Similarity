def replace_ch(string: str, characters: list, replacement: str) -> str:
    """Replaces all intances of characters in a given string with a given 
    replacement character.
    """
    n_string = string
    for ch in characters:
        n_string = n_string.replace(ch, replacement)
    return n_string

with open('Text_1.txt') as file1:
    text_1 = file1.readlines()[0]
with open('Text_2.txt') as file2:
    text_2 = file2.readlines()[0]

# Normalize text file strings
text_1 = replace_ch(text_1, [',', '.', '?', '!', ';', ':'], '')
text_2 = replace_ch(text_2, [',', '.', '?', '!', ';', ':'], '')
text_1 = text_1.replace('\n', ' ')
text_2 = text_2.replace('\n', ' ')

words_1 = text_1.split(' ')
words_2 = text_2.split(' ')

word_and_place_score = []
words_in_texts_score = []

# Compare words and their order
for character_1, character_2 in zip(words_1, words_2):
    if character_1 == character_2:
        word_and_place_score.append(1)
    else:
        word_and_place_score.append(0)

# Compare words without their order
for character_1 in words_1:
    if character_1 in words_2:
        words_in_texts_score.append(1)
    else:
        words_in_texts_score.append(0)

# Calculate similarity score
similarity = 0
order_score = sum(word_and_place_score) / len(word_and_place_score)
unordered_score = sum(words_in_texts_score) / len(words_in_texts_score)
similarity = (order_score + unordered_score) / 2

print(similarity)