import argparse

parser = argparse.ArgumentParser(description='run the logarithm function')
parser.add_argument('--base', '-b', dest='b', type=float, help='the base to exponentiate')
parser.add_argument('--target', '-x', dest='x', type=float, help='the number to exponentiate the base to')
parser.add_argument('--precision', '-p', dest='precision', type=float, help='the error allowed for a binary search guess to be correct')
parser.set_defaults(
  base=2,
  precision=0.000000001
)

args = parser.parse_args()
b = args.b
x = args.x
precision = args.precision

if not b > 0:
  print("\nbase must be greater than 0. you cannot put an exponent on 0 and expect it to reach the target.")
  print("")
  parser.print_help()
  exit(1)
elif not x > 1:
  print("\nthis implementation does not cover targets smaller than 1 yet.")
  print("")
  parser.print_help()
  exit(1)


def abs(x):
  return x if x > 0 else x * -1

#the simple definition of log is the amount of times that you can divide a number, x, by another, base

def simple_log(b, x):

  exp = 0
  cursor = int(x)
  b_int = int(b)
  while cursor > 1:
    cursor = cursor/b_int   #intentionally integer division
    exp += 1

  return exp


def log(b,x,precision=0.000000001):

  left = simple_log(b,x)
  right = left+1

  cursor = (left + right) / 2.0
  guess = b**cursor

  while abs(guess - x) > precision:

    #guess was too small, lower bound increases
    if guess == x:
      return cursor
    #guess was too large, upper bound decreases
    elif guess > x:
      right = cursor
    else:
      left = cursor

    cursor = (left + right) / 2.0
    guess = b**cursor

  return cursor

print('custom function result: %s' % log(b,x,precision=precision) )

import math
print('library function result: %s' % (math.log(x) / math.log(b) ) )

