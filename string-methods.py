text = "awsxdrfvbghnmjk"
print(dir(text))
help(text.isupper)
print(text.isupper())

print(text.upper)
print(text.upper().isupper())

new_text=text.upper()
print(text, new_text)
print("bannannnaa".count("n"))
print("bannnananana".index("ana"))
print("bannabnanaa".replace("ana", "XXYY"))

sentence = "Hello, kind-sir; how may! I be of service today?"
print(sentence.replace(",","").replace(";","").replace("!","").replace("?",""))
#or
punctuation = ".,;!?-"
for p in punctuation:
    sentence = sentence.replace(p,"")
print(sentence)
#the result is still a string

print("this is a sentence and I want the words".split(" "))


text = "Bob goes to school. Bob likes to play tennis. I am friends with Bob. Such a nice guy Bob is"
print(text.find("Bob"))
print(text.rfind("Bob"))
# find all the positions of Bob

i=0
while i<len(text):
    i=text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i+=1
    
