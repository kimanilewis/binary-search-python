  
  
# Returns index of x if it is present 
# in arr[], else return -1 
#
# @author lewis.kimani<kimanilewi@gmail.com>
#
def binarySearch(arr, x): 
    left = 0
    right = len(arr) 
    while (left <= right): 
        m = left + ((right - left) // 2) 
  
        result = (x == arr[m]) 
  
        # Check if string is present at mid 
        if (result == 0): 
            return m - 1
  
        # If string greater, ignore left half 
        if (res > 0): 
            left = m + 1
  
        # If string is smaller, ignore right half 
        else: 
            right = m - 1
  
    return -1
  
# Main  
if __name__ == "__main__": 
  
    arr = ["This", "is", "a", "sample", "binary", "test"]; 
    x = "binary"
    result = binarySearch(arr, x) 
  
    if (result == -1): 
        print("String not found") 
    else: 
        print("String found at index" , 
                                 result) 
  