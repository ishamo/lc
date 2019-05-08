class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bag = {}


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        lenw = len(word)
        if not lenw in self.bag:
            self.bag[lenw] = []
        self.bag[lenw].append(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        lenw = len(word)
        if lenw not in self.bag: return False
        return any([self.equal_to(word, item) for item in self.bag[lenw]])

    def equal_to(self, target, word):
        if not len(target) == len(word): return False
        for idx, c in enumerate(target):
            if not c == '.' and not c == word[idx]:
                return False
        return True





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
