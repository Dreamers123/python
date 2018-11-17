import re

def isPhoneNumber(text):
 if len(text) != 12:
    return False
 for i in range(0, 3):
      if not text[i].isdecimal():
       return False
 if text[3] != '-':
       return False
 for i in range(4, 7):
     if not text[i].isdecimal():
      return False
 if text[7] != '-':
      return False
 for i in range(8, 12):
     if not text[i].isdecimal():
      return False

 return True
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
   chunk = message[i:i+12]
   if isPhoneNumber(chunk):
     print('Phone number found: ' + chunk)
print('Done')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 430-555-4242.')
print('Phone number found: ' + mo.group())
print(phoneNumRegex.findall('Cell: 415-555-99 Work: 212-555-0000'))
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
