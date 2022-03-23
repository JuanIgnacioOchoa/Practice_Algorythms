#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ans = []
    ranks = dict()
    j = 0
    r = 1
    prev = 0
    while j < len(ranked):
        if r not in ranks and prev != ranked[j]:
            ranks[r] = ranked[j]
            prev = ranked[j]
            r+=1
        j+=1
    a = len(player) - 1 
    for key in ranks:
        if ranks[key] <= 0 and a >= 0:
            ans.append(key)
            a-=1
            while ranks[key] <= 0 and a >= 0:
                ans.append(key)
                a -= 1
    if ranks[key] <= 0:
        r -= 1
    while len(ans) != len(player):
        ans.append(r)
    ans.reverse()
    return ans

ranked_count = 6

ranked = list(map(int, "997 988 981 966 957 937 933 930 929 928 927 926 922 920 916 915 903 896 887 874 872 866 863 863 860 859 858 857 857 847 847 842 830 819 815 809 803 797 796 794 794 789 785 783 778 772 765 765 764 757 755 751 744 740 737 733 730 730 724 716 710 709 691 690 684 677 676 653 652 650 625 620 619 602 587 587 585 583 571 568 568 556 552 546 541 540 538 531 530 529 527 506 504 501 498 493 493 492 489 482 475 468 457 452 445 442 441 438 435 435 433 430 429 427 422 422 414 408 404 400 396 394 387 384 380 379 374 371 369 369 369 368 366 365 363 354 351 341 337 336 328 325 318 316 314 307 306 302 287 282 281 277 276 271 246 238 236 230 229 229 228 227 220 212 199 194 179 173 171 168 150 144 136 125 125 124 122 118 98 98 95 92 88 85 70 68 61 60 59 44 43 35 32 30 28 23 20 13 12 12".rstrip().split()))

player_count = 5

player = list(map(int, "83 129 140 184 198 300 312 325 341 344 349 356 370 405 423 444 465 471 491 500 506 508 539 543 569 591 607 612 614 623 645 670 689 726 744 747 764 773 777 787 805 811 819 829 841 905 918 918 955 997".rstrip().split()))

result = climbingLeaderboard(ranked, player)
print(result)