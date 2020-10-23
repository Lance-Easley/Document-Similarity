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
    text_1 = file1.readlines()[0]
with open('Text_2.txt') as file2:
    text_2 = file2.readlines()[0]

# Normalize text file strings
text_1 = replace_ch(text_1, [',', '.', '?', '!', ';', ':'], '')
text_2 = replace_ch(text_2, [',', '.', '?', '!', ';', ':'], '')
text_1 = text_1.replace('\n', ' ')
text_2 = text_2.replace('\n', ' ')
case_text1 = text_1.lower()
case_text2 = text_2.lower()

words_1 = text_1.split(' ')
words_2 = text_2.split(' ')
case_1 = case_text1.split(' ')
case_2 = case_text2.split(' ')

levenshtein_scores = []
# word_and_place_scores = []
words_in_texts_scores = []
len_words_score = 0
cased_scores = []
similarity = 0

# Use Levenshtein Distance on all words in texts
for character_1, character_2 in zip(words_1, words_2):
    score = levenshtein_func.leven_distance(character_1, character_2)
    if score > 0:
        levenshtein_scores.append(0)
    else:
        levenshtein_scores.append(1)

        # Compare the capitalization of words if the words are the same when lowercased
        for character_1, character_2 in zip(case_1, case_2):
            score = levenshtein_func.leven_distance(character_1, character_2)
            if score > 0:
                cased_scores.append(0)
            else:
                cased_scores.append(1)

# Calculate score
case_score = sum(cased_scores) / len(cased_scores)
leven_score = sum(levenshtein_scores) / len(levenshtein_scores)

# # Compare words and their order
# for character_1, character_2 in zip(words_1, words_2):
#     if character_1 == character_2:
#         word_and_place_scores.append(1)
#     else:
#         word_and_place_scores.append(0)
# # Calculate score
# order_score = sum(word_and_place_scores) / len(word_and_place_scores)

# Compare words without their order
for character_1 in words_1:
    if character_1 in words_2:
        words_in_texts_scores.append(1)
    else:
        words_in_texts_scores.append(0)
# Calculate score
unordered_score = sum(words_in_texts_scores) / len(words_in_texts_scores)

# Compare the lengths of the documents
if len(words_1) > 0 and len(words_2) > 0:
    if len(words_1) / len(words_2) <= 1.0:
        len_words_score = len(words_1) / len(words_2)
    else:
        len_words_score = len(words_2) / len(words_1)
else:
    len_words_score = (leven_score + unordered_score) / 2

# Calculate total score
similarity = round((leven_score + case_score + unordered_score + len_words_score) / 4, 5)



print(similarity)