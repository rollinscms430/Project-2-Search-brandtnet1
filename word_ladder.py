def word_ladder(start, end):
    file = open('words.txt')
    word_list = {}
    
    for word in file:
        if len(start) + 1 == len(word):
            word.replace('\n', '')
            word.replace(' ', '')
            word_list[word[:len(start)]] = start  # Stores all words with same length as start word
    
    print word_list

    queue = [start]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'       # Alphabet to replace a single letter of each word

    while len(queue): # BFS
        cur = queue[0]
        queue.pop(0)
        
        if cur == end: # We got to the end word
            return word_list[cur]
        for i in range(len(start)):
            for char in alphabet:  
                if cur[i] != char:              # Go until you find a word that replaces a single letter
                    next = list(cur)            # of the current word that is in the word list and add that
                    next[i] = char              # to the queue. Append the current path of getting to that word
                    new = str(''.join(next))    # to the current word for printing out once you find the end.
                    if new in word_list and word_list[new] == start:
                        queue.append(new)
                        word_list[new] = word_list[cur] + ' ' + new

#print word_ladder('dog', 'cat')
print word_ladder('snakes', 'brains')