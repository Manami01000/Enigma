from Enigma_Machine import *

x = Enigma_Machine('A','I','II','III')

x.multiconnect('asdfghjkl', 'zxcvbnm')

y = x.get_phrase('hello')
print(x.get_phrase(y))