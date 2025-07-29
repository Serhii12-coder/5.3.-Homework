import string

text = "Алекс, привіт&"

words = text.split()
text = [word.capitalize() for word in words]
text2 = "".join(text)
#print(text2)

cleaned = "".join([char for char in text2 if char not in string.punctuation])
#print(cleaned)

my_string = f"#{cleaned}"
print(my_string)
