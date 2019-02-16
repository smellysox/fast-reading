import time
from kivy.properties import StringProperty
x = StringProperty
text_file = open("example.txt","r")
for word in text_file.read().split():
        print(word)
print(x)
text_file.close()