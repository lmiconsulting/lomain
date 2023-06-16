import traceback
import sys, os

from . import strings

def get_module(level=0):
    """Retrieves the module of the calling function, at the desired level of depth.

    Parameters
    ----------
    level : int
        The 

    Notes
    -----
    If level is 0, the module of the file where the calling function lives is returned.
    If level is 1, 
    """
    namespace = sys._getframe(1).f_globals
    caller_abs_path = os.path.abspath(namespace['__file__'])

    # get the index of the [level]th-to-last backslash character
    idx = strings.get_nth_to_last_instance(s=caller_abs_path, char="\\", n=level)
    
    return caller_abs_path[:idx]