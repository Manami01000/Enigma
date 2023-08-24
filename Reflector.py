class Reflector:
    def __init__(self, type):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        Model_a = 'ejmzalyxvbwfcrquontspikhgd'
        Model_b = 'yruhqsldpxngokmiebfzcwvjat'
        Model_c = 'fvpjiaoyedrzxwgctkuqsbnmhl'
        Reflector_dict = {}
        if type == 'A' or type == 'a':
            for i in range(len(alphabet)):
                Reflector_dict[alphabet[i]] = Model_a[i]
        elif type == 'B' or type == 'b':
            for i in range(len(alphabet)):
                Reflector_dict[alphabet[i]] = Model_b[i]
        elif type == 'C' or type == 'c':
            for i in range(len(alphabet)):
                Reflector_dict[alphabet[i]] = Model_c[i]
        else:
            print('Invalid Reflector Type, no such type as ' + str(type))

        self.reflector = Reflector_dict
    
    def get(self, letter):
        try:
            return self.reflector[letter]
        except:
            return letter

