# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #2 | PROBLEM 2 - DECRYPTION

# ASCII art for the header with ANSI escape codes for color.
print("\033[38;5;218m" + """
┼┼┼┼┼┼┼┼┼┼┼┼▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄┼┼┼┼┼┼┼┼┼┼┼  
┼┼┼┼┼┼┼┼┼┼┼┼█▒▒░░░░░░░░░▒▒█┼┼┼┼┼┼┼┼┼┼┼ 
┼┼┼┼┼┼┼┼┼┼┼┼█░░█░░░░░█░░█┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼─▄▄──█░░░▀█▀░░░█──▄▄─┼┼┼┼┼┼┼┼ 
┼┼┼┼┼┼┼┼┼█░░█─▀▄░░░░░░░▄▀─█░░█┼┼┼┼┼┼┼┼ 
┼┼┼┼┼┼██░██░████░██░░░██░░░█████┼┼┼┼┼┼
┼┼┼┼┼┼██▄██░██▄▄░██░░░██░░░██░██┼┼┼┼┼┼
┼┼┼┼┼┼██▀██░██▀▀░██░░░██░░░██░██┼┼┼┼┼┼
┼┼┼┼┼┼██░██░████░████░████░█████┼┼┼┼┼┼                                         
""" + "\033[0m")

#Pseudocode
# Ask the user to provide an encrypted text to be decrypted.
user_input_string = input("Enter a string to decrypt: ")
output_str = ""
# Go through each character in the string.
for char in range(len(user_input_string)): 
#   If the symbol is asterisk "*", replace it with the character "a"
    if user_input_string[char] == "*":
        output_str += "a" 
#   If the symbol is ampersand "&", replace it with the character "e"
    elif user_input_string[char] == "&":
        output_str += "e"
#   If the symbol is hash "#", replace it with the character "i"
    elif user_input_string[char] == "#":
        output_str += "i"
#   If the symbol is plus "+", replace it with the character "o"
    elif user_input_string[char] == "+":
        output_str += "o"
#   If the symbol is exclamation point "!", replace it with the character "u"
    elif user_input_string[char] == "!":
        output_str += "u"
    else:
        output_str += user_input_string[char]

# Print the output.
print (output_str)

