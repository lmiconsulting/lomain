from importlib.metadata import version
import inspect

def get_version(pkg_name):
    """Returns the version number of a package.ß

    Parameters
    ----------
    pkg_name : str
        The name of the package to look up.
    """
    return version(pkg_name)

def is_from_package(obj, package_name):
    """Check if an object's class originates from a specific package.

    Parameters
    ----------
    obj : object
        The object to inspect.
    package_name : str
        Name of the package to check against.

    Returns
    -------
    bool
        True if the object's class is from the specified package, False otherwise.

    Examples
    --------
    >>> import numpy as np
    >>> a = np.array([1, 2, 3])
    >>> is_from_package(a, "numpy")
    True

    >>> from unittest.mock import Mock
    >>> mock_obj = Mock(spec=['attribute', 'method'])
    >>> is_from_package(mock_obj, "mock")
    True
    >>> is_from_package(mock_obj, "unittest")
    True
    >>> is_from_package(mock_obj, "numpy")
    False

    Notes
    -----
    This function checks the immediate parent module of the object's class.
    It may not accurately determine the package for deeply nested module structures.
    """
    # inspect the object's class and find its parent module
    module_name = obj.__class__.__module__
    split_module_name = module_name.rsplit('.', 1) if '.' in module_name else [module_name]
    if package_name not in split_module_name:
        return False
    return True