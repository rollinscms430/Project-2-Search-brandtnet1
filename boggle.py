def IDDFS(start, length, matrix):
    visited = set()
    goal = set()
    visited.clear()
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
                    
    start_node = [matrix[start/4][start%4], start, visited]
                    
    for i in range(1, length):  # Depth first search until you hit the depth of current length or max length of words wanted
        DFS(start_node, i, word_list, prefix_list, visited, goal)
    return goal

def DFS(node, max_depth, word_list, prefix_list, visited, goal):
    if max_depth <= 0:
        return goal

    x = node[1] / int(4)
    y = node[1] % int(4)
    
    visited.add((x, y))     # Need to fix visited!!!!!!

    for next_square in possible_next(x, y):
        if next_square not in visited:
            prefix = node[0] + matrix[next_square[0]][next_square[1]]   # Create the prefix for next node to compare to word_list
            if prefix in prefix_list:
                next = [prefix, (next_square[0] * 4 + next_square[1] + 4)]
                DFS(next, max_depth - 1, word_list, prefix_list, visited, goal) # DFS from updated prefix and depth 
                if next[0] in word_list:        # word is a goal state, add to goal
                    goal.add(next[0])

def possible_next(x, y):  # Returns a list of all the possible grid squares you can go to next
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
    
def scan_whole_matrix(length, matrix): # Given a length of word to find, this method searches for that length starting at all indexes.
    for i in range(0,16):
        print str(length) + ' letter words starting with the letter ' + str(matrix[i/4][i%4]) + ': ' + str(IDDFS(i, length, matrix))
        
matrix = [
['u', 'n', 't', 'h'],
['g', 'a', 'e', 's'],
['s', 'r', 't', 'r'],
['h', 'm', 'i', 'a']
]  

print scan_whole_matrix(4, matrix)