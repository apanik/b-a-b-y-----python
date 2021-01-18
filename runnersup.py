def second_max():
    # First Sorting Array
    n = int(input())
    arr = map(int, input().split())
    myset = set(arr)
    sorted_numbers = sorted(myset)
    # Taking 2nd Last value
    runners_up = sorted_numbers[-2]
    print(runners_up)


second_max()
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     myset = set(arr)
#     smax = second_max(myset)
