# 별세개, p466
# 단어리스트에서 words[i] + words[j]가 팰린드롬이 되는 모든 인덱스 조합(i, j)를 구하라.

# # 브루트 포스 -> O(kn^2) , 타임아웃
# def palinndromePairs(self, words):
#     def is_palindrome(word):
#         return word == word[::-1]
    
#     output = []
#     for i, word1 in enumerate(words):
#         for j, word2 in enumerate(words):
#             if i == j:
#                 continue
#             if is_palindrome(word1+word2):
#                 output.append([i,j])

#     return output



# 트라이 구현
import collections
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    @staticmethod
    def is_palindrome(word):
        return word[::] ==word[::-1]

    # 단어 삽입
    def insert(self, index, word: str) -> None:
        node = self.root
        for char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    # 단어 존재 여부 판별
    def search(self, index, word:str) -> bool:
        result = []
        node = self.root
        
        while word:
            # 판별 로직
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
                if not word[0] in node.children:
                    return result
                node = node.children[word[0]]
                word = word[1:]

        # 판별 로직
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별 로직
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
        
        return result
    
class Solution:
    def palindromePairs(self, words):
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        
        for i, word in enumerate(words):
            results.extend(trie.search(i,word))

        return results