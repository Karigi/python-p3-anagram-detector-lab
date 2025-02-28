class Anagram:
    def __init__(self,word):
        self.word = word
        self.matching_word = []

    def match(self,my_list):
        new_word = sorted(self.word)
        for item in my_list:
            new_item = sorted(item)
            if new_word == new_item:
                self.matching_word.append(item)
        return self.matching_word
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))

