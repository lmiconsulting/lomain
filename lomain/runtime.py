import subprocess
import platform

def check_vpn(vpn_server_address=None):
    """Verifies if the user is connected to a VPN.

    Parameters
    ----------
    vpn_server_address : str
        the IP address of the VPN server
    """
    public_ip_address = subprocess.check_output(["curl", "ifconfig.co"]).decode("utf-8").strip()
    return public_ip_address == vpn_server_address

def get_os():
    """Returns whether the system is running Mac OSX
    """
    os = platform.system()
    if os == "Darwin":
        # using mac os
        return True
    return False