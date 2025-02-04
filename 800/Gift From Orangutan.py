"""
time limit per test 1 second
memory limit per test 256 megabytes
While exploring the jungle, you have bumped into a rare orangutan with a bow tie! You shake hands with the orangutan and offer him some food and water. In return...

The orangutan has gifted you an array 𝑎 of length 𝑛. Using 𝑎, you will construct two arrays 𝑏 and 𝑐, both containing 𝑛 elements, in the following manner:

𝑏𝑖=min(𝑎1,𝑎2,…,𝑎𝑖) for each 1≤𝑖≤𝑛.
𝑐𝑖=max(𝑎1,𝑎2,…,𝑎𝑖) for each 1≤𝑖≤𝑛.
Define the score of 𝑎 as ∑𝑛𝑖=1𝑐𝑖−𝑏𝑖 (i.e. the sum of 𝑐𝑖−𝑏𝑖 over all 1≤𝑖≤𝑛). Before you calculate the score, you can shuffle the elements of 𝑎 however you want.

Find the maximum score that you can get if you shuffle the elements of 𝑎 optimally.

Input
The first line contains 𝑡 (1≤𝑡≤100) — the number of test cases.

The first line of each test case contains an integer 𝑛 (1≤𝑛≤1000) — the number of elements in 𝑎.

The following line contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤1000) — the elements of the array 𝑎.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 1000.

Output
For each test case, output the maximum score that you can get.

input:
3
1
69
3
7 6 5
5
1 1 1 2 2

output:
0
4
4

"""

def score(c,b):
    score = 0 
    for i in range(len(c)):
        score += c[i] - b[i]
    return score

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = []
    d = []
    for i in range(n):
        if i==0:
            c.append(a[i])
            d.append(a[i])
        else:
            c.append(max(a))
            d.append(min(a))
          
    print(score(c,d))
