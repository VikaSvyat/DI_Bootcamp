class AnagramChecker:
    _word_list = None   # class-level cache

    def __init__(self): 
          if AnagramChecker._word_list is None:       
               with open ('./Week4/Day1/sowpods.txt','r') as f:
                    AnagramChecker._word_list = [line.strip().lower() for line in f]
                    
          self.word_list = AnagramChecker._word_list
    
    def is_valid_word (self,word_for_check):
         return word_for_check.lower() in self.word_list

    @staticmethod          
    def is_anagram(word1, word2):
         return sorted(word1) == sorted(word2)
    
    def get_anagrams(self, word):
         anagrams =[]
         for w in self.word_list:
              if AnagramChecker.is_anagram(w, word) and w != word:
                   anagrams.append(w)
         return anagrams
    
# ac = AnagramChecker()
# print(ac.is_valid_word("race"))

# print(AnagramChecker.is_anagram('meat','amte'))
# print(ac.get_anagrams("meat"))