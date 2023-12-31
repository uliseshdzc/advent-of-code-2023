from functools import cache
import sys

# sys.argv[1]: part of the daily challenge to run
# sys.argv[2]: input file to use

"""
This code was based on the solution given by 'hyper-neutrino'
https://github.com/hyper-neutrino/advent-of-code
"""

def spring(tiles, nums, in_spring):
    if in_spring and nums[0] == 0:
        return 0
    return arrangements(tiles[1:], (nums[0] - 1, *nums[1:]), True)

def space(tiles, nums, in_spring):
    if in_spring and nums[0] > 0:
        return 0
    return arrangements(tiles[1:], nums[1:] if nums[0] == 0 else nums, False)

@cache
def arrangements(tiles, nums, in_spring=False):
    # Stop conditions for recursive function
    if tiles == "":
        return 1 if sum(nums) == 0 else 0
    if sum(nums) == 0:
        return 0 if '#' in tiles else 1

    # Get both possible results ('#' and '.')
    if tiles[0] == '?':
        return spring(tiles, nums, in_spring) + space(tiles, nums, in_spring)
    
    if tiles[0] == '#':
        return spring(tiles, nums, in_spring)
    
    if tiles[0] == '.':
        return space(tiles, nums, in_spring)

def main():

    count = 0

    with open(sys.argv[1]) as file:
        for line in file.read().splitlines():
            tiles, nums = line.split()
            nums = tuple(map(int, nums.split(',')))

            # For part 2
            if sys.argv[2] == '2':
                tiles = "?".join([tiles] * 5)
                nums *= 5

            count += arrangements(tiles, nums)

    return count

if __name__ == "__main__":
    print(main())