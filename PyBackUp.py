#! python3
# a program to backup all python codes in D and C to a Zip file
# into E:\codes\backup


import os, zipfile, shutil
driver1 = 'D:'
driver2 = 'E:'
save_to = r'C:\Users\mohamed alghaly\Downloads\Music'

os.chdir(save_to)      # the place where we save files
data = os.mkdir('python backup')

# a backup contains only python scripts 


# back up D drive
for foldername, subfolders, files in os.walk(driver1):  # walk D tree
    print(' I am now in %s '%(foldername))
    
    for file in files:   # append each python file
        if file.endswith('.py') or file.endswith('.pyw'):
            print('----Coping %s from %s ----'%(file, foldername)) 
            shutil.copy(os.path.join(foldername, file), os.path.join(os.getcwd(),'python backup'))  
            
print('Done with D partition ')
            


for foldername, subfolders, files in os.walk(driver2):
    print(' I am now in %s '%(foldername))
    
    for file in files:
        if file.endswith('.py') or file.endswith('.pyw'):
            print('----Coping %s from %s ----'%(file, foldername)) 
            shutil.copy(os.path.join(foldername, file), os.path.join(os.getcwd(),'python backup'))
            
print('Done with E partition ')
            
