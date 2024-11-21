def find_maximum_difference(a, b):
    """
    Finds the maximum absolute difference between corresponding elements of two lists.

    Parameters:
    ----------
    a : list
        The first list of numerical values.
    b : list
        The second list of numerical values.

    Returns:
    -------
    float:
        The maximum absolute difference between corresponding elements of the two lists.
    
    Example:
    --------
    find_maximum_difference([1, 2, 3], [4, 0, 8])  # Output: 5
    """
    max_list1 = a[0]
    min_list1 = a[0]
    max_list2 = b[0]
    min_list2 = b[0]

    for num in a:
        if num > max_list1:
            max_list1 = num
        if num < min_list1:
            min_list1 = num

    for num in b:
        if num > max_list2:
            max_list2 = num
        if num < min_list2:
            min_list2 = num

    max_diff = max(abs(max_list1 - min_list2), abs(max_list2 - min_list1))
    return max_diff

print(find_maximum_difference([1,10, 999 ],[2,22,22222]))



