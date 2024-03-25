import json
import os.path
from glob import glob
mafs = glob('input\\*.maFile')

if not os.path.exists('out'):
    os.mkdir('out')

for mafile in mafs:
    data = json.loads(open(mafile).readline())
    filename = data['account_name']
    with open(f'out\\{filename}.maFile', 'w+') as f:
        f.write(json.dumps(data))
