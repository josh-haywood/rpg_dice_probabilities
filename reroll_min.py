#!/bin/python

import random
import math

def dice_roll(d):
  return random.randrange(1,d+1)

def stat_roll():
  dice = [dice_roll(6),dice_roll(6),dice_roll(6),dice_roll(6)]
  dice[dice.index(min(dice))] = dice_roll(6)
  dice.remove(min(dice))
  total = 0
  for i in dice:
    total += i
  return total




max_ = 0
min_ = 100000
sum_ = 0
mean = 78
runs = 10000000
s = 0
for i in range(1,runs+1):
  val = 0
  for j in range(1,7):
    val += stat_roll()
  if val > max_:
    max_ = val
  elif val < min_:
    min_ = val
  s += (val - mean)**2
  sum_ += val
  if i % 10000 == 0:
    print("\033c")
    print("%d/%d iterations performed, %.02f%% done" % (i,runs,float(i)/runs*100))

s = s/(runs-1)
d = math.sqrt(s)
avg = sum_/float(runs)
print(max_)
print(min_)
print(avg)
print(s)
print(d)
