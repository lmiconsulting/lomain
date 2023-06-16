import traceback
import sys, os

from . import strings

def get_module(level=0):
    """Retrieves the module of the calling function, at the desired level of depth.

    Parameters
    ----------
    level : int
        The number of levels above the module of the calling function to return.
        See notes section for detailed explanation.

    Notes
    -----
    If level is 0, the module of the file where the calling function resides is returned.
    If level is 1, the module ONE ABOVE the file where the calling function resides is returned.

    Examples
    --------
    Add the parent module to the path:

        import lomain
        PARENT_MODULE_PATH = lomain.get_module(1)
        sys.path.append(PARENT_MODULE_PATH)
    """
    namespace = sys._getframe(1).f_globals
    caller_abs_path = os.path.abspath(namespace['__file__'])

    # get the index of the [level]th-to-last backslash character
    idx = strings.get_nth_to_last_instance(s=caller_abs_path, char="\\", n=level)
    
    return caller_abs_path[:idx]