"""
time limit per test 1 second
memory limit per test 256 megabytes
Matthew is given two strings 𝑎 and 𝑏, both of length 3. He thinks it's particularly funny to create two new words by swapping the first character of 𝑎 with the first character of 𝑏. He wants you to output 𝑎 and 𝑏 after the swap.

Note that the new words may not necessarily be different.

Input
The first line contains 𝑡 (1≤𝑡≤100)  — the number of test cases.

The first and only line of each test case contains two space-separated strings, 𝑎 and 𝑏, both of length 3. The strings only contain lowercase Latin letters.

Output
For each test case, after the swap, output 𝑎 and 𝑏, separated by a space.

Example
input:
6
bit set
cat dog
hot dog
uwu owo
cat cat
zzz zzz

output:
sit bet
dat cog
dot hog
owu uwo
cat cat
zzz zzz
"""
t = int(input())

for _ in range(t):
    s = input().split(" ")
    a = s[0]
    b = s[1]

    first = b[0]
    last = a[0]
    new_first = first + s[0][1:]
    new_last = last + s[1][1:]
    print(new_first + " "+ new_last)
