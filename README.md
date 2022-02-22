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
