# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggieSize(biggieList):
    for idx in range(0, len(biggieList), 1):
        if biggieList[idx] < 0:
            biggieList[idx] = "big"
    return biggieList

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it


def countPositives(numList):
    sum = 0
    for idx in range(0,len(numList), 1):
        if numList[idx] > 0:
            sum+=1
        numList[len(numList)-1] = sum
        
    print(numList)

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sumTotal(total_list):
    sum = 0
    for idx in range(len(total_list)):
        sum+=total_list[idx]

    return sum

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(average_list):
    sum = 0
    avg = 0
    for idx in range(len(average_list)):
        sum += average_list[idx]
    
    avg = sum/len(average_list)
    
    return avg


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(lengthy_list):
    counter = 0
    for i in range(0, len(lengthy_list), 1):
        counter+=1

    print(counter)
     

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(min_list):
        if len(min_list) == 0:
            return False
        min = 0
        for idx in range(0, len(min_list), 1):
            if min > min_list[idx]:
                min = min_list[idx]
            
        print(min)


# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(max_list):
    if len(max_list) == 0:
        return False
    max = 0
    for idx in range(len(max_list)):
        if max_list[idx] > max:
            max = max_list[idx]
    print(max)


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimateAnalysis(ultimate_list):
    ultimateResults = {
        'sumTotal' : None,
        'average' : None,
        'minimum' : None,
        'maximum' : None,
        'length' : 0
    }
    if len(ultimate_list) == 0:
        return ultimateResults
    ultimateResults['maximum'] = ultimate_list[0]
    ultimateResults['minimum'] = ultimate_list[0]
    ultimateResults['sumTotal'] = 0
    for idx in range(len(ultimate_list)):
        if ultimate_list[idx] > ultimateResults['maximum']:
            ultimateResults['maximum'] = ultimate_list[idx]
        elif ultimate_list[idx] < ultimateResults['minimum']:
            ultimateResults['minimum'] = ultimate_list[idx]
    for idx in range(len(ultimate_list)):
        ultimateResults['sumTotal']+=ultimate_list[idx]

    ultimateResults['average'] = ultimateResults['sumTotal']/len(ultimate_list)
    ultimateResults['length'] = len(ultimate_list)
    
    return ultimateResults

    

    


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

#def reverseList(list_to_reverse):
 #   list_to_reverse.reverse()
##   print(list_to_reverse)


def reverse_list(list_to_reverse):
    print(list_to_reverse[::-1])
    return list_to_reverse

def reversingList(switcheroo):
    for idx in range(len(switcheroo)):
        movingIndex = switcheroo.pop()
        switcheroo.insert(idx,movingIndex)
    print(switcheroo)
        



