# pychordpro

pychordpro is a simple Python package that allows to easly interact with the [ChordPro](https://www.chordpro.org/) file format.

## Installation

To install the package you can simply type:

```
pip install pychordpro
```

## Example Usage

```py
from pychordpro import Song

song = Song(filename='mysong.cho', notes='latin')
song.open()

print(song.read())

song.transpose(1)
song.config('config.json')

song.compile()
```

## Methods

All the functions and methods are basically Python transcriptions of the [command line options](https://www.chordpro.org/chordpro/using-chordpro/) for ChordPro, so you will have to install the ChordPro file transformation program as well.

However you can easily see the source code [here](https://github.com/FraKappa/pychordpro/blob/master/pychordpro/chordpro.py).

ChordPro installation guides for:
* [Linux](https://www.chordpro.org/chordpro/chordpro-install-on-linux/)
* [Windows](https://www.chordpro.org/chordpro/chordpro-install-on-windows/)
* [Mac OS/X](https://www.chordpro.org/chordpro/chordpro-install-on-mac-osx/)