import os
# from datetime import datetime
print(os.getcwd())
print(os.listdir())
# os.chdir('\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python')
# os.mkdir("python new")
# os.makedirs("python2\\test python")
# os.rmdir("python new")
# os.removedirs("python2\\test python")
# os.rename("python CheatSheets","python cheatsheet")
# a = os.getcwd()
# print(os.listdir("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Lists"))
# os.rename("functions","Functions.py")
# print(os.listdir("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Lists"))
# os.stat("python cheatsheet")
# print(sorted(os.listdir()))
# print(os.stat("python cheatsheet").st_size)
# mod_time = os.stat("python cheatsheet").st_mtime
# print(datetime.fromtimestamp(mod_time))
# print(os.getcwd())
# os.chdir("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\List")
# print(os.getcwd())
# for dirpath, dirnames, filemanes in os.walk('\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Lists'):
#     print("current path: ", dirpath)
#     print("directories: ", dirnames)
#     print("files: ", dirnames)
#     print()

# print(os.listdir("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Lists")

# print(os.environ.get("HOMEPATH"))
file_path = os.environ.get("HOMEPATH") + "python" # Not recommended because it will not add a \ to the created path.
file_path2 = os.path.join(os.environ.get("HOMEPATH"), "python")
# print(file_path)
# print(file_path2)
# print(os.listdir("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Lists"))
# print(os.path.basename("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Lists"))
# print(os.path.dirname("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Lists"))
# print(os.path.split("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Lists"))
# print(os.path.isdir("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python"))
# print(os.path.isfile("scope.py"))
# print(os.path.splitext("dictinories.py"))
# print(os.path.exists("\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Lists"))

# print(dir(os))