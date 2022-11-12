import os, shutil

folders =[
    fr"C:\Users\{os.getlogin()}\AppData\Local\Temp",
    r"C:\Windows\Temp",
    r"C:\Windows\SoftwareDistribution\Download"
]

for folder in folders:
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)

        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                print(f"Deleted fail {file_name}")

            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Deleted directory {file_name}")

        except Exception as x:
            print(f"Failed to delete {file_path}. Reson: {x}")