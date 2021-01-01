from distutils.core import setup
import setuptools
VERSION = "1.0.4"
long_description = ""
with open("README.md", "r", encoding="utf-8") as file:
	long_description = file.read()
setup(
name='lyricsScraper', 
packages=['lyricsScraper'],
version=VERSION,
description='You can get lyrics from genius with many usefull functions.',
long_description=long_description,
long_description_content_type="text/markdown",
author='Ahmet Metin',               
author_email='ahmet.metin817@gmail.com',   
url='https://github.com/letsplaywithstrings/lyrcisScraper',
download_url=f'https://github.com/letsplaywithstrings/lyrcisScraper/archive/{VERSION}.tar.gz',
keywords=['Lyrics', 'Artist',],
install_requires=['requests','BeautifulSoup'],
classifiers=[
'Development Status :: 4 - Beta',
'Intended Audience :: Developers',
'Topic :: Software Development :: Build Tools',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python :: 3.6',
'Programming Language :: Python :: 3.7',
'Programming Language :: Python :: 3.8',
'Programming Language :: Python :: 3.9',
],
)
