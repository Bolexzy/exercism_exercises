import random

"""
Diffie-Hellman key exchange is a mathematical method of securely exchanging cryptographic keys over a public channel and was one of the first public-key protocols as conceived by Ralph Merkle and named after Whitfield Diffie and Martin Hellman.
"""

def private_key(p):
    """
    This function generates a private key greater than 1 and less than p.
    The private key is used to generate the public key and secret key.

    Parameters:
    p (int): A prime number used in the public key and secret key generation process

    Returns:
    int: A private key within the range of 2 and (p - 1).
    """
    private = random.randint(2, (p - 1))
    return private


def public_key(p, g, private):
    """
    This function generates a public key using the provided p, g and private key.
    The public key is used to generate the secret key.

    Parameters:
    p (int): A prime number used in the public key and secret key generation process
    g (int): A number that is primitive root modulo p
    private (int): A private key greater than 1 and less than p.

    Returns:
    int: A public key
    """
    public = (g ** private) % p
    return public


def secret(p, public, private):
    """
    This function generates a secret key using the provided p, public key and private key.

    Parameters:
    p (int): A prime number used in the public key and secret key generation process
    public (int): A public key
    private (int): A private key greater than 1 and less than p.

    Returns:
    int: A secret key
    """
    secret_key = (public ** private) % p
    return secret_key
