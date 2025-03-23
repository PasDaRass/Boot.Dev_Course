def check_ingredient_match(recipe, ingredients):
        match_counter = 0
        missing = []
    
        for i in recipe:
            if i in ingredients:
                match_counter += 1
            else:
                missing.append(i)             
            
        percentage = (match_counter / len(recipe)) * 100
        return float(percentage), missing
