import subprocess

def play(note):
    note = note.lower()

    subprocess.run('alda play -c "piano: c"')

lilypond_path = r'C:\Program Files (x86)\LilyPond\usr\bin\lilypond.exe'
file_path = r'"C:\Users\Trevaris Small\Desktop\test.ly"'
destination_path = r' -o "C:\Users\Trevaris Small\Desktop" '

def write_score():
    subprocess.run(lilypond_path + destination_path + file_path )


#######################################


import sys
for arg in sys.argv:
    print(arg)

inputNote = "D"

pitch_classes = {
    0: "c",
    1: "c+",
    2: "d"
}

# intervals = {}


