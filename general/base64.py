import base64
hex_val='72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
flag=bytes.fromhex(hex_val)
print(base64.b64encode(flag))
