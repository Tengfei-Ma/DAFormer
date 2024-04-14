import os
import subprocess


def get_all_files_in_folder(folder_path):
    file_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_names.append(os.path.join('configs/experiments/local_exp8/', file))
    return file_names


folder_path = "F:/python_projects/DAFormer/configs/experiments/local_exp8"
all_files = get_all_files_in_folder(folder_path)

for config in all_files:
    command = 'python run_experiments.py --config ' + config
    subprocess.run(command)

print('over')
