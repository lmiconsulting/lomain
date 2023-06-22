import os, yaml

from attrdict import AttrDefault


def read_cfg(cfg_path, DEFAULTS=None):
    """Load the config from a yaml file, given a path

    Parameters
    ----------
    cfg_path : str
        the full path to your config file
    DEFAULTS : generic object w/ attributes or None
        the defaults for your config. see Notes for an example.

    Notes
    -----
    Example DEFAULTS object:

        class DEFAULTS():
            num_params=15e9
            model_type="GPTNeoXForCausalLM"
            device_map=True
    """
    with open(cfg_path, "r") as f:
        cfg: AttrDefault = AttrDefault(
            lambda: None, 
            yaml.load(f, Loader=yaml.Loader),
            sequence_type=list
        )
    
    if DEFAULTS is not None:
        D = DEFAULTS.__dict__
        for k in D:
            if cfg[k] is None:
                cfg[k] = D[k]
    return cfg