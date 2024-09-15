import time
import es_chord as music
import BedgerIO as bIO
import numpy as np
# from pydub import AudioSegment # for exporting an MP3 
from scipy.io.wavfile import write
from scipy.io import wavfile
from pydub import AudioSegment

if __name__ == "__main__":
    melody_notes = np.random.choice(music.BEDGING_CHORD, size=31, replace=True)
    # freqs = [music.NOTES[n] for n in music.BEDGING_CHORD]
    freqs = [music.NOTES[n] for n in melody_notes]
    # melody = np.random.choice(freqs, size=16, replace=True)
    note_dur_ms = 100 * np.random.randint(2, high=5, size=len(freqs), dtype=int)
    # print (np.random.choice(music.BEDGING_CHORD, size=12, replace=True))
    # print (melody)
    
    for note,f,ms in zip(melody_notes,freqs,note_dur_ms):
        print(note,'['+str(f)+']',"->",ms)
        bIO.Append2bin_file("dataMelodies/melodiesV4.schl",note,ms)
    bIO.Append2bin_file("dataMelodies/melodiesV4.schl",3 * "-- --- ",sum(note_dur_ms)/1000)

    sound_melody = music.composer(frequencies=freqs, durations_ms= note_dur_ms)

    # Create a Pygame sound object
    melody_sound = music.pygame.sndarray.make_sound(sound_melody)
    # Save the melody as a WAV file
    # write("melody.wav", 44100, sound_melody)
    # Save the melody as a WAV file
    # Save the melody waveform to a NumPy file
    np.save("melody.npy", sound_melody)
    sound_melody.play()
    time.sleep(sum(note_dur_ms)/1000 + 1)
    # Load the melody waveform from the NumPy file
    melody_wave = np.load("melody.npy")
    # Write the melody to a WAV file
    wavfile.write("melody.wav", 44100, melody_wave)

    while music.pygame.mixer.music.get_busy():
        music.pygame.event.wait()
    # Load the WAV file
    wav_file = "melody.wav"
    audio = AudioSegment.from_wav(wav_file)

    # Convert the audio to MP3
    # mp3_file = "melody.mp3"
    # audio.export(mp3_file, format="mp3")
    # Wait for the melody to finish playing
    

    
    # sound_melody.play()
    # time.sleep(sum(note_dur_ms)/1000 + 1) # music.seconds_per_beat

    music.pygame_stop()