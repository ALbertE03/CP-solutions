"""
time limit per test 1 second
memory limit per test 256 megabytes
You are given two integers 𝑛 and 𝑘.

In one operation, you can subtract any power of 𝑘 from 𝑛. Formally, in one operation, you can replace 𝑛 by (𝑛−𝑘^𝑥) for any non-negative integer 𝑥.

Find the minimum number of operations required to make 𝑛 equal to 0.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤104). The description of the test cases follows.

The only line of each test case contains two integers 𝑛 and 𝑘 (1≤𝑛,𝑘≤109).

Output
For each test case, output the minimum number of operations on a new line.

Example
input:
6
5 2
3 5
16 4
100 3
6492 10
10 1
output:
2
3
1
4
21
10

Note:
In the first test case, 𝑛=5 and 𝑘=2. We can perform the following sequence of operations:

Subtract 2^0=1 from 5. The current value of 𝑛 becomes 5−1=4.
Subtract 2^2=4 from 4. The current value of 𝑛 becomes 4−4=0.
It can be shown that there is no way to make 𝑛 equal to 0 in less than 2 operations. Thus, 2 is the answer.

In the second test case, 𝑛=3 and 𝑘=5. We can perform the following sequence of operations:

Subtract 5^0=1 from 3. The current value of 𝑛 becomes 3−1=2.
Subtract 5^0=1 from 2. The current value of 𝑛 becomes 2−1=1.
Subtract 5^0=1 from 1. The current value of 𝑛 becomes 1−1=0.
It can be shown that there is no way to make 𝑛 equal to 0 in less than 3 operations. Thus, 3 is the answer.
"""
def calculate_attempts(n, k):
    attempts = 0
    if k == 1:
        return n  

    power_value = 1
    powers = []
    while power_value <= n:
        powers.append(power_value)
        power_value *= k
    while n > 0:
        for power in reversed(powers):
            if power <= n:
                count = n // power  
                attempts += count
                n -= count * power
                break
        else:
            attempts += n  
            break
    return attempts

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(calculate_attempts(n, k))