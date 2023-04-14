import tqdm
import glob
import lxml.etree as et


data = [
]

for file in tqdm.tqdm(glob.glob("lemmatized/xml/*.xml")):
    f = et.parse(file)
    title = str(f.xpath(".//t:title[1]/text()", namespaces={"t": "http://www.tei-c.org/ns/1.0"})[0])
    author = str(f.xpath(".//t:author[1]/text()", namespaces={"t": "http://www.tei-c.org/ns/1.0"})[0])
    words = int(f.xpath("count(.//t:w)", namespaces={"t": "http://www.tei-c.org/ns/1.0"}))
    data.append((author, title, str(words), file))
    del f

import csv

with open("corpus.csv", "w") as f:
    w = csv.writer(f)
    w.writerows(
    [["Author", "Title", "Word-count", "File"]] + sorted(data, key=lambda x: x[0] + x[1]))
