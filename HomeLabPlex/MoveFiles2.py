import shutil

import os



source_dir = '/home/chase/Documents/Public Storage' 

target_dir = '/home/chase/Documents/Movies'



file_names = os.listdir(source_dir)



for file_name in file_names:

    shutil.move(os.path.join(source_dir, file_name), target_dir)
