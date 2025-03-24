def filter_messages(messages):
    filtered = []
    words_removed = []
    for i in messages:
        split_msg = i.split()
        clean_msg = []
        counter = 0
        
        for word in split_msg:
            if word == "dang":
             counter += 1
            else:
                clean_msg.append(word)
        
        sentence = " ".join(clean_msg)
        filtered.append(sentence)
        words_removed.append(counter)
    return filtered, words_removed
        
            
    
        
    
