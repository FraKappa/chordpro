from setuptools import setup

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name='pychordpro',
    packages=['pychordpro'],
    version='0.1',
    license='MIT',
    description='A simple package to create, edit, compile files in the ChordPro file format.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kappa',
    author_email='f.cappetti.05@gmail.com',
    url='https://github.com/FraKappa/pychordpro',
    download_url='https://github.com/FraKappa/pychordpro/archive/v_01.tar.gz',
    keywords=['chordpro', 'music'],
    install_requires=[

    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8'
  ]
)
