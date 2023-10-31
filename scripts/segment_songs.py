'''
Helper script to segment all files with a particular extension
into smaller segments of configurable length.
'''

import os

def main(
        target_directory: str = 'data/songs',
        target_extensions: list[str] = ['wav'],
        chunk_duration: int = 5,
        chunked_directory: str = 'chunks/'
    ):
    segment_audio_source_into_segments(
        target_directory,
        target_extensions,
        chunk_duration,
        chunked_directory
    )

def segment_audio_source_into_segments(
        target_directory: str,
        target_extensions: list[str],
        chunk_duration: int,
        chunked_directory: str,
    ):
    os.makedirs(chunked_directory, mode = 511, exist_ok=True)
    for directory, nested_directories, files in os.walk('.'):
        if target_directory in directory:
            for filename in files:
                if any(filename.endswith(target_extension) for target_extension in target_extensions):
                    full_target_path = os.path.join(directory, filename)
                    full_target_path = full_target_path.replace(' ','\ ')
                    full_chunk_path =  os.path.join(chunked_directory, f'chunk_{filename}%03d.wav')
                    full_chunk_path = full_chunk_path.replace(' ', '_')
                    os.system(fr'ffmpeg -i "{full_target_path}" -f segment -segment_time {chunk_duration} {full_chunk_path}')


if __name__ == '__main__':
    main()