def get_files_in_folder(path):
    import glob
    paths=glob.glob(path)
    files=[]
    for file in paths:      
        files.append(file.split('\\')[-1])        
    return files


def save_listo_to_txt(list, name):
    print('saving error logs')
    with open(str(name) +'.txt', 'w') as filehandle:
        for el in list:
            filehandle.write('%s\n' % el)

    with open('file_name.txt', 'w') as filehandle:
        for index in asset_list:
            filehandle.write('%s\n' % index)

            
def get_files_in_dir(path):
    import os
    return os.listdir(path)
    
