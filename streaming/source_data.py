import os
import json

data = []
for path, dirs, files in os.walk('./data'):
    for file in files[2:]:
        f = open(os.path.join(path, file)).readlines()
        data.extend(f)

d = []
for i in xrange(len(data)):
    if data[i] != '\n':
        d.append(json.loads(data[i]))

# ideally I would save it separated by '\n' and not in a list
with open("bartstrike.json", "w") as outfile:
    json.dump(d, outfile)

