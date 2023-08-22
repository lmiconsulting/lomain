from importlib.metadata import version

def get_version(pkg_name):
    """Returns the version number of a package.ß

    Parameters
    ----------
    pkg_name : str
        The name of the package to look up.
    """
    return version(pkg_name)