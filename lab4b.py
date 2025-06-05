#!/usr/bin/env python3
# Author ID: 114163223

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def join_lists(l1, l2):
    return list(set(l1).union(set(l2)))

def match_lists(l1, l2):
    return list(set(l1).intersection(set(l2)))

def diff_lists(l1, l2):
    return list(set(l1) ^ set(l2))
    # result = []
    # for item in l1 + l2:
    #     if (item in l1) != (item in l2) and item not in result:
    #         result.append(item)
    # return result
    

# def create_dictionary(keys, values):
#     # Place code here - refer to function specifics in section below

# def shared_values(dict1, dict2):
#     # Place code here - refer to function specifics in section below

if __name__ == '__main__':
    list1 = list(range(1, 10))
    list2 = list(range(5, 15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))
    # york = create_dictionary(list_keys, list_values)
    # print('York: ', york)
    # common = shared_values(dict_york, dict_newnham)
    # print('Shared Values', common)