# python2exe(py) => exe

## Abstract

py2exe(http://www.py2exe.org/) converts Python scripts into executable Windows programs. However, it leads to an error when scripts import "numpy".

python2exe.py is using py2exe with "numpy problem" fixed and records the timestamp of building.

## Installation

>>git clone https://github.com/ktyeh/python2exe.git

## Usage

### python python2exe.py -t <target.py> [-D <dirname>] [-s <source>] [-D <destination>]

>>cd python2exe
>>python python2exe.py -t test.py -D DIRNAME -s source -d dist

And test.exe would be in ./dist/DIRNAME.

