import os

# Function to calculate the average of given numbers
def avg(*num):
    moy = sum(num) / len(num)  # Calculate the average
    return moy

if __name__ == '__main__':
    # Open the output file (used in some environments like HackerRank)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Read input, convert it to a list of integers
    nums = list(map(int, input().split()))
    
    # Call the avg function with unpacked numbers
    res = avg(*nums)
    
    # Write the result to the output file, formatted to 2 decimal places
    fptr.write('%.2f' % res + '\n')

    # Close the file pointer
    fptr.close()
