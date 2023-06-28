
def top_n_values(d, topn, largest=True):
    """Given a dictionary, returns the sub-dictionary whose items have the top n values.

    Parameters
    ----------
    d : dict
        the dictionary to search
    topn : int
        the number of top values to return
    largest : bool
        if True, we select the top n LARGEST values
        if False, we select the top n SMALLEST values
    """
    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=largest)
    top_n_dict = {}
    for i in range(topn):
        top_n_dict[sorted_dict[i][0]] = sorted_dict[i][1]
    return top_n_dict