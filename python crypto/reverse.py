msg=input('Enter message: ')
translated='' 

i=len(msg)-1
while i>=0:
    translated+=msg[i]
    #print('i is', i, ',msg[i] is', msg[i], ',translated is', translated)
    i-=1

print(translated)
