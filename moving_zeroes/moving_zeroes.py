'''
Input: a List of integers
Returns: a List of integers
'''

def moving_zeroes(arr):
    # count = 0
    # # Your code here
    # for i in range(n):
    #     if arr[i] != 0:
    #         arr[count] = arr[i]
    #         count += 1
    # while count < n:
    #     arr[count] = 0
    #     count += 1

    count_zero = arr.count(0)
    while 0 in arr:
        arr.remove(0)
    for n in range(count_zero):
        arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    n = len(arr)

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")