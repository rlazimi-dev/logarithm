# logarithm

## Purpose
An implementation of the logarithm function without using any existing definitions.

## Running
```
python log.py
```

## Example Input/Output
```
➜ ~/projects/logarithm git:(main) Ω python log.py -b 2 -x 100
custom function result: 6.64385618977
library function result: 6.64385618977
```

## Notes
Binary search is used to guess the best exponent to raise the base to get to the target.

This binary search terminates when a guess is a configurable distance away from the target. To configure this distance: populate the `-p` parameter.

## Runtime Analysis (Work in Progress – Example Only)
```
When calculating log(2,100) instead of trying 2^6, then trying 2^6.5, the algorithm should try 2^6, then save that result, and in the next iteration only calculate 2^0.5 and multiply that to the previously saved answer before comparing the new guess, 2^6 * 2^0.5 = 2^6.5, to the target.

Note that the runtime of doing so ends up being lgarithmic in terms of n. The runtime of 2^6 is log(2,64). The runtime of 2^0.5 = log(2,0.5), and so on.

The sum of logs adds up such that the terms inside are multiplied (TODO)...

Assume log(x) = log(2,x):


```

In short, in each increment, we always divide by two, then decide which direction to go in, to get closer to our answer (classic binary search). In other words, in each increment, we only do constant work.

Therefore, this log function runs in O(log(n)) time.

## TODO
In the current implementation of the log function, the exponent is calculated from scratch in every iteration. Conisdering there are log(n) iterations, where n is the number passed in, this means that the current implementation performs in log(log(n)) time (since python exponentiation is fast). This will be updated so that the result of the first exponentiation is saved and iteratively modified by fractional exponents to get closer to the answer.
