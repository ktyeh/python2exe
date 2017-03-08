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
        opts, args = getopt.getopt(argv, "hyt:s:d:D:", ["target=", "dirname=", "source=", "destination="])
    except getopt.GetoptError:
        print 'python python2exe.py -t <target.py> [-D <dirname>] [-s <source>] [-D <destination>]'
        sys.exit(2)

    dic = {
        'target': None,
        'dirname': None,
        'source': '.',
        'destination': '.',
        'overwrite': False,
    }
    for opt, arg in opts:
        if opt == '-h':
            # help function
            print 'python python2exe.py -t <target.py> [-D <dirname>] [-s <source>] [-D <destination>]'
            sys.exit()
        elif opt in ("-t", "--target"):
            dic['target'] = arg
        elif opt in ("-D", "--dirname"):
            dic['dirname'] = arg
        elif opt in ("-s", "--source"):
            dic['source'] = arg
        elif opt in ("-d", "--destination"):
            dic['destination'] = arg
        elif opt in ("-y"):
            dic['overwrite'] = True

    print dic

    if not os.path.exists(dic['source']):
        print '{} doesn\'t exist.'.format(dic['source'])
        sys.exit(2)
    if not os.path.exists(dic['destination']):
        os.makedirs(dic['destination'])

    owd = os.getcwd()

    if dic['target'] is None:
        print 'python python2exe.py -t <target.py> [-D <dirname>] [-s <source>] [-D <destination>]'
        sys.exit(2)
    elif dic['target'] not in os.listdir(dic['source']):
        print '{} not found in {}.'.format(dic['target'], dic['source'])
        sys.exit(2)
    elif dic['target'][-3:] != '.py':
        print 'target should be a python script'
        sys.exit(2)

    if dic['dirname'] is None:
        dic['dirname'] = dic['target'][:-3]

    # to be simplified
    if os.path.exists(dic['destination'] + '\\' + dic['dirname']) and not dic['overwrite']:
        ret = raw_input('{} already exists. Overwrite it? (yes/no) '.format(dic['dirname'])).lower()
        if not ret == 'y' and not ret == 'yes':
            sys.exit(2)
        shutil.rmtree(dic['destination'] + '\\' + dic['dirname'])

    os.chdir(dic['source'])

    if 'numpy-atlas.dll' not in os.listdir('.'):
        shutil.copy(numpy_core_path+'numpy-atlas.dll', '.\\')

    with open('.\\setup.py', 'w') as f:
        f.write(setup_py.replace('PLACEHOLDER', dic['target']))

    if 'dist' in os.listdir('.'):  # just in case
        shutil.rmtree('.\\dist')

    os.system('python setup.py py2exe')

    try:
        shutil.rmtree('.\\build')
    except:
        pass

    try:
        os.remove('.\\numpy-atlas.dll')
    except:
        pass

    try:
        os.remove('.\\setup.py')
    except:
        pass

    ts = datetime.strftime(datetime.today(), '%y%m%d%H%M') + '.ts'
    open('.\\dist\\'+ts, 'w').close()

    os.chdir(owd)
    if os.path.exists(dic['destination'] + '\\' + dic['dirname']):
        shutil.rmtree(dic['destination'] + '\\' + dic['dirname'])
    shutil.move(dic['source'] + '\\dist', dic['destination'] + '\\' + dic['dirname'])

if __name__ == '__main__':
    main()
