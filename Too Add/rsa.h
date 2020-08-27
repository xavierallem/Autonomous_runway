#ifndef RSA_FUNCTIONS_H_
#define RSA_FUNCTIONS_H_

/* Same function is used to encrypt/decrypt.
Encrypt: slInput - Int to encrypt ; slKey - Public key
Decrypt: slInput - Encrypted Int to decrypt ; slKey - Private key */
long encryptInt(long slInput, long slN, long slKey)
{
	long k = 1;
	long j;
	for (j = 0; j<slKey; j++)
	{
		k = k * slInput;
		k = k % slN;
	}
	return k;
}

#endif