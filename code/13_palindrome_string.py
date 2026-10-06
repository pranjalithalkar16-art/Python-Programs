def is_palindrome(text):
    reverse = ""

    for ch in text:
        reverse = ch + reverse

    return text == reverse


print(is_palindrome("madam"))