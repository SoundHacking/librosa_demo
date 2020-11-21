import librosa

filename = librosa.example('nutcracker')
audio, sample_rate = librosa.load(filename)

tempo, beat_frames = librosa.beat.beat_track(y=audio, sr=sample_rate)

print('tempo: {:.1f} beats per minute'.format(tempo))

beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate)
print(beat_times)
