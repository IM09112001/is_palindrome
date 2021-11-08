isPalindrome = input("Write string: ")
isPalindrome = isPalindrome.lower().rstrip(" ")
def is_palindrome(isPalindrome):
  return isPalindrome == isPalindrome[::-1]
#     print("This string is palindrome.")
# else: print("This string is not palindrome.")

print(is_palindrome(isPalindrome))