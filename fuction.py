# def task_1(filter_list, number):
#     i = 0
#     while i < len(filter_list):
#         x = filter_list[i]
#         if type(x) == int:
#             number.append(x)
#         i += 1
#     return number
# print(task_1([1, 2, 3, "a", "b", 4], []))



# def task_2(list, list2):
#     i = 0
#     while i < len(list):
#         x = list[i]
#         if 6 < x:
#            list2.append(x)
#         i += 1
#     return list2
# print(task_3([7, 4, 17, 14, 12, 3], []))



# def task_3(lst, lst2):
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         if type(x) == int:
#             lst2.append(x)
#         i += 1
#     return lst2
# print(task_10([9, 2, "space", "car", "lion", 16], []))



# def task_4(string, lst):
#     i = 0
#     while i < len(string):
#         x = string[i]
#         if x == '1':
#             lst.append(True)
#         else:
#             lst.append(False)
#         i += 1
#     return lst
# print(task_4("100101", []))
# print(task_4("10", []))
# print(task_4("001", []))



# def task_5(lst, lst1, output_lst):
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         if x in lst1:
#             output_lst.append(1)
#         else:
#             output_lst.append(-1)
#         i  += 1
#     return output_lst
# print(task_5(["cat", "blue", "skt", "umbrells", "paddy"], ["cat", "blue", "sky", "umbrella", "paddy"], []))



# def task_6(lst):
#     result = 0
#     i = 0
#     while i < len(lst):
#         x = lst[i]
#         # result += x["budget"]
#         result += x.get("budget")
#         i+=1
#     return result
#
# print(task_6([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ]))



# def task_7(dict, resalt1):
#   o = 0
#   while o < len(dict):
#     x = dict[o]
#     for i in x.values():
#       if type(i) == int:
#         resalt1 = resalt1 + i
#   return resalt1
#
# print(task_7([
#   { "tile": "N", "score": 1 },
#   { "tile": "K", "score": 5 },
#   { "tile": "Z", "score": 10 },
#   { "tile": "X", "score": 8 },
#   { "tile": "D", "score": 2 },
#   { "tile": "A", "score": 1 },
#   { "tile": "E", "score": 1 }
# ], 0))



# def task_8(harflar):
#     a = {}
#     i = 0
#     while i < len(harflar):
#         x = harflar[i]
#         a[x] = x.upper()
#         i+=1
#     return a
# print(task_8(["a", "v", "y", "z"]))



# def task_9(person, nums, list, list2, resalt):
#     s = " ".join(person).split()
#     i = 0
#     while i < len(person):
#         x = person[i]
#         if x in nums:
#             list.append(x)
#         else:
#             list2.append(x)
#         i+=1
#     resalt.update({"LETTERS": len(list2), 'DIGITS': len(list)})
#     return resalt
# print(task_9("H3ll0 Wor1d", ['1', '2', '3', '4', '5', '6', '7', '8', '9',], [], [], {}))



# def task_10(object, num, rer):
#     i = 0
#     while i < len(object):
#         x = object[i]
#         rer = rer + x
#         rresalt = rer - int(num)
#         i+= 1
#         return rresalt
# print(task_10({"basketball": 12, "football": 10, "tennis": 20}, input("Num: "), 0))