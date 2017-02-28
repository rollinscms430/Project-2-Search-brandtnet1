"""
IDDFS - Iterative Deepening Depth First Search

Search up until desired depth, depth = length of word.
"""
def IDDFS(start, length, matrix):
    goal = set()
    goal.clear()
    file = open('words.txt')
    word_list = {}
    prefix_list = {}
    
    for word in file:
        if length == (len(word) - 1) and word[:1] == matrix[start/4][start%4]:
            word_list[word[:length]] = 0
            for i in range(2, len(word)):
                if word[:i] not in prefix_list:
                    prefix_list[word[:i]] = 0
                    
    cords = set()
    cords.add((start/4,start%4))
    start_node = [matrix[start/4][start%4], start, cords]

    for i in range(1, length):  # Depth first search until you hit the depth of current length or max length of words wanted
        DFS(start_node, i, word_list, prefix_list, goal)
    return goal

"""
DFS- Depth First Search

Following logic from IDDFS, only search up until a specific depth at any given time.
"""
def DFS(node, max_depth, word_list, prefix_list, goal):
    if max_depth <= 0:
        return goal

    x = node[1] / int(4)
    y = node[1] % int(4)
    node[2].add((x,y))
    
    visited = set()
    
    for i in node[2]:       # Look through all cords been through so far, if cords match with letters then save them otherwise get rid of them.
        if matrix[i[0]][i[1]] in node[0]:
            visited.add(i)
            
    node[2] = visited 
    
    for next_square in possible_next(x, y):
        if next_square not in node[2]:
            prefix = node[0] + matrix[next_square[0]][next_square[1]]   # Create the prefix for next node to compare to word_list
            if prefix in prefix_list:
                next = [prefix, (next_square[0] * 3 + next_square[1] + next_square[0]), visited]
                DFS(next, max_depth - 1, word_list, prefix_list, goal) # DFS from updated prefix and depth
                if next[0] in word_list:        # word is a goal state, add to goal
                    goal.add(next[0])

"""
Return a list of all possible next grid squares
"""
def possible_next(x, y):
    neighbors = (       
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y),
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y + 1))
    return [p for p in neighbors if 0 <= p[0] < 4 and 0 <= p[1] < 4]
    
def scan_whole_matrix(matrix): # Given a length of word to find, this method searches for that length starting at all indexes.
    count = 0
    for i in range(0,16):
        dict = []
        
        for j in range(2, 16): # 3 letter words up to max of 16 letter words
            temp = IDDFS(i, j, matrix)
            for item in temp:
                dict.append(item)  
                count += 1   # Number of words, just a test
            
        print 'Words starting with the letter ' + str(matrix[i/4][i%4]) + ': ' + str(dict) + '\n'

matrix = [
['u', 'n', 't', 'h'],
['g', 'a', 'e', 's'],
['s', 'r', 't', 'r'],
['h', 'm', 'i', 'a']
]  

scan_whole_matrix(matrix)
# print IDDFS(7, 4, matrix)