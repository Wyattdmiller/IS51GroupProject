""" Structured English
This program takes user input and displays information about the words 
and letters of the input. It starts by taking the user input, prompted by
"Please enter a sentence you'd like to know more about." Then the sentence
is split into one list of the words in the input, and a second list of the 
letters in the input. 

A loop will determine the length of each word in the input, and add it to 
a variable in order to determine the total number of letters in the input.
The number of letters will be divided by the number of words to determine
the average word length. Then the number of words in the input, and the
average length of the words will be displayed to the user, as in:
"Your sentence has (#) words in it." 
and "The words are an average of (#) letters long."

Then, a loop will go through a list of all the letters in the alphabet
and compare them with the user input to determine which letters of the 
alphabet are used and which are not. Those which are used are put in one
list, and those that are not are put in a second list. 

If the length of the missing-letters-list is 0, then it will print
"Your sentence uses every letter of the alphabet!"
Otherwise if the missing-letters-list is smaller than the letters-used
list, it will print "Your sentence is missing (#) letters. They are:
(missing-letters-list)"
Otherwise if the letters-used list is smaller, it will print
"Your sentence uses (#) letters of the alphabet. They are:
(letters-used)"
"""

""" Pseudocode
alphabet = ['a' 'b' 'c' 'd' ... 'z']
totalLengths = 0
wordLength = 0
used = []
missing = []
sentence = input("Enter a sentence that you would like to know more about")
wordList = sentence words
letterList = sentence letters

for word in wordList
  wordLength = len(word)
  totalLengths += wordLength
avg = totalLengths / len(wordList)

print("Your sentence has len(wordList) words in it")
print("The words are an average of avg letters long")

for letter in alphabet:
  if sentence contains (letter):
    append letter to used
  else:
    append letter to missing

if len(missing) == 0:
  print("Your sentence uses every letter of the alphabet!")
elif len(missing) < len(used):
  print("Your sentence is missing len(missing) letters of the alphabet. They are:")
  print(missing)
else:
  print("Your sentence uses len(used) letters of the alphanet. They are:")
  print(used)
"""

def main():
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  totalLengths = 0
  wordLength = 0
  used = []
  missing = []
  sentence = input("Enter a sentence that you would like to know more about. ")
  sentence = sentence.lower()
  wordList = sentence.split()
  letterList = list(sentence)

  avg(wordList, totalLengths)
  letters(alphabet, sentence, used, missing)

def avg(wordList, totalLengths):
  for word in wordList:
    wordLength = (len(word))
    totalLengths += wordLength
  avgWordLength = round(totalLengths / (len(wordList)), 2)
  print(f"Your sentence has {len(wordList)} words in it.")
  print(f"The words are an average of {avgWordLength} letters long.")

def letters(alphabet, sentence, used, missing):
  for letter in alphabet:
    if sentence.__contains__(letter):
      used.append(letter)
    else:
      missing.append(letter)
    
  if len(missing) == 0:
    print("Your sentence uses every letter of the alphabet!")
  elif len(missing) < len(used):
    print(f"Your sentence is missing {len(missing)} letters of the alphabet. They are:")
    print(missing)
  else:
    print(f"Your sentence uses {len(used)} letters of the alphabet. They are:")
    print(used)

main()