def convert(v):
    seed = v
    for m in conversions:
        for c in m:
            k = c[2]
            seed_range = range(c[1], c[1]+k)

            if seed in seed_range:
                index = seed-c[1]
                seed = c[0]+index
                break

    return seed



file = open("input").read().strip().split("\n\n")
seeds = [int(x) for x in file[0].replace("seeds: ", "").split(" ")]
conversions = [
    [[int(y) for y in x.split(" ")] for x in file[i].splitlines()[1::]]
    for i in range(1, 8)
]

converted_seeds = []
for x in seeds:
    converted_seeds.append(convert(x))

print(min(converted_seeds))
