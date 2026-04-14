#text="car"
#reverse=""
#for char in text:
#    text2=char+reverse
#    reverse=text2
#print(text2)
text=input("enter the name of the text")
reverse=text[0:3][::-1]
print(reverse)