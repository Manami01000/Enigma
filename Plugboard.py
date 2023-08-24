import string


class Plugboard:
    def __init__(self):
        self.plugboard = {chr(ord('a')+i) : chr(ord('a')+i) for i in range(26)}

    def get(self, letter):
        try:
            return self.plugboard[letter]
        except:
            return letter

    def disconnect(self, letter1, letter2):
        self.plugboard[letter1] = letter1
        self.plugboard[letter2] = letter2

    def connect(self, letter1, letter2):
        if self.plugboard[letter1] != letter1:
            self.disconnect(letter1, self.plugboard[letter1])
        if self.plugboard[letter2] != letter2:
            self.disconnect(letter2, self.plugboard[letter2])
        self.plugboard[letter1] = letter2
        self.plugboard[letter2] = letter1

    def multiconnect(self, string_1, string_2):
        big_str = max(string_1, string_2, key = len)
        small_str = min(string_1, string_2, key = len)
        for i in range(len(small_str)):
            self.connect(small_str[i], big_str[i])
        

        