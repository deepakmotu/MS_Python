import os

# This is to get the directory that the program
# is currently running in.
#dir_path = os.path.dirname(os.path.realpath(__file__))
class file_search:
    def FS(self, Fname, ext, Spath):
        dir_path = os.path.dirname(Spath)
        print(f'Searching {Fname}{ext} in {dir_path}')
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                print(root)
                # change the extension from '.mp3' to
                # the one of your choice.
                if file.endswith(ext):
                    if file.startswith(Fname):
                        run = root + '\\' + str(file)
                        print(run)
                     #   with open(run, 'r') as fp:
                      #      fp.readlines()
                        print(run)
                        exit(0)
        print('File Not Found')

fse = file_search()
fse.FS('Deepak','.mp3','E:')
