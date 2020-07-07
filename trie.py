from collections import defaultdict


class TrieNode():

    def __init__(self):
        self.children = defaultdict()
        self.wordslist = set()
        self.terminating = False


class Trie():

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):

        original_word = word.lower()
        word =''.join(sorted(word.lower()))

        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)

        root.terminating = True
        root.wordslist.add(original_word)

    def search(self, word):
        root = self.root
        len1 = len(word)

        original_word = word.lower()
        word =''.join(sorted(word.lower()))

        for i in range(len1):
            index = self.get_index(word[i])
            if not root:
                return (False,None)
            root = root.children.get(index)

        return (True,root.wordslist) if root and root.terminating else (False,None)

    def delete(self, word):

        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])

            if not root:
                print ("Word not found")
                return -1
            root = root.children.get(index)

        if not root:
            print ("Word not found")
            return -1
        else:
            root.terminating = False
            return 0

    def update(self, old_word, new_word):
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)

    

