import numpy as np

rng=np.random.default_rng()
random=rng.integers(low=1,high=101)
number=int(input("guess any number between 1-100: "))
while(number!=random):
    if number>random:
        number=int(input(f"guess number lower than {number}: "))
    else:
        number=int(input(f"guess number greater than {number}: "))
print("you guessed the number 🎉🎊")