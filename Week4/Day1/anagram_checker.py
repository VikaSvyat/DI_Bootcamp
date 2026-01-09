class AnagramChecker:
    def __init__(self, word):        
        with open ('Week4/Week1/sowpods.txt','r') as f:
                word_list = f.readlines()
        self.word_list = [line.strip().lower() for line in word_list]
        self.word = word.lower()

    def is_valid_word (self):
         return self.word in self.word_list

    @staticmethod          
    def is_anagram(word1, word2):
         return sorted(word1) == sorted(word2)
    
    def get_anagrams(self, word):
         anagrams =[]
         for w in self.word_list:
              if AnagramChecker.is_anagram(w, word) and w != word:
                   anagrams.append(w)
         return anagrams
    
# ac = AnagramChecker("meat")
# print(ac.is_valid_word())

# print(AnagramChecker.is_anagram('meat','amte'))
# print(ac.get_anagrams("meat"))