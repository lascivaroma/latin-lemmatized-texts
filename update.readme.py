import lxml.etree as ET
import glob
import tabulate
from collections import Counter
import tqdm


counter = Counter()

for file in tqdm.tqdm(glob.glob("lemmatized/xml/*.xml")):
	data = ET.parse(file)
	counter.update((pos for pos in data.xpath("//@pos")))

stats = tabulate.tabulate(sorted(list(counter.items()), key=lambda x: x[0]), headers=["POS", "Tokens"], tablefmt="github")

tokens = sum(list(counter.values()))
tokens_nopunct = sum(list([counter[pos] for pos in counter if pos not in {"PUNC"}]))

with open("README.md", "r") as f:
	out = []
	ignore = False
	for line in f:
		if ignore:
			if line.startswith("<!---END-STATS--->") or line.startswith("<!--END-NB-->"):
				ignore = False
			else:
				continue
			
		out.append(line)
		
		if line.startswith("<!---START-STATS--->"):
			out.append(stats+"\n")
		elif line.startswith("<!--START-NB-->"):
			out.append(f"**Number of tokens**: {tokens:,} ({tokens_nopunct:,} without punctuation)\n")

			ignore = True
			
with open("README.md", "w") as f:
	f.write("".join(out))