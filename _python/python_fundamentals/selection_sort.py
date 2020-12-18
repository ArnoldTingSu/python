



## method behavior development and testing

## num_list = [9,5,3,7,6,8,1,4,2,0]

# for min in range(len(num_list)):
#     min_index = min
#     for sort in range(min_index + 1, len(num_list)):
#         if num_list[min] > num_list[sort]:
#             print(f"it is {num_list[min]} versus {num_list[sort]}")
#             min_index = sort
#             print(f"so the number {num_list[min]} is higher")
#         else:
#             print(f"it is {num_list[min]} versus {num_list[sort]}")
#             print(f"so the number {num_list[min]} is smaller")
#         print("end of sort round")
#     print(min, "interation count")


num_list = [9,8,7,5]

for min in range(len(num_list)):
    compare_idx = min
    for sort in range(compare_idx + 1, len(num_list)):
        print("interation count")
        print(f" {num_list[compare_idx]} versus {num_list[sort]}")
        if num_list[compare_idx] > num_list[sort]:
            compare_idx = sort
    print(num_list)
    placeholder = num_list[compare_idx]
    num_list[compare_idx] = num_list[min]
    num_list[min] = placeholder
    print(num_list)