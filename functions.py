import numpy as np, numpy.random

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



def randomArrayist(n,p):
    """Generates Random Array.

    Parameters
    ----------
    n : Int
        Length.
    p : type
        Width.

    Returns
    -------
    type
        Array

    """
    x = np.random.dirichlet(np.ones(n),size=p)
    return x
