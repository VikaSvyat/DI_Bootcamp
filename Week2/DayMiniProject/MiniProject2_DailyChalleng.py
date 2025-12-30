#Write a Python program that takes a single string of words as input, where the words are separated 
# by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical 
# order, with the sorted words also separated by commas.

# string = input("Enter a list of words separated by commas: ")
string = "without,hello,bag,world"
words = string.split(',')
words.sort()
sorted_string = ','.join(words)
print("Sorted words:", sorted_string)   

#Write a function that takes a sentence as input and returns the longest word in the sentence. 
#If there are multiple longest words, return the first one encountered. 
# Characters like apostrophes, commas, and periods should be considered part of the word.
def longest_word(sentence):
    words = sentence.split()
    longest = '' 
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
# string = input("Enter a sentence: ")
# print(longest_word(string))
print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever."))  
print(longest_word("Forgetfulness is by all means powerless!"))