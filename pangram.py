def is_pangram(sentence):
    sentence = sentence.lower()
    unique_letters = set()
    for char in sentence:
        if char.isalpha():
            unique_letters.add(char)
    return len(unique_letters) == 26  # 26 letters in the English alphabet
sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
