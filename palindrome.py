# Test a sentence is palindrome or not

text = "Rise to vote, sir."
original_text=''.join(t for t in text if t.isalnum()) # joins the each character continuously eliminating special char

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == text[::-1]

if is_palindrome(original_text.lower()):
    print 'Yes, its palindrome'
else:
    print 'No, its not palindrome'
