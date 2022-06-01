import pandas as pd


cornell_cites = open('raw/webkb/cornell.cites', 'r')
texas_cites = open('raw/webkb/texas.cites', 'r')
washington_cites = open('raw/webkb/washington.cites', 'r')
wisconsin_cites = open('raw/webkb/wisconsin.cites', 'r')

cornell_cites_lines = cornell_cites.read().splitlines()
texas_cites_lines = texas_cites.read().splitlines()
washington_cites_lines = washington_cites.read().splitlines()
wisconsin_cites_lines = wisconsin_cites.read().splitlines()

cornell_content = pd.read_csv('raw/webkb/cornell.content', sep='\t', header=None)
texas_content = pd.read_csv('raw/webkb/texas.content', sep='\t', header=None)
washington_content = pd.read_csv('raw/webkb/washington.content', sep='\t', header=None)
wisconsin_content = pd.read_csv('raw/webkb/wisconsin.content', sep='\t', header=None)

links = []

for lines in [cornell_cites_lines, texas_cites_lines, washington_cites_lines, wisconsin_cites_lines]:
    for line in lines:
        link1, link2 = line.split(' ')
        if link1 not in links:
            links.append(link1)
        if link2 not in links:
            links.append(link2)

def link_to_number(x):
    return links.index(x) + 10000

with open('data/webkb/link', 'a') as f:
    for lines in [cornell_cites_lines, texas_cites_lines, washington_cites_lines, wisconsin_cites_lines]:
        for line in lines:
            link1, link2 = line.split(' ')
            f.write(str(link_to_number(link1)) + ' ' + str(link_to_number(link2)) + '\n')

merged_df = pd.concat([cornell_content, texas_content, washington_content, wisconsin_content])
merged_df[0] = [link_to_number(i) for i in merged_df[0]]
merged_df.to_csv('data/webkb/node', sep='\t', header=False, index=False)
