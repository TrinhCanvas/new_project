import sys
import subprocess
import importlib
import os

def read_txt(filepath):
    f = open(filepath, "r")
    libs=f.readlines()
    f.close()
    return libs
def write_txt(content):
    f = open("check_installed.txt", "a")
    f.write(content)
    f.close()
def init_file_n_folder():
    try:
        os.mkdir("cookies")
    except:
        pass
    try:
        with open('requirements.txt', 'w') as f:
            f.write('async-generator==1.10\n')
            f.write('attrs==22.1.0\n')
            f.write('requests==2.28.1\n')
            f.write('urllib3==1.26.12\n')
            f.write('selenium==4.4.3\n')
            f.write('beautifulsoup4==4.11.1\n')
            f.write('HTMLParser==0.0.2\n')
            f.write('chromedriver-autoinstaller==0.4.0\n')
            f.write('Pillow==9.2.0\n')
            f.write('lxml==4.9.1\n')
            f.write('Selenium-Screenshot==2.0.0\n')
        f.close()
    except:
        pass
    try:
        with open('check_installed.txt', 'w') as f:
            f.write('')
        f.close()
    except:
        pass

def installer():
    libs = read_txt("requirements.txt")
    for lib in libs:
        try:
            lib_no_ver=lib.split("==")[0]
            lib_import = importlib.import_module("{}".format(lib_no_ver))
            # print(lib_no_ver ,lib_import.__version__)
            write_txt("y")
        except:
            try:
                # print("Lib {} has not been installed. Installer started ...".format(lib))
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', '{}'.format(lib)], check=True)
                write_txt("y")
            except:
                write_txt("y")
                pass

def installer_caller():
    try:
        check_installed = read_txt("check_installed.txt")
        if len(check_installed)==0:
            installer()
        else:
            pass
    except:
        init_file_n_folder()
        check_installed = read_txt("check_installed.txt")
        if len(check_installed)==0:
            installer()
        else:
            pass