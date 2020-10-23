# Document Similarity
This project takes two .txt files and ranks them in similarity from a scale of 0.0 - 1.0.
Ranking is based on three categories.

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

# Overall Score
The final score is calculated by taking the average of all ranking methods, and rounding it to five decimal places.

### Licence
MIT
