s1 = "hello world"
print(s1)
print(s1[0], s1[1], s1[2])
print(s1[4], s1[7])
#print(s1[11], s1[-1])
print(s1[-2])

#if operations
if "bob":
    print("bob is")

else:
    print("bob isn't")

if "":
    print("empty string is true")

else:
    print("empty string is false")



s = "abcdefghijklmnñop"
print(len(s))
#we can iterate over a string

for character in s:
    print(character, end=" ")


i = 0 #the begining of index
while i < len(s):
    print(s[i], end=" ")
    i += 1


i = 0 #the begining of index
while i < len(s):
    print(s[len(s) - i - 1], end=" ")
    i += 1

# :4 = the first 4 leters, 4: = all leters after first 4

n = "0123456789"
print(n)
print(n[2:3])
print(n[4:6])
print(n[:3])
print(n[3:])
print(n[1:7:2])
print(n[::3])
print(n[::-1])
print(n[::-2])

