def word_break_v2(s, wordDict):
    word_set = set(wordDict)
    memo = {}
    def backtrack(index):
        if index in memo:
            return memo[index]
        if index == len(s): 
            return [""]

        sentences = []
        for end in range(index + 1, len(s) + 1): 
            word = s[index:end]
            if word in word_set: 
                rest_sentences = backtrack(end)
                for sentence in rest_sentences: 
                    sentences.append(word + (" " + sentence if sentence else ""))
        memo[index] = sentences
        return sentences
        
    return backtrack(0)

s = "catsanddog"
word_dict =  ["cat","cats","and","sand","dog"]
print(word_break_v2(s, word_dict))
