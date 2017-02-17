def word_ladder(start, end):
    file = open('words.txt')
    word_list = {}
    
    for word in file:
        if len(start) + 1 == len(word):
            word.replace('\n', '')
            word.replace(' ', '')
            word_list[word[:len(start)]] = start

    queue = [start]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while len(queue):
        cur = queue[0]
        queue.pop(0)
        
        if cur == end:
            return word_list[cur]
        for i in range(len(start)):
            for char in alphabet:
                if cur[i] != char:
                    next = list(cur)
                    next[i] = char
                    new = str(''.join(next))
                    if new in word_list and word_list[new] == start:
                        queue.append(new)
                        word_list[new] = word_list[cur] + ' ' + new

#print word_ladder('dog', 'cat')
#print word_ladder('snakes', 'brains')