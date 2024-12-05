
WORD = "XMAS"

def get_word_search():
    word_search = []

    with open("inputs/4.txt") as file:
        for line in file:
            word_search.append(line)
            
    return word_search

def search_for_word(word_search, i, j):
    width = len(word_search[0])
    height = len(word_search)
    word_len = len(WORD)
    total = 0
    
    space_right = j + word_len <= width
    space_left = j >= word_len - 1
    space_down = i + word_len <= height
    space_up = i >= word_len - 1
    
    if space_down:
        """
        X
        M
        A
        S
        """
        word = "".join([word_search[i+change][j] for change in range(word_len)])
        if word == WORD:
            total+=1
    
    if space_up:
        """
        S
        A
        M
        X
        """
    
        word = "".join([word_search[i - change][j] for change in range(word_len)])
        if word == WORD:
            total+=1

    if space_right:
        """
        XMAS
        """
        word = "".join([word_search[i][j+change] for change in range(word_len)])
        if word == WORD:
            total+=1
            
                
    if space_left:
        """
        SAMX
        """
        word = "".join([word_search[i][j-change] for change in range(word_len)])
        if word == WORD:
            total+=1
            
    if space_up and space_right:
        """
           S
          A
         M 
        X
        """
        word = "".join([word_search[i-change][j+change] for change in range(word_len)])
        if word == WORD:
            total+=1
        
    if space_down and space_right:
        """
        X   
         M 
          A
           S
        """
        word = "".join([word_search[i+change][j+change] for change in range(word_len)])
        if word == WORD:
            total+=1  
        
    if space_up and space_left:
        """
        S   
         A 
          M
           X
        """
        
        word = "".join([word_search[i-change][j-change] for change in range(word_len)])
        if word  == WORD :
            total+=1
            
    if space_left and space_down:
        """
           X
          M
         A 
        S
        """
        word = "".join([word_search[i+change][j-change] for change in range(word_len)])
        if word == WORD:
            total+=1
    
    return total

def search_for_x(word_search, i, j):
    print(i, j)
    if i <= 0:
        return 0
    
    if j <= 0:
        return 0
    
    width = len(word_search[0])
    height = len(word_search)
    
    if i >= height - 1:
        return 0
    
    if j >= width - 1:
        return 0
    
    up_left = word_search[i-1][j-1]
    up_right = word_search[i-1][j+1]
    down_left = word_search[i+1][j-1]
    down_right = word_search[i+1][j+1]
    
    M = "M"
    S = "S"
    
    if up_left == M:
        if up_right == S and down_left == M and down_right == S:
            return 1
    
        if up_right == M and down_left == S and down_right == S:
            return 1
        
    if up_left == S:
        if up_right == S and down_left == M and down_right == M:
            return 1
    
        if up_right == M and down_left == S and down_right == M:
            return 1
        
    return 0
    
        

def count_all_words():
    word_search = get_word_search()

    word_count = 0

    for i, line in enumerate(word_search):
        for j, char in enumerate(line):
            if char == WORD[0]:
                word_count+= search_for_word(word_search, i, j)
                
    print(word_count)
    
def count_all_x():
    word_search = get_word_search()
    
    count = 0
    for i, line in enumerate(word_search):
        for j, char in enumerate(line):
            if char == "A":
                count += search_for_x(word_search, i, j)
                
    print(count)
    

count_all_words()
count_all_x()