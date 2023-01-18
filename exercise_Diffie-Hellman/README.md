# Diffie-Hellman key exchange.

This code uses the Diffie-Hellman key exchange algorithm to generate private, public and secret key.

`private_key(p: int) -> int`

This function generates a private key within the range of 2 and (p - 1) using the `random.randint()` function. The private key is used in the generation of the public key and secret key.

`public_key(p: int, g: int, private: int) -> int`

This function generates a public key using the provided `p`, `g`, an`d` private key. The public key is used in the generation of the secret key.

`secret(p: int, public: int, private: int) -> int`

This function generates a secret key using the provided `p`, `public key` and `private key`. The secret key is a shared key that is derived from the public key and private key.

The `p` and `g` are the prime number and primitive root modulo p respectively, which are commonly shared between the two parties. The private key is the key that is kept private by one of the parties, the public key is derived from the private key and shared, and the secret key is derived from the public key and private key.

## Example

```python
p = 23
g = 5

# Generate private key
private = private_key(p)
print(f'Private key: {private}')

# Generate public key
public = public_key(p, g, private)
print(f'Public key: {public}')

# Generate secret key
secret_key = secret(p, public, private)
print(f'Secret key: {secret_key}')
```

Please keep in mind that this is an example and its output depends on the input and the randomness of the private key generated, so it could be different every time the code runs
