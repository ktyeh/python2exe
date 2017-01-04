import sys
import shutil
import getopt
import os
from datetime import datetime
import site

numpy_core_path = site.getsitepackages()[-1] + '\\numpy\\core\\'  # where numpy-atlas.dll is
setup_py = '''from distutils.core import setup
import py2exe
 
setup(
    console = [{"script": "PLACEHOLDER"}]
)
'''

def main():
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"hyt:s:d:",["target=", "dirname=", "source=", "destination="])
    except getopt.GetoptError:
        print 'python -m python2exe.py -t <target.py>'
        sys.exit(2)

    dic = {
        'target': None,
        'dirname': None,
        'source': '.',
        'destination': 'D:\\python2exe\\',
        'overwrite': False,
    }
    for opt, arg in opts:
        if opt == '-h':
            # help function
            sys.exit()
        elif opt in ("-t", "--target"):
            dic['target'] = arg
        elif opt in ("--dirname"):
            dic['dirname'] = arg
        elif opt in ("s", "--source"):
            dic['source'] = arg
        elif opt in ("d", "--destination"):
            dic['destination'] = arg
        elif opt in ("y"):
            dic['overwrite'] = True

    if not os.path.exists(dic['source']):
        print '{} doesn\'t exist.'.format(dic['source'])
        sys.exit(2)
    if not os.path.exists(dic['destination']):
        os.makedirs(dic['destination'])

    if dic['target'] is None:
        print 'python -m python2exe.py -t <target.py>'
    elif dic['target'] not in os.listdir('.'):
        print '{} not found in current directory.'.format(dic['target'])
        sys.exit(2)
    elif dic['target'][-3:] != '.py':
        print 'target should be a python script'
        sys.exit(2)

    if dic['dirname'] is None:
        dic['dirname'] = dic['target'][:-3]
	
	print dic

    if os.path.exists(dic['destination'] + '\\' + dic['dirname']):
        if dic['overwrite']:
            shutil.rmtree(dic['destination'] + '\\' + dic['dirname'])
        else:
            ret = raw_input('{} already exists. Overwrite it? (yes/no)'.format(dic['dirname'])).lower()
        if ret == 'y' or ret == 'yes':
            shutil.rmtree(dic['destination'] + '\\' + dic['dirname'])
        else:
            sys.exit(2)

    os.chdir(dic['source'])
    if 'numpy-atlas.dll' not in os.listdir('.'):
        shutil.copy(numpy_core_path+'numpy-atlas.dll', '.\\')
    with open('.\\setup.py', 'w') as f:
        f.write(setup_py.replace('PLACEHOLDER', dic['target']))
    if 'dist' in os.listdir('.'):  # just in case
        shutil.rmtree('.\\dist')
    os.system('python setup.py py2exe')
    shutil.rmtree('.\\build')
    os.remove('.\\numpy-atlas.dll')
    os.remove('.\\setup.py')

    version = datetime.strftime(datetime.today(), '%y%m%d%H%M') + '.vsn'
    open('.\\dist\\'+version, 'w').close()

    os.rename('dist', dic['dirname'])
    shutil.move(dic['dirname'], dic['destination']+'\\')

if __name__ == '__main__':
    main()
