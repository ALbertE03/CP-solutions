"""
time limit per test1 second
memory limit per test256 megabytes

You are given an array 𝑎1,𝑎2,…,𝑎𝑛 of positive integers.

You can color some elements of the array red, but there cannot be two adjacent red elements (i.e., for 1≤𝑖≤𝑛−1, at least one of 𝑎𝑖 and 𝑎𝑖+1 must not be red).

Your score is the maximum value of a red element plus the number of red elements. Find the maximum score you can get.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤500). The description of the test cases follows.

The first line of each test case contains a single integer 𝑛 (1≤𝑛≤100) — the length of the array.

The second line of each test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤1000) — the given array.

Output
For each test case, output a single integer: the maximum possible score you can get after coloring some elements red according to the statement.

Example
inputCopy
4
3
5 4 5
3
4 5 4
10
3 3 3 3 4 1 2 3 4 5
9
17 89 92 42 29 92 14 70 45
outputCopy
7
6
10
97

Note:
In the first test case, you can color the array as follows: [5,4,5]. Your score is max([5,5])+size([5,5])=5+2=7. This is the maximum score you can get.

In the second test case, you can color the array as follows: [4,5,4]. Your score is max([4,4])+size([4,4])=4+2=6. This is the maximum score you can get.

In the third test case, you can color the array as follows: [3,3,3,3,4,1,2,3,4,5]. Your score is max([3,3,4,3,5])+size([3,3,4,3,5])=5+5=10. This is the maximum score you can get.
"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    max_red = 0
    count_red = 0
    max_aux = 0
    count_aux = 0

    for i in range(n):
        if i % 2 == 0:  
            count_red += 1
            max_red = max(max_red, a[i])
        else:          
            count_aux += 1
            max_aux = max(max_aux, a[i])

    if max_red >= max_aux:
        print(max_red + count_red)
    else:
        print(max_aux + count_aux)