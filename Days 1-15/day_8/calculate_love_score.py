def calculate_love_score(name1, name2):
    #combine names
    names = name1.lower() + name2.lower()
    names_without_spaces = names.replace(" ", "")
    
    #iterate for loop
    true = 0
    love= 0
    for letter in names_without_spaces:
        if letter in 'true':
            true += 1
        if letter in 'love':
            love += 1
            
            
    love_score = str(true) + str(love)
    #return 2 digit num as an f basestring
    print(love_score)
    return int(love_score)
    
    
calculate_love_score("Alex Straton", "Miguel Cano")