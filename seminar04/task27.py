punctuation_marks = (".", ",", ";", ":", "!", "?", "(", ")", "[", "]", "{", "}", "'", "\"", "\\", "+", "-", "*", "%", "=", "/", "|", "^", "$", "€", "£", "¥", "<", ">")
english_letters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

user_string = input()

for char in user_string:
    if char in punctuation_marks or char in english_letters:
        user_string = user_string.replace(char, "")

print(len(set(user_string.split())))