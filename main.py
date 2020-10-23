import levenshtein_func

# Levenshtein Distance in this context performs the same as "Words in Order".
# Words in Order code is commented for reference, and Levenshtein is in it's 
# place.

def replace_ch(string: str, characters: list, replacement: str) -> str:
    """Replaces all intances of characters in a given string with a given 
    replacement character.
    """
    n_string = string
    for ch in characters:
        n_string = n_string.replace(ch, replacement)
    return n_string

with open('Text_1.txt') as file1:
    text_1 = file1.readlines()[0].lower()
with open('Text_2.txt') as file2:
    text_2 = file2.readlines()[0].lower()

# Normalize text file strings
text_1 = replace_ch(text_1, [',', '.', '?', '!', ';', ':'], '')
text_2 = replace_ch(text_2, [',', '.', '?', '!', ';', ':'], '')
text_1 = text_1.replace('\n', ' ')
text_2 = text_2.replace('\n', ' ')

words_1 = text_1.split(' ')
words_2 = text_2.split(' ')

levenshtein_score = []
# word_and_place_score = []
words_in_texts_score = []
len_words_score = 0
similarity = 0

# Use Levenshtein Distance on all words in texts
for character_1, character_2 in zip(words_1, words_2):
    score = levenshtein_func.leven_distance(character_1, character_2)
    if score > 0:
        levenshtein_score.append(0)
    else:
        levenshtein_score.append(1)
# Calculate score
leven_score = sum(levenshtein_score) / len(levenshtein_score)

# # Compare words and their order
# for character_1, character_2 in zip(words_1, words_2):
#     if character_1 == character_2:
#         word_and_place_score.append(1)
#     else:
#         word_and_place_score.append(0)
# # Calculate score
# order_score = sum(word_and_place_score) / len(word_and_place_score)

# Compare words without their order
for character_1 in words_1:
    if character_1 in words_2:
        words_in_texts_score.append(1)
    else:
        words_in_texts_score.append(0)
# Calculate score
unordered_score = sum(words_in_texts_score) / len(words_in_texts_score)

# Compare the lengths of the documents
if len(words_1) > 0 and len(words_2) > 0:
    if len(words_1) / len(words_2) <= 1.0:
        len_words_score = len(words_1) / len(words_2)
    else:
        len_words_score = len(words_2) / len(words_1)
else:
    len_words_score = (leven_score + unordered_score) / 2

# Calculate total score
similarity = round((leven_score + unordered_score + len_words_score) / 3, 5)



print(similarity)