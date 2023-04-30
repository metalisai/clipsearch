import argparse
import os
from annoy import AnnoyIndex
import jsonlines

EMB_DIM = 1536 # OpenAI ada v2

parser = argparse.ArgumentParser(description="Clip videos")
parser.add_argument('meta', type=str, help='database json file')

args = parser.parse_args()

t = AnnoyIndex(EMB_DIM, 'angular')
database_ann = os.path.splitext(args.meta)[0] + '.ann'

if os.path.exists(args.meta):
    with jsonlines.open(args.meta) as db_meta:
        for obj in db_meta:
            t.add_item(obj['idx'], obj['emb'])
else:
    raise FileNotFoundError(f'The database meta json "{args.meta}" was not found.')

t.build(10)
t.save(database_ann)
