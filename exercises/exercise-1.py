# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

result = "not valid"
while result == "not valid":
    letter = input("Enter a letter: ")
    littleletter = letter.lower()
    vowel = ('aeiou')
    if littleletter.isalpha() and len(littleletter) == 1:
        if littleletter in vowel:
            print(f"{letter} is a Vowel")
            result = "valid"
        elif letter == "y":
            print(f"{letter} is SOMETIMES a Vowel!")
            result = "valid"
        else:
            print(f"{letter} is a Consonant!")
            result = "valid"
    else:
        print("Invalid entry, don't get cheeky, 1 letter.")