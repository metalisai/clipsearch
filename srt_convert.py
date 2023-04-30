import argparse
import srt
import os 
import sys
import json

parser = argparse.ArgumentParser(description="Convert subtitles into metadata")
parser.add_argument('srt', type=str, help=".srt file to parse")
parser.add_argument('video', type=str, help="video file that the subtitle is for")
parser.add_argument('--meta', nargs='?', const='', help="optional metadata used for search")

args = parser.parse_args()

# check if srt file exists
if not os.path.exists(args.srt):
    raise FileNotFoundError(f'The .srt file "{args.srt}" does not exist')
if not os.path.exists(args.video):
    raise FileNotFoundError(f'The video file "{args.video}" does not exist')

data = {}
data['meta'] = args.meta
data['video'] = args.video

with open(args.srt, 'rb') as srt_file:
    srt_data = srt_file.read().decode('cp1252')
    srt_data = srt_data.rstrip('\0')
    sub_gen = srt.parse(srt_data)
    subs = list(sub_gen)
# data format: Subtitle(index=1, start=datetime.timedelta(seconds=69, microseconds=236000), end=datetime.timedelta(seconds=72, microseconds=780000), content='Oh, my God. Christ!', proprietary='')
    metasubs = []
    print(f"Start parsing {len(subs)} subs")
    for sub in subs:
        metasub = {'start': str(sub.start), 'end': str(sub.end), 'text': sub.content} 
        metasubs.append(metasub)
    print("Done parsing")

data['utters'] = metasubs

#out_dir = os.path.dirname(args.srt)
out_dir = "Meta"
out_file_name = os.path.splitext(os.path.basename(args.srt))[0] + '.json'
out_file_path = os.path.join(out_dir, out_file_name)
print(f"Saving output to {out_file_path}")
with open(out_file_path, 'w') as f:
    json.dump(data, f)

