from Plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflector

class Enigma_Machine:
     def __init__(self, Reflector_type, Rotor_type1, Rotor_type2, Rotor_type3):
         self.plugboard = Plugboard()
         self.rotor1 = Rotor(Rotor_type1)
         self.rotor2 = Rotor(Rotor_type2)
         self.rotor3 = Rotor(Rotor_type3)
         self.reflector = Reflector(Reflector_type)

     def connect(self, letter1, letter2):
         self.plugboard.connect(letter1, letter2)

     def multiconnect(self, string1, string2):
         self.plugboard.multiconnect(string1, string2)

     def disconnect(self, letter1, letter2):
         self.plugboard.disconnect(letter1, letter2)
    
     def get_phrase(self, string):
         phrase = ""
         for letter in string:
            plugboard_letter = self.plugboard.get(letter)
            rotor1_letter = self.rotor1.get(plugboard_letter)
            rotor2_letter = self.rotor2.get(rotor1_letter)
            rotor3_letter = self.rotor3.get(rotor2_letter)
            reflector_letter = self.reflector.get(rotor3_letter)
            rotor3_letter = self.rotor3.get_reverse(reflector_letter)
            rotor2_letter = self.rotor2.get_reverse(rotor3_letter)
            rotor1_letter = self.rotor1.get_reverse(rotor2_letter)
            plugboard_letter = self.plugboard.get(rotor1_letter)
            phrase += plugboard_letter

         return phrase
