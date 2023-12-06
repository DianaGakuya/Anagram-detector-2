class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagrams = []
        for candidate in word_list:
            if self.is_anagram(candidate):
                anagrams.append(candidate)
        return anagrams

    def is_anagram(self, candidate):
        return sorted(candidate.lower()) == sorted(self.word.lower())
