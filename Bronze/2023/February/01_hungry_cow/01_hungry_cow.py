"""
ID: mck15821
LANG: PYTHON3
PROG: Watching Mooloo
"""
# http://www.usaco.org/index.php?page=viewproblem2&cpid=1299

N, T = map(int, input().split())
food_count = 0  # final output
last_day_with_food = 0  # furthest day with food

for _ in range(N):
    day, volume = map(int, input().split())
    if last_day_with_food < day:
        last_day_with_food = day - 1
    # has enough food until end
    if last_day_with_food + volume >= T:
        # last_day_with_food will never be bigger than T
        food_count += T - last_day_with_food
        break
    food_count += volume
    last_day_with_food += volume

print(food_count)
