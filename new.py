
# def student_details(n):
#     roll_no = [x for x in range(1, n + 1)]
#     names_of_students = []
#     details = {}
#     for i in range(1, n + 1):
#         name = input(f"enter {i} student name: ")
#         names_of_students.append(name)
#     for k,v in zip(roll_no, names_of_students):
#         details[k] = [v]
#     return details
#
#
# def address_of_students(info):
#     for k,v in info.items():
#         addressdict = {}
#         address = input(f"enter the address of \"{v}\":")
#         addressdict[f"adderss of {v}"] = address
#         v.extend(addressdict)
#
#     return info
#
#
# # def adding_details_to_info(info, addressdict):
# #     for k, v in info.items():
# #         for i,j in addressdict.items():
# #             if isinstance(v, list):
# #                 v = v.extend(v)
# #     return info
#
# info = student_details(5)
# addressdict = (address_of_students(info))
# # adding = adding_details_to_info(info, addressdict)
# print(addressdict)

my_dict = {
    "srinu": [{"address":"john"},{"name":"srinu"}]
}
l = []
dict3 = {"nam": "hvuyvuabcuab"}
l = my_dict['srinu']
for i in l:
    for k,v in i.items():
        print(k,v)

# my_dict["srinu"].append(dict3)
# print(my_dict)

