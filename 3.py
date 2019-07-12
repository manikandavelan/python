nr=input()
if(nr=='a' or nr=='e' or nr=='i' or nr=='o' or nr=='u' or nr=='A' or nr=='E' or nr=='I' or nr=='O' or nr=='U'):
    print("Vowel")
elif(nr.isalpha()==False):
    print("invalid")
else:
    print("Consonant")
