#Testing

s = input("Enter a Sentence: ")
print(s.strip().lower())
c = s.strip().lower()[::-1] == s.strip().lower()[::1]
print("Palindrome? ",c)

print(s[:3])
print(s[-2:])
print(s.upper())
print(s[::-1])