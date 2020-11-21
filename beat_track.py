import librosa

filename = librosa.example('nutcracker')
audio, sample_rate = librosa.load(filename)
print(sample_rate)

tempo, beat_frames = librosa.beat.beat_track(y=audio, sr=sample_rate)
beat_times = librosa.frames_to_time(beat_frames, sr=sample_rate)

print('tempo: {:.1f} beats per minute'.format(tempo))
print(beat_times)
