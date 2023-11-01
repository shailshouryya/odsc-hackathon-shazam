# odsc-hackathon-shazam

This integrates Weaviate's API to match a given
  - text phrase
  - audio clip
  - video clip (future addition)

Weaviate's vectorization has the ability to match the "meaning" of the vectorized objects, meaning that the model can infer the context about an object and find objects that have a similar, but not exactly the same, context as the original query. For example, searching for "I enjoy ice cream" may match "I like dessert," even though the text for the two phrases is not (syntactically) similar. This feature is useful for finding "near matches" for a given query, and can also be used to find new results that are similar, but not an exact match, to the original query the user provides.

## project overview

1. Gather raw audio files (we used `.wav` format, but any other format can be used as long as the audio file can be processed with `ffmpeg`)
2. Chunk the raw audio into smaller chunks
  - we used the [`scripts/segment_songs.py`](./scripts/segment_songs.py) script to automate this process
    - requires `ffmpeg`, which is available at https://ffmpeg.org/download.html, or via `brew update ; brew upgrade ; brew install ffmpeg` on macOS
    - requires python version 3.9+
3. Modify the recipe from [media_search_bind.ipynb](https://github.com/weaviate/recipes/blob/main/media-search/media_search_bind.ipynb) to upload and analyze the chunks of the songs
4. Run queries against the local Weavite objects