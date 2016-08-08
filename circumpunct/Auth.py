from requests.auth import HTTPBasicAuth

from Common.Encryption import getPassword


def getBasicAuth():
    return HTTPBasicAuth('ecstaticjack@gmail.com',getPassword())