def anagrams(word, words):
    """"find all the anagrams of a word from a list"""
    
    word_sorted = sorted(word)
    anagram_list = [*filter(lambda w: sorted(w) == word_sorted, words)]
    return anagram_list
