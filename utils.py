def get_padding(column_header:str)-> str:
    """
    Returns the necesarry character number padding in order
    for the information to be centered in the table returned
    by the __str__ functions for each object of the domain.
    Args:
        column_header (str): header of the column that we
        want centering for

    Returns:
        int: the left/right hand-side padding needed
    """
    column_header=str(column_header)
    return int((len(column_header)/2)+1) * " "