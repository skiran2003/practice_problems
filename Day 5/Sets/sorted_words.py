word = 'Hello world! Hello Python. Welcome to the world of Python.'
punctuations='!@#$%^&*()_-,."'
l1=[]
s1=''
for i in word:
    if i not in punctuations:
        s1+=i
s1 = s1.lower()
words=s1.split()
unique_words=set(words)
print(sorted(unique_words))
