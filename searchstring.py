import webbrowser

automated = True
homecage = True
activity = False
behavior = True
pheno = True

combiner = ' AND '

substrings = {}

substrings["pubmed"] = 'https://pubmed.ncbi.nlm.nih.gov/?term='

if automated:
    substrings["auto"] = 'automat*'
else:
    substrings["auto"] = ''

if homecage:
    substrings["homecage"] = '("home cage" OR "homecage" OR "home-cage")'
else:
    substrings["homecage"] = ''

if activity:
    substrings["activity"] = '(activity OR monitoring)'
else:
    substrings["activity"] = ''

if behavior:
    substrings["behavior"] = '("behavior" OR "behaviour")'
else:
    substrings["behavior"] = ''

if pheno:
    substrings["pheno"] = 'phenotyping'
else:
    substrings["pheno"] = ''

substrings["custom"] = ''

pubmed_search_string =  substrings["pubmed"] + \
                        substrings["auto"] + combiner + \
                        substrings["homecage"] + combiner + \
                        substrings["activity"] + combiner + \
                        substrings["behavior"] + combiner + \
                        substrings["pheno"] + combiner + \
                        substrings["custom"]

print(pubmed_search_string)

webbrowser.open(pubmed_search_string)  # Go to example.com