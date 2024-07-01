import mido
from mido import MidiFile, MidiTrack, Message
import easygui

# Function to convert note name to MIDI number
def note_to_midi(note):
    note_names = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    note = note.upper()  # Convert note to uppercase to handle lowercase input
    octave = int(note[-1])
    key = note[:-1]
    return note_names[key] + (octave + 1) * 12 - 12

# Get user inputs
start_note = easygui.enterbox("Enter the starting note (e.g., C4, D#3):")
range_notes = int(easygui.enterbox("Enter the range (number of semitones):"))
note_length = int(easygui.enterbox("Enter the note length (in milliseconds):"))
note_gap = int(easygui.enterbox("Enter the note gap (in milliseconds):"))

# Convert the starting note to MIDI number
start_midi = note_to_midi(start_note)

# Create a new MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Add the chromatic scale notes to the track
for i in range(range_notes + 1):
    note = start_midi + i
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=note_length))
    track.append(Message('note_off', note=note, velocity=64, time=note_gap))

# Save the MIDI file
midi_file_name = 'chromatic_scale.mid'
mid.save(midi_file_name)
easygui.msgbox(f'MIDI file "{midi_file_name}" has been created.', 'Success')
