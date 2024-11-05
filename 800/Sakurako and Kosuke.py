"""
A. Sakurako and Kosuke
time limit per test 1 second
memory limit per test 256 megabytes
Sakurako and Kosuke decided to play some games with a dot on a coordinate line. The dot is currently located in position 𝑥=0. They will be taking turns, and Sakurako will be the one to start.

On the i-th move, the current player will move the dot in some direction by 2⋅i-1 units. Sakurako will always be moving the dot in the negative direction, whereas Kosuke will always move it in the positive direction.

In other words, the following will happen:

Sakurako will change the position of the dot by -1, x=-1 now
Kosuke will change the position of the dot by 3, x=2 now
Sakurako will change the position of the dot by -5, x=-3 now
⋯
They will keep on playing while the absolute value of the coordinate of the dot does not exceed n. More formally, the game continues while −𝑛≤𝑥≤𝑛. It can be proven that the game will always end.

Your task is to determine who will be the one who makes the last turn.

Input
The first line contains one integer t (1≤t≤100) — the number of games that Sakurako and Kosuke played.

Each game is described by one number n (1≤n≤100) — the number that defines the condition when the game ends.

Output
For each of the t games, output a line with the result of that game. If Sakurako makes the last turn, output "Sakurako" (without quotes); else output "Kosuke".
Example
input:
4
1
6
3
98
output:
Kosuke
Sakurako
Kosuke
Sakurako
"""

def determine_winner(n):
    return "Sakurako" if n % 2 == 0 else "Kosuke"


t = int(input())      
for _ in range(t):
    n = int(input())  
    winner = determine_winner(n)
    print(winner)


