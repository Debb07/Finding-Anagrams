# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

s1 = input("Enter the first word: ")
s2 = input("Enter the second word: ")

a = s1.lower()
b = s2.lower()

def find_anagrams(s1, s2):
    # [assignment] Add your code here
    if(sorted(a) == sorted(b)):
        return True
    else:
        return False

print(find_anagrams(s1, s2))
