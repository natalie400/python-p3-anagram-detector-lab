# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        return [item for item in words if sorted(self.word) == sorted(item.lower()) and item.lower() != self.word]
