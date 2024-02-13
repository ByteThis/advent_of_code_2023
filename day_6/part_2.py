def distance_traveled(time, speed):
    return speed * (time - speed)

file = open("input").read().strip().split("\n")
times = [x for x in file[0].split(":")[1].strip().split(" ") if x]
distances = [x for x in file[1].split(":")[1].strip().split(" ") if x]

time = int("".join(times))
distance = int("".join(distances))

first_win = last_win = 0

for i in range(1, time):
    if distance_traveled(time, i) > distance:
        first_win = i
        break

for i in range(time-1, 0, -1):
    if distance_traveled(time, i) > distance:
        last_win = i
        break

winning_combo = last_win-first_win+1
print(winning_combo)