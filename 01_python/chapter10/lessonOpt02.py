def merge(dict1, dict2):
    new_dict = {}
    for k in dict1:
        new_dict[k] = dict1[k]
    for k in dict2:
        new_dict[k] = dict2[k]
    return new_dict


def total_score(score_dict):
        score = 0
        for k in score_dict:
            score += score_dict[k]
        return score
