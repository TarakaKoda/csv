import os
os.chdir("D:\\DownloadMaster")
# print(os.getcwd())
# print(os.listdir())
# for f in os.listdir():
#     file_name, file_ext = os.path.splitext(f)
#     file_artist, file_song = file_name.split("-")
#     file_num, file_artist_name = (file_artist.split("."))
#     file_ext = file_ext.strip()
#     file_artist_name = file_artist_name.strip()
#     file_num = file_num.strip().zfill(2)
#     file_song = file_song.strip()
#     new_name = (f"{file_num}. {file_song} by {file_artist_name}{file_ext}")
#     os.rename(f,new_name)

# Copying a video file
# for f in os.listdir():
#     with open(f,"rb") as rf:
#         with open("copy"+f,"wb") as wf:
#             for line in rf:
#                 wf.write(line)

# Deleting a file if the name of the is starts with "copy"
# for filename in os.listdir():
#     if filename.startswith("copy"):
#         os.remove(filename)
#         print(f"Deleted {filename}")











