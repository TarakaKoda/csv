# File Object

# f = open("Scope.py","r")
# # f_read = open("Scope.py","r")
# # f_write = open("Scope.py","w")
# # f_append = open("Scope.py","a")
# # f_read_write = open("Scope.py","r+")
# print(f.name)
# print(f.mode)
# print(f.read())
# f.close()
# # If we didn't close the file
# Resource leaks: When a file is opened in Python, the operating system reserves some resources to manage the file,
# such as file handles and memory buffers. If you don't close the file object after you're done using it,
# those resources may not be released immediately, which can lead to resource leaks. Over time, if you keep opening
# and not closing files, you may run out of available resources and your program may crash.

# Data loss: If you don't close a file object after you've written data to it, there's a risk that the data you wrote
# won't be saved to the file. This can happen if the operating system's buffers aren't flushed to disk before the
# file object is garbage collected. If the program terminates abruptly or the file is closed without being properly
# flushed, some or all of the data you wrote may be lost.

# Inconsistent file state: If you don't close a file object after you've read data from it, you may end up with an
# inconsistent file state. For example, if you read some but not all of the data in a file, and then close the file
# without reading the rest, the file may be left in an inconsistent state where some data has been read and some
# hasn't. This can cause errors or unexpected behavior if you try to read from the file again later.

# with open("Scope.py", "r") as f:
    # size_to_read = 100
    # f_content = f.read(size_to_read)
    # print(f_content,end="")
    # f.seek(0)
    # f_content = f.read(size_to_read)
    # print(f_content,end="")

    # print(f.tell())
    # while len(f_content) > 0:
    #     print(f_content, end="*")
    #     f_content = f.read(size_to_read)
    # f_content = f.read(100)
    # print(f_content, end="")
    # f_content = f.read(100)
    # print(f_content, end="")


    # for line in f:
    #     print(line, end="")
    # f_contents = f.readline()
    # print(f_contents, end="")
    # f_contents = f.readline()
    # print(f_contents, end="")
    # f_contents = f.readline()
    # print(f_contents)

# with open("Scope2.py","w") as f:
#     f.write('print("Hello world")')
#     f.seek(0)
#     f.write("print('rello world')")
#

with open("Scope.py","r") as rf:
    with open("copy Scope.py", "w") as wf:
        for line in rf:
            wf.write(line)

# working with image (copy image by using binary mode bytes)
# using for loop
# with open("Scope.jng","rb") as rf:
#     with open("copy Scope.jpg", "wb") as wf:
#         for line in rf:
#             wf.write(line)

# using while loop
# with open("Scope.jng","rb") as rf:
#     with open("copy Scope.jpg", "wb") as wf:
#         rf_chunk = 4096
#         rf_chunk = rf.read(rf_chunk)
#         while len(rf_chunk) > 0:
#             wf.write(rf_chunk)
#             rf_chunk = rf.read(rf_chunk)

