
class Rotor:
    def __init__(self, type):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        Model_dict = {
            'I' : 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'.lower(),
            'II' : 'AJDKSIRUXBLHWTMCQGZNPYFVOE'.lower(),
            'III' : 'BDFHJLCPRTXVZNYEIWGAKMUSQO'.lower(),
            'IV' : 'ESOVPZJAYQUIRHXLNFTGKDCMWB'.lower(),
            'V' : 'VZBRGITYUPSDNHLXAWMJQOFECK'.lower()
            }
        Rotor_reverse = {}
        Rotor_dict = {}
        for i in range(len(alphabet)):
                Rotor_dict[alphabet[i]] = Model_dict[type][i]
                Rotor_reverse[Model_dict[type][i]] = alphabet[i]
        self.rotor_reverse = Rotor_reverse
        self.rotor = Rotor_dict


    def get(self, letter):
        try:
            return self.rotor[letter]
        except:
            return letter


    def get_reverse(self, letter):
        try:
            return self.rotor_reverse[letter]
        except:
            return letter


    
