# for loops
n1 = []
for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:

        n1.append(str(n)
print(','.join(n1))



# monkey trouble

'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each
is smiling. We are in trouble if they are both smiling or if neither of them is smiling.
Return True if we are in trouble
'''

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and b_smile:
        return False
    else:
        return False
print(monkey_trouble(False, False))

# sume_double.
'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
'''

def sum_double(a, b):
    if a == b:
        return (a + b)*2

    else:
        return a + b
print(sum_double(2, 2))
print(sum_double(1, 3))

# diff
'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
'''
def diff(n):
    if n <= 21:
        return 21-n
    else:
        return (n-21)*2
print(diff(23))

# parrot_trouble
'''
We have a loud talking parrot. The "hour" parameter is the current hour time in the range
0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return
True if we are in trouble.
'''

def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))
print(parrot_trouble(True, 6))

# near_hundered
'''
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
'''

def near_hund(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
print(near_hund(111))


# pos_neg
'''
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True,
then return True only if both are negative.
'''

def pos_neg(a, b, neg):
    if neg:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))

print(pos_neg(-1, 1, False))
