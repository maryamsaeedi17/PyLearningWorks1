from pysynth_s import make_wav

song=(('r',4),('e',4),('f#',4),('g',4),('f#',2),('g',4),('f#',2),('g',4),('e',2),
      ('r',4),('e',4),('f#',4),('g',4),('f#',2),('g',4),('f#',2),('g',4),('e',2),

      ('r',4),('e',4),('f',4),('g',4),('a',2),('c5',4),('b',8),('a',8),('g#',8),('f',8),('e',-2),
      ('r',4),('e',4),('f',4),('g',4),('a',2),('c5',4),('b',8),('a',8),('g#',8),('f',8),('e',-2),

      ('r',4),('e',4),('f',4),('g',4),('f',2),('g',4),('a',2),('f',4),('e',2),
      ('r',4),('e',4),('f',4),('g',4),('f',2),('g',4),('a',2),('f',4),('e',2)
)

make_wav(song, bpm=140, fn="qoqa_ye_setaregan1.wav")