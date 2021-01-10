from os import walk
from os.path import splitext
from os.path import join
from xml.etree import cElementTree as ET
from xml.etree.ElementTree import ParseError

directory = input('Directory: ')
extension = input('Extension: ')

text_file_paths = []
for root, dirs, files in walk(directory):
    for f in files:
        if splitext(f)[1].lower() == extension:
            text_file_paths.append(join(root, f))

lines = []

for text_file_path in text_file_paths:
    try:
        with open(text_file_path, 'r', encoding='utf-8') as f:
            root = ET.fromstring(f.read())
    except (ParseError, UnicodeDecodeError):
        continue
    for post in root.findall('post'):
        lines.append(post.text.strip())

with open('output.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
