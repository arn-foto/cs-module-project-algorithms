# '''
# Input: a List of integers where every int except one shows up twice
# Returns: an integer
# '''

# # Single Number

# Given a non-empty array of integers where every element appears twice except for one. Find that single number. You may assume that there will _always_ be _one_ odd-number-out and every other number in the input shows up exactly twice.  

# ## Examples
# ```
# Sample input: [2, 2, 1]
# Expected output: 1
# ```

# ```
# Sample iput: [4, 1, 2, 1, 2]
# Expected output: 4
# ```

# Can you implement a solution that finds the single number in _one_ pass through the input array with `O(1)` space complexity?

# ## Testing
# Run the test file by executing `python test_single_number.py`. 

def single_number(arr):
    
    n = []
    for x in arr:
        n.append(arr.count(x))
    for i in range(len(n)):
        if n[i] == 1:
            return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")