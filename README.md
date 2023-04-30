
## Search video by text embeddings

This is a proof of concept to use text embeddings to search for video clips.
This doesn't really demonstrate the power of text embeddings, yet. 
Only advantage over string search is the fuzzyness of the search.

I used .srt subtitle files to generate the search database.
```
python srt_convert.py subtitles.srt video.mp4
python append.py db.ann Meta/subtitles.json
export OPENAI_API_KEY=yourkeyhere
python find.py
```
generated files:
1. db.ann - vector database
2. db.jsonl - metadata and embeddings, can be used to regenerate db.ann
3. db.meta.json - unused per video metadata

## Improvements
The main issue right now is with the input data. A single line from subtitles doesn't contain
much information.
Ideally you'd use text for an entire movie scene to allow more complex queries.
I don't know if there is any tool for temporal scene segmentation of a video.

Another issue is file size. The text embedding API used is an overkill for something like this.
The embeddings are 1536 dimensional, just 3 hours of video made the database size 10MB.

Where I wanted to get with this is having a chat bot that responds with video clips.
Not sure if I'll keep going.


Demo using first 4 episodes of Breaking Bad. (I hope this is fair use lol)
[![](https://markdown-videos.deta.dev/youtube/_Dfskm2TID4)](https://youtu.be/_Dfskm2TID4)
