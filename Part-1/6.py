def count_word(sentence):
    words = sentence.split()
    return len(words)

scan = input("Enter a sentence: ")
word_count = count_word(scan)
print(f"The number of words is:{word_count}")