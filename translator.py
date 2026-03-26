from googletrans import translator
x=translator()
text1=input("enter the sentence:")
text2=input("enter targeted language:")
rest=x.translate(text1,dest=text2)
print("the original:",text1)
print("tranlate:",rest)
