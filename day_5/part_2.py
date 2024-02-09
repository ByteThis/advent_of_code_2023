def convert(r):
    to_convert = [r]
    converted = []

    for m in conversions:

        for c in m:
            k = c[2]
            value_range = (c[1], c[1] + k)
            map_range = (c[0], c[0] + k)

            temp = []
            while to_convert:
                ran = to_convert.pop(0)

                if ran[0] >= value_range[0] and ran[1] <= value_range[1]:
                    # All values within range
                    #            V     V
                    #        R               R
                    #        M               M
                    intersect_from_begining = ran[0] - value_range[0]
                    mapped = (map_range[0]+intersect_from_begining, map_range[0]+intersect_from_begining + (ran[1]-ran[0]))
                    converted.append(mapped)

                # no values within range
                elif ran[1] < value_range[0] or ran[0] > value_range[1]:
                    temp.append(ran)

                # intersection
                else:

                    if ran[0] < value_range[0] and ran[1] <= value_range[1]:
                        temp.append((ran[0], value_range[0]-1))
                        # cut begining of range
                        #         V    X----V
                        #              R           R
                        #              M----X      M

                        intersect_from_begining = ran[1]-value_range[0]
                        mapped = (map_range[0], map_range[0]+intersect_from_begining)
                        converted.append(mapped)


                    elif ran[0] >= value_range[0] and ran[1] > value_range[1]:
                        temp.append((value_range[1]+1, ran[1]))
                        # cut end of range
                        #             V----X       V
                        #        R         R
                        #        M         M

                        intersect_from_begining = ran[1] - value_range[0]
                        mapped = (map_range[0]+intersect_from_begining, map_range[1])
                        converted.append(mapped)


                    elif ran[0] < value_range[0] and ran[1] > value_range[1]:
                        # cut middle of range in 3 pieces
                        #     V                   R
                        #          R         R
                        #          M         M

                        temp.append((ran[0], value_range[0] - 1))
                        temp.append((value_range[1] + 1, ran[1]))
                        converted.append(map_range)

            to_convert += temp
            if not to_convert and not temp:
                break

        to_convert = converted + temp
        converted = []

    return to_convert


file = open("input").read().strip().split("\n\n")
seeds = [int(x) for x in file[0].replace("seeds: ", "").split(" ")]
conversions = [
    [[int(y) for y in x.split(" ")] for x in file[i].splitlines()[1::]]
    for i in range(1, 8)
]

ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

converted_seeds = []
for x in ranges:
    converted_seeds.append([x[0] for x in convert(x)])

final = min([min(x) for x in converted_seeds])
print(final)
