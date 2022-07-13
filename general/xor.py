text="label"
result=""

for i in text:
    result+=chr(ord(i)^13)

print(f"crypto{{{result}}}")
