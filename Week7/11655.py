# input str
S = input()

# apply ROT13
cipher = ''
for c in S:
  if ord('A') <= ord(c) <= ord('Z'):
      cipher += chr(( ord(c) - ord('A') + 13 ) % 26 + ord('A'))
  elif ord('a') <= ord(c) <= ord('z'):
      cipher += chr(( ord(c) - ord('a')+ 13 ) % 26 + ord('a'))
  else:
      cipher += c
  
# print a cipher
print(cipher)