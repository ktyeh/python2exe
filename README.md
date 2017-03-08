# python2exe(py) => exe

## Abstract

py2exe(http://www.py2exe.org/) converts Python scripts into executable Windows programs. However, it leads to an error when scripts import "numpy".

python2exe.py is using py2exe with "numpy problem" fixed and records the timestamp of building.

## Installation

	git clone https://github.com/ktyeh/python2exe.git

## Usage

### python python2exe.py -t &lt;target.py> [-D &lt;dirname>] [-s &lt;source>] [-d &lt;destination>]

#### Args:
* target.py: name of the main Python script

* dirname: name of directory, defaultly set as same as target

* source: path of target.py, defaultly set as current directory

* destination: output path, defaultly set as current directory

#### Examples:
	cd python2exe
	python python2exe.py -t test.py -D DIRNAME -s source -d dist

And test.exe would be in ./dist/DIRNAME

Run ./dist/DIRNAME/test.exe
![alt tag](https://github.com/ktyeh/python2exe/blob/master/success.jpg)