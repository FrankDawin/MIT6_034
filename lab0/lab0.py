# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    """take an int and return the cube of the first input (int)"""
    return x**3


def factorial(x):
    """Take an int and return the factorial for that number"""

    answer = 1

    if x < 0:
        raise Exception, "factorial: input must not be negative"

    else:
        for i in range(1, x + 1):
            answer = answer * i

    return answer


p = ("a", "t")
l = ("a", "t", "a", "c", "a", "t", "a", "t")


def count_pattern(pattern, lst):
    """Take a tuple as pattern and a tuple to check and count occurence"""

    answer = 0

    for i in range(len(lst)):
        if lst[i] == pattern[0]:
            if lst[i+1] == pattern[1]:
                answer += 1

    return answer

# Problem 2.2: Expression depth


def depth2(expr, answer = 0):
    """Take an expression and return an int representing the depth"""

    d = []

    for i in expr:
        if isinstance(i, (list, tuple)):
            answer += 1
            return depth(i, answer)
        
    d.append(answer)
    
    return answer      


def depth3(expr):
    """Take an expression and return an int representing the depth"""
        
    if isinstance(expr, tuple):
        return 1 + max(depth(a) for a in expr)

    else:
        return 0
        

def depth4(expr):
    d = lambda expr: isinstance(expr, tuple)
    answer = max(map(d, expr))+1

    return answer


def depth(expr, count=0):
    return count if not isinstance(expr, (list, tuple)) else max([depth(x, count+1) for x in expr])


ex = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
print(depth(ex))


# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    """Function to access data in a tree"""

    answer = None
    current_branch = None

    if len(tree) == 0:
        raise ValueError, "No input"

    elif len(index) == 1:
        return tree[index[0]]

    elif len(index) == 2:
        return tree[index[0]][index[1]]

    elif len(index) == 3:
        return tree[index[0]][index[1]][index[2]]

    elif len(index) == 4:
        return tree[index[0]][index[1]][index[2]][index[3]]
            
    else:
        raise ValueError, "Not a tuple"

    return answer


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = "Last year"

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = "2-20 hours"

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = "Good progression and understanding"

# How many hours did this lab take?
HOURS = "Real long time"
