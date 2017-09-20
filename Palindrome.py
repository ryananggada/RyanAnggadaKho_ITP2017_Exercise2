word=input("Enter word: ")
word=word.lower()
rev_word=word[::-1]
if (rev_word==word):
    print("It is a palindrome word.")
else:
    print("It is not a palindrome word.")
