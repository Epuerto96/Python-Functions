def percentDifference(new,old):
    """
    Parameters
    ----------
    new : float
        New value being compared
    old : float
        Old value being reference for change

    Returns
    -------
    Float
        Difference bewteen new and old in percent.

    """
    return (abs(new-old)/abs(old))*100
