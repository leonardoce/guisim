"""
This is a set of relationship between notes and underlying fundamental
frequencies
"""

from collections import namedtuple


HZ_A1 = 55
"""
This is the frequency of A1 
"""

notes_db = list()
"""
This is the list of notes
"""

Note = namedtuple("Note", "hz name")
"""
This represent a musical note
"""

note_names = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']


def compare(hz_1, hz_2):
    """
    Comparison function between two frequencies
    """
    return abs(hz_1 - hz_2) < 2


def find_note(hz):
    """
    Find the note name given a certain frequency
    """
    prev_note = None
    next_note = None

    for note in notes_db:
        if note.hz <= hz:
            prev_note = note
        if hz < note.hz:
            next_note = note
            break

    if compare(prev_note.hz, hz):
        return prev_note
    elif compare(next_note.hz, hz):
        return next_note
    else:
        return Note(hz=hz, name=f"{prev_note.name} {next_note.name}")


def __generate_db():
    """
    Generate the set of notes, as according to TET 12
    """
    current_note_name_idx = 0
    current_octave = 1
    current_hz = HZ_A1

    # 880 is the frequency of A5

    while current_hz <= 882:
        note_name = f"{note_names[current_note_name_idx]}{current_octave}"
        note = Note(hz=current_hz, name=note_name)
        notes_db.append(note)

        current_hz = current_hz * pow(2, 1/12)
        current_note_name_idx += 1
        if current_note_name_idx >= len(note_names):
            current_note_name_idx = 0
            current_octave += 1


__generate_db()
