vowel = "aeiou"
char = input("Enter character: ")
if len(char)==1 and char.isalpha():
  char_lower = char.lower()
  if char_lower in vowel:
    print(f"{char} is vowel")
  else:
    print(f"{char} is consonant")
else:
  print("Enter valid character")