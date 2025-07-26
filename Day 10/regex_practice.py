import re

# Regular expressions are only used to check patterns in Strings(Does not work on other data types)
text="Python regular expressions"
a=re.search("python",text,re.IGNORECASE) 
# Returns the index of the given word found in the String - IGNORECASE(ignores the case of the word to be found)
print(a)

a=re.split("\s",text)  
# Splits the given sentence (\s represents whitespace)
a=re.split("\s",text,1) 
# Splits the given sentence upto specified number of word and returns rest of the sentence as a single string
print(a)

a=re.findall("expressions",text) 
# Returns the matching word from the given text. Returns empty list if no match found
print(a)

a=re.findall("[a-z]",text) 
# Returns all the lowercase characters from the given text
a=re.match("^[0-9]+$","45954") 
# ^[0-9]+$ ---> ^ = starts with, [0-9] = Range of numbers between 0-9, + = Contain more than 1 of the characters

a=re.sub("\s",'-',text) 
# Replaces the whitespaces with the given character
print(a)

# Returns the characters if the given words are at the beginning of the string 
a=re.findall("\APyt",text)
print(a)

# Finds one or more occurences of a character
s=re.findall("s+",text)
print(s)

c=re.compile(r"[\d]{2}") # Pattern is compiled once and can be reused with the variable name
b=re.search(c,"2258")
print(b)
