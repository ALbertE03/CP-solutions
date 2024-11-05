"""
time limit per test 2 seconds
memory limit per test 256 megabytes
You are given a sequence of integers. Output the alternating sum of this sequence. In other words, output 𝑎1−𝑎2+𝑎3−𝑎4+𝑎5−…. That is, the signs of plus and minus alternate, starting with a plus.

Input
The first line of the test contains one integer 𝑡 (1≤𝑡≤1000) — the number of test cases. Then follow 𝑡 test cases.

The first line of each test case contains one integer 𝑛 (1≤𝑛≤50) — the length of the sequence. The second line of the test case contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤100).

Output
Output 𝑡 lines. For each test case, output the required alternating sum of the numbers.

Example
input:
4
4
1 2 3 17
1
100
2
100 100
5
3 1 4 1 5
output:
-15
100
0
10
"""

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = list(map(int,input().split()))
    suma = 0

    for i in range(len(numbers)):
        if i%2==0:
            suma+=numbers[i]
        else:
            suma-=numbers[i]

    print(suma)
