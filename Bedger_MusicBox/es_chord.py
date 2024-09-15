import random
import sys
import pygame
import time
import numpy as np
#import BedgerIO as bedger

# Initialize pygame
pygame.init()
pygame.mixer.init()

tempo = 120
note_duration = 500
f_0=[440, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.26, 698.46, 739.99, 783.99, 830.61]
seconds_per_beat = 60 / tempo

NOTES = {
"A" : 440,
"A#/Bb" : 466.16,
"B" : 493.88,
"C" : 523.25,
"C#/Db" : 554.37,
"D" : 587.33,
"D#/Eb" : 622.25,
"E" : 659.26,
"F" : 698.46,
"F#/Gb" : 739.99,
"G" : 783.99,
"G#/Ab" : 830.61
}

BEDGING_CHORD = ["A#/Bb", "C", "D", "D#/Eb", "F", "G", "G#/Ab"]

def generate_sound(frequency, duration_ms):
    sample_rate = 44100  # CD quality audio
    t = np.linspace(0, duration_ms / 1000, int(sample_rate * (duration_ms / 1000)), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    wave *= 32767 / np.max(np.abs(wave))  # Scale to 16-bit integer range
    # Convert to a 2D array for mono sound
    wave = np.column_stack((wave, wave))
    return pygame.sndarray.make_sound(wave.astype(np.int16))

# Function to compose melody
def composer(frequencies, durations_ms):
    sample_rate = 44100  # CD quality audio
    melody_wave = np.array([], dtype=np.float64)  # Initialize an empty array to hold the melody waveform
    for frequency, duration_ms in zip(frequencies, durations_ms):
        t = np.linspace(0, duration_ms / 1000, int(sample_rate * (duration_ms / 1000)), endpoint=False)
        note_wave = np.sin(2 * np.pi * frequency * t)  # Generate the sine wave for the current note
        # Apply fade-in and fade-out effects to the note waveform
        fade_in_samples = int(0.05 * len(note_wave))  # 5% of note fade-in duration
        fade_out_samples = int(0.15 * len(note_wave))  # 9% of note fade-out duration
        fade_in = np.linspace(0, 1, fade_in_samples)
        fade_out = np.linspace(1, 0, fade_out_samples)
        note_wave[:fade_in_samples] *= fade_in
        note_wave[-fade_out_samples:] *= fade_out
        melody_wave = np.concatenate((melody_wave, note_wave))  # Concatenate the current note to the melody waveform
    melody_wave *= 32767 / np.max(np.abs(melody_wave))  # Scale to 16-bit integer range
    # Convert to a 2D array for mono sound
    melody_wave = np.column_stack((melody_wave, melody_wave))
    return pygame.sndarray.make_sound(melody_wave.astype(np.int16))

def play_note(note, duration):
    frequency = NOTES[note]
    sound = generate_sound(frequency, duration * note_duration)
    sound.play()
    time.sleep(duration * seconds_per_beat)

def check(pair):
    k,v = pair
    if k in BEDGING_CHORD:
        return True
    else:
        return False

def F_n_octav(f0,n,up):
    if up:
        return f0*(2**n)
    else:
        return f0/(2**n)
    
def pygame_stop():
    pygame.quit()

def export_wav(melody_wave,filename):
    # Save the melody as a WAV file
    pygame.mixer.Sound(melody_wave).set_volume(1)  # Reset the volume
    pygame.mixer.Sound(melody_wave).play()  # Play the sound (for export)
    pygame.mixer.Sound(melody_wave).export("filename", format="wav")  # Export the melody as a WAV file


if __name__ == "__main__":
    wav_File = sys.argv[1]
    chord_dict = dict(filter(check, NOTES.items()))
    bedging_freq=[NOTES[note] for note in BEDGING_CHORD if note in NOTES]
    note_dur_ms=[1000 for i in range(len(bedging_freq))]
    # for note, duration in melody:
    #     play_note(note, duration)

    sound_melody = composer(durations_ms= note_dur_ms,frequencies=bedging_freq)

    sound_melody.play()
    time.sleep(sum(note_dur_ms)/100 * seconds_per_beat)
    # Append2bin_file("notes.schl", "note", 1000)
    pygame.quit()


        