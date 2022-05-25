# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    # i am trying to replace all empty spaces inside and around the word
    word = word.replace(" ", "").strip()
    # i am trying to replace all empty spaces inside and around the word to comapre with the other
    anagram = anagram.replace(" ", "").strip()
    # checking to see if the length of the two words are the same. If they are not, Then it is not Anagram
    if(len(word) != len(anagram)):
        return False
    else:
        # since the length are the same. I will try to sort them to see if the values are the same.
        if sorted(word) == sorted(anagram):
            return True
        else:
            return False


# collecting the first input from the user
first_string = input("Provide the first string or word: ")
# collecting the second input from the user
second_string = input(
    "Provide the second string to compare with the word above: ")

# calling the function to find anagram between the two words or strings
print(find_anagram(first_string, second_string))
