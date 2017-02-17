file = open('words.txt')
anagram_dictionary = {}

for word in file:
    word_list = list(word)
    word_list.sort()
    
    if tuple(word_list) not in anagram_dictionary:
        temp_list = [word]
        anagram_dictionary[tuple(word_list)] = temp_list
            
    anagram_dictionary[tuple(word_list)].append([word])