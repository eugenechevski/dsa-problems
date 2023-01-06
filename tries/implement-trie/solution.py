"""
https://github.com/eugenechevski
https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
    * Trie() Initializes the trie object.
    * void insert(String word) Inserts the string word into the trie.
    * boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    * boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
    
Example 1:
    Input
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    Output
        [null, null, true, false, true, null, true]

Explanation
    Trie trie = new Trie();
    trie.insert("apple");
    trie.search("apple");   // return True
    trie.search("app");     // return False
    trie.startsWith("app"); // return True
    trie.insert("app");
    trie.search("app");     // return True
    
Constraints:
    * 1 <= word.length, prefix.length <= 2000
    * word and prefix consist only of lowercase English letters.
    * At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _get_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word) -> None:
        current_node = self.root
        for char in word:
            index = self._get_index(char)

            if not current_node.children[index]:
                current_node.children[index] = TrieNode()
            current_node = current_node.children[index]

        current_node.end_of_word = True

    def search(self, word) -> bool:
        current_node = self.root
        for char in word:
            index = self._get_index(char)

            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]

        return current_node.end_of_word

    def startsWith(self, prefix) -> bool:
        current_node = self.root
        for char in prefix:
            index = self._get_index(char)

            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
