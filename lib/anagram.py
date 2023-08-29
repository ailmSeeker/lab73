# your code goes here!
# returns a list with one element when one element of the input list matches the initialized word.

class Anagram:
    def __init__(self, word):
        self.word = []
        self.word.append(word)

    def hello():
        print('hello')
   
    def matching(self, word, getting_word):
            testing_letter = []
            counter = 0

            # the first for loop make sure to find all the matching letters between the two words
            for aletter in getting_word:
                if(word.find(aletter) > -1):
                    counter = counter + 1
                    testing_letter.append(aletter)
            # this if statement make sure that the getting_word is a Anagram
            # right now we are checking the length of the word, the length of the unique words and making sure that testing_letter is also matching that list
            if((len(word) == len(getting_word)) and (len(self.isUnique(word)) == len(self.isUnique(getting_word)))):
                return getting_word
            else:
                return 0
            

    def isUnique(self, word):
        return_list = []

        for letter in word:
            if(not(letter in return_list)):
                return_list.append(letter)

        return return_list
                

    def match(self, another):
        matchs = []

        for a_word in another:
            if(self.matching(self.word[0], a_word)):
                matchs.append(self.matching(self.word, a_word))

        return matchs


x = Anagram('hello')
print(x.match(['dragon', 'hawk', 'olleh']))
