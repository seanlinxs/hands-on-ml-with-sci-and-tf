def vector_norm(vector):
    """
    Return Euclidian norm of vector
    >>> import numpy as np
    >>> v = np.array([2, 5])
    >>> vector_norm(v)
    5.385164807134504
    """
    squares = [i ** 2 for i in vector]
    return sum(squares) ** .5


def dot_product(u, v):
    """
    Return dot product of u and v
    >>> import numpy as np
    >>> u = np.array([1, 3, 5])
    >>> v = np.array([2, 4, 6])
    >>> dot_product(u, v)
    44
    """
    products = [ui * vi for ui, vi in zip(u, v)]
    return sum(products)
