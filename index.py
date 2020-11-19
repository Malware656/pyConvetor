from PIL import Image
import os

def gcon(name):
    if '"' in name:
        name = name.replace('"', '')
    yes = ["YES", "Y", "y"]
    no = ['NO', "N", "n"]
    # print(os.path.split(name))
    if os.path.isfile(name):
        img = Image.open(name)
        splitted_name = os.path.splitext(name)[0]
        img.save(splitted_name + '.png')
        print("PROCESSING : " + splitted_name + '.png')
        img.close()

    else:
        query = input("""The specified location is a Folder\nDo you want to proceed further [Y] or [N] : """)

        if query in yes:
            
            for roots, dirs, files in os.walk(name):
                for file in files:
                    file_name = roots + "\\" + file
                    img = Image.open(file_name)
                    folder_name = file.split('.')[1]
                    img.save(roots + "\\" + file.split('.')[0] + '.png')
                    print("PROCESSING : " + roots + "\\" + file.split('.')[0] + '.png')
                    img.close()
        
        else:
            print("Thank you for using GCoverter !!")
        

while True:
    name = input('Enter FIle or FOlder : ')

    if name != '' and name != 'q':
        gcon(name)
    if name in ['q', 'Q']:
        print('Quitting..')
        break

    else:
        print("Enter Valid Filename or Folder !")
