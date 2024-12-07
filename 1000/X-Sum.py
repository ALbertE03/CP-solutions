"""
time limit per test 2 seconds
memory limit per test 256 megabytes
Timur's grandfather gifted him a chessboard to practice his chess skills. This chessboard is a grid 𝑎 with 𝑛 rows and 𝑚 columns with each cell having a non-negative integer written on it.

Timur's challenge is to place a bishop on the board such that the sum of all cells attacked by the bishop is maximal. The bishop attacks in all directions diagonally, and there is no limit to the distance which the bishop can attack. Note that the cell on which the bishop is placed is also considered attacked. Help him find the maximal sum he can get.

Input
The first line of the input contains a single integer 𝑡 (1≤𝑡≤1000) — the number of test cases. The description of test cases follows.

The first line of each test case contains the integers 𝑛 and 𝑚 (1≤𝑛≤200, 1≤𝑚≤200).

The following 𝑛 lines contain 𝑚 integers each, the 𝑗-th element of the 𝑖-th line 𝑎𝑖𝑗 is the number written in the 𝑗-th cell of the 𝑖-th row (0≤𝑎𝑖𝑗≤106)

It is guaranteed that the sum of 𝑛⋅𝑚 over all test cases does not exceed 4⋅104.

Output
For each test case output a single integer, the maximum sum over all possible placements of the bishop.

Example
input
4
4 4
1 2 2 1
2 4 2 4
2 2 3 1
2 4 2 4
2 1
1
0
3 3
1 1 1
1 1 1
1 1 1
3 3
0 1 1
1 0 1
1 1 0
output
20
1
5
3
"""

def max_bishop_sum(n, m, board):
    max_sum = 0
    
    for i in range(n):
        for j in range(m):
            current_sum = 0
            
            current_sum += board[i][j]
            
            x, y = i - 1, j - 1
            while x >= 0 and y >= 0:
                current_sum += board[x][y]
                x -= 1
                y -= 1
            
            
            x, y = i - 1, j + 1
            while x >= 0 and y < m:
                current_sum += board[x][y]
                x -= 1
                y += 1
            
       
            x, y = i + 1, j - 1
            while x < n and y >= 0:
                current_sum += board[x][y]
                x += 1
                y -= 1
            
            
            x, y = i + 1, j + 1
            while x < n and y < m:
                current_sum += board[x][y]
                x += 1
                y += 1
            
          
            max_sum = max(max_sum, current_sum)
    
    return max_sum


t = int(input())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    
    result = max_bishop_sum(n, m, board)
    results.append(result)

for res in results:
    print(res)