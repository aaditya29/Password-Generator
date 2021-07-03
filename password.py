import string
from secrets import choice
#The secrets module is used for generating cryptographically strong random numbers suitable
#for managing data such as passwords, account authentication, security tokens, and related secrets.

#In particular, secrets should be used in preference to the default pseudo-random number generator in the random module,
#which is designed for modelling and simulation, not security or cryptography.

# Here, secrets.choice(sequence) returns a randomly-chosen element from a non-empty sequence.

characters = string.ascii_letters + string.punctuation + string.digits
# string.punctuation is a pre-initialized string used as string constant. In Python, string.punctuation will give the all sets of punctuation.
# e.g. !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
# string.digits prints ascii letters and string.digits print numbers
print(characters)

password = "".join(choice(characters) for x in range(0, 32))
print(password)
