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

Note that the runtime of doing so ends up being lgarithmic in terms of n. The runtime of 2^6 is log(2,64). The runtime of 2^0.5 = 1/(2^2) = log(2,4), and so on.

Assume log(x) = log(2,x):

claim:
  we can calculate a given guess by simply multiplying a difference by √2 and adding or subtracting to the previous guess

intuition (needs to be formalized to a proof):
  2^(1/2) = 1/(2)

  suppose we're calculating log(100)

  step 1:
    2^6     => O(log(64))

  step 2:
    The next guess will be exponentiate by a number 0.5 away from 6:

    2^6.5
      = 2^6 * 2^0.5
      = 90.50966799187809...

    notice that we already know the answer to 2.6, so we dont actually calculate it again
  
  step 3:
    The next guess will be exponentiate by a number 0.25 away from 6.5. Since we undershot last time, the exponent will be 6.75.
    
    How do we get from 2^6.5 to 2^6.75 in small time? (hopefully the small time over all iterations adds to log(answer-6) in this case)
    
    2^6.75
      = 2^6.5 * 2^0.25
      = 2^6.5 * 2^(1/4)
      = 2^6.5 * √√2
      = 107.63474115247547...
      
    we already know √2, so all we need is to get from √2 to √√2 _quickly_

  step 4:
    
   

  And so on, with as many steps as necessary until satisfied. In a computer, we stop when the number stops updating due to hardware limitations (floating point number limitations).
  ...

runtime analysis:


```

In short, in each increment, we always divide by two, then decide which direction to go in, to get closer to our answer (classic binary search). In other words, in each increment, we only do constant work.

Therefore, this log function runs in O(log(n)) time.

## TODO
In the current implementation of the log function, the exponent is calculated from scratch in every iteration. Conisdering there are log(n) iterations, where n is the number passed in, this means that the current implementation performs in log(log(n)) time (since python exponentiation is fast). This will be updated so that the result of the first exponentiation is saved and iteratively modified by fractional exponents to get closer to the answer.
