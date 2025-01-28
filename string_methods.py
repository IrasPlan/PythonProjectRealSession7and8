from string import punctuation

methods = dir("hi")
useful_methods = []
for methods in methods:
    if "__" in methods:
        continue
    useful_methods.append(methods)
print(useful_methods)


print(help("hi".capitalize()))
print("cat".capitalize())
s = "123i go to school every day"
print(s.capitalize())

print(help("".casefold))
print("I LIKE CAKE!!@GMAIL.COM".casefold()) #lowercase everything


print("hello".center(20,"*"))
print("bananananananananannana".count("ana"))

print("ana ana banana".find("ana")) #0 bc the first ana in in position 0
print("ana ana banana".find("ana",5))#after position 5

print("abcdefg".index("b"))

words = ["I", "like", "to", "sing"]
print(" ".join(words))

s = "I like to go hiking"
print(s.replace(" ", "! !"))
#print(s.split())
print(s.replace("!", "").split)

sentence = "how, are you? ain't it."
punctuation = "!.?-/;`',"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)

print("i like to go hiking".title())









