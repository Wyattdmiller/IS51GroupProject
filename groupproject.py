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