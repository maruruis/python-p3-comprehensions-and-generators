def return_evens(num_list):
    evens = []
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
    return evens

def make_exclamation(sentence_list):
    exclamations = []
    for sentence in sentence_list:
        exclamations.append(sentence + '!')
    return exclamations
