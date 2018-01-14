def checkPalindrome(inputString):
    if (inputString == inputString[::-1]):
        return True
    else:
        return False


eyy = "aabaa"
print (checkPalindrome(eyy))
