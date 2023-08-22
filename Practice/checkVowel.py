ch=input("Enter a character: ")
ch.lower()
# if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
vowel = ['a', 'e', 'i', 'o', 'u']
for i in ch:
    if(i.lower() in vowel):
        print(ch, "contains vowel")
        break
    else:
        print(ch, "does not contains vowel")
        break

    