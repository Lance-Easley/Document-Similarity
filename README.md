# Document Similarity
This project takes two .txt files and ranks them in similarity from a scale of 0.0 - 1.0.
Ranking is based on four categories.

## Words In Order
The first method of ranking is words in order.
The program takes the first word of a document and sees if the other document's first word is the same.
Then, it moves onto the second word of a document and sees if the other document's second word is the same.
Them, the third, the fourth, and so on.
For every matching word pair, the program adds "1" to a list; if they don't match, a "0" is added.
Final score is calculated by averaging this list.

## Words In Text
The second method of ranking is words in text.
The program will take the first word of a document and see if that word appears anywhere in the other document.
If the word appears in the other document, the program adds "1" to a list; if not, a "0" is added.
Final score is calculated by averaging this list.

## Difference in Length
The third method of ranking is the difference in length.
The program will calculate and record the number of words in each document.
Then program will divide the smaller number of words by the largest number of words.
This division produces a value between 0.0 and 1.0, which is the score for this method.

## Capitalization
The fourth method of ranking is the comparison of lettercases.
The program will check to see of the words in lowercase are the same.
If they are the same, it will check to see if there is a difference in capitalization.
If there is a difference, then the total score will be slightly affected.
If the words in lowercase are different, the program will not check for capitalization.

# Levenshtein Distance
The ranking method "Words in Order" works fine. 
However, as described in my Levenshtein Distance repository, I was introduced to Levenshtein Distance and I wanted to implement it.
For more information about creating Levenshtein Distance and what it does, visit my [Levenshtein Distance](https://github.com/Lance-Easley/Levenshtein-Distance) repository.

# Overall Score
The final score is calculated by taking the average of all ranking methods, and rounding it to five decimal places.

### Licence
MIT
