import csv
# import os
with open("sample data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("new name.csv","w") as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)


# with open("sample data.csv","a") as wf:cd
#     wf.seek(0)
#     wf.write("first name,last name, email")
