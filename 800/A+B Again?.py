"""
A+B Again?
time limit per test 1 second
memory limit per test 256 megabytes
Given a two-digit positive integer 𝑛, find the sum of its digits.

Input
The first line contains an integer 𝑡 (1≤𝑡≤90) — the number of test cases.

The only line of each test case contains a single two-digit positive integer 𝑛 (10≤𝑛≤99).

Output
For each test case, output a single integer — the sum of the digits of 𝑛.

Example
input:
8
77
21
40
34
19
84
10
99
output:
14
3
4
7
10
12
1
18
"""

s = int (input())

for _ in range(s):
    t = input()
    suma = 0
    for i in t:
        suma+=int(i)
    print(suma)