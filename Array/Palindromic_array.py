# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    for i in range(len(arr)):
        cpy = arr[i]
        sum = 0
        while(cpy!=0):
            rem = cpy % 10
            sum = sum * 10 + rem
            cpy = int(cpy / 10)
        if(sum!=arr[i]):
            return False
        else:
            continue
    return True
            