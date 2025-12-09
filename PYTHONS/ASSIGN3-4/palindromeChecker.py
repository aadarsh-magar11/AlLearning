word = input("enter the word to check if it is palindrome or not:")
# str[::-1] reverses the string 
def checkPalindrome(text):
    if text == text[::-1] :
        print(f"{text} is palindrome")
    else:
        print(f"{text} is not a palindrome")

checkPalindrome(word)