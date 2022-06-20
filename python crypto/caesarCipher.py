import pyperclip

msg=input('type a message: ')

key=13

mode='encrypt' #or 'decrypt'

Symbols='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated=''

for symbol in msg:
    if symbol in Symbols:
        symbolIndex=Symbols.find(symbol)
    
    if mode=='encrypt':
        translatedIndex=symbolIndex+key
    elif mode=='decrypt':
        translatedIndex=symbolIndex-key
   
    if translatedIndex >= len(Symbols):
        translatedIndex -= len(Symbols)
    elif translatedIndex < 0:
        translatedIndex += len(Symbols)
    
    translated += Symbols[translatedIndex]
else:
    translated += symbol

print(translated)
pyperclip.copy(translated)
