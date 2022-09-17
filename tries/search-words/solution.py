"""
https://github.com/cherokee-rose
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
    * WordDictionary() Initializes the object.
    * void addWord(word) Adds word to the data structure, it can be matched later.
    * bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

 
Example:
    Input
        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output
        [null,null,null,null,false,true,true,true]

Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True

Constraints:
    * 1 <= word.length <= 25
    * word in addWord consists of lowercase English letters.
    * word in search consist of '.' or lowercase English letters.
    * There will be at most 3 dots in word for search queries.
    * At most 10^4 calls will be made to addWord and search.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            current = node
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in current.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                else:
                    if word[i] not in current.children:
                        return False
                    current = current.children[word[i]]

            return current.is_end

        return dfs(self.root, 0)
