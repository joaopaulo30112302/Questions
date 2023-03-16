word = "teste"
wordLength = len(word)
reverseWord = []
for x in range(wordLength):
    reverseWord.append(word[wordLength-1])
    wordLength = wordLength - 1
reverseWord = "".join(reverseWord)
print(reverseWord)