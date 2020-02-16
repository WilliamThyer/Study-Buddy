from music21 import *
import random

# Increasingly louder volumes
d1, d2, d3, d4 = dynamics.Dynamic(.35), dynamics.Dynamic(.4), dynamics.Dynamic(.45), dynamics.Dynamic(.5)
d5, d6, d7, d8 = dynamics.Dynamic(.55), dynamics.Dynamic(.6), dynamics.Dynamic(.65), dynamics.Dynamic(.7)
d9, d10, d11 = dynamics.Dynamic(.8), dynamics.Dynamic(.9), dynamics.Dynamic(1)

# Discordant notes
n1, n2, n3, n4 = note.Note('Db4'), note.Note('Eb4'), note.Note('E'), note.Note('Gb')
n5, n6, n7 = note.Note('Ab'), note.Note('A'), note.Note('B')

for note in [n1, n2, n3, n4, n5, n6, n7]:
    note.duration.quarterLength = 3

# Dictionary of unpleasant sounds
punishment = {
    1: [d1, n1, n2],
    2: [d2, n1, n2],
    3: [d3, n1, n2, n3],
    4: [d4, n1, n2, n3],
    5: [d5, n1, n2, n3, n4],
    6: [d6, n1, n2, n3, n4],
    7: [d7, n1, n2, n3, n4, n5],
    8: [d8, n1, n2, n3, n4, n5],
    9: [d9, n1, n2, n3, n4, n5, n6],
    10: [d10, n1, n2, n3, n4, n5, n6],
    11: [d11, n1, n2, n3, n4, n5, n6, n7]
}


def punish(pain):
    """ Play increasingly more unpleasant chords """
    if pain < 12:
        sd = stream.Stream(punishment[pain])
    else:
        sd = stream.Stream(punishment[11]).transpose(pain % 73 - 12 - 2 * random.random())
    sp = midi.realtime.StreamPlayer(sd)
    sp.play()


# Test increasingly more unpleasant sounds
# for x in range(1, 360):
#     punish(x)
