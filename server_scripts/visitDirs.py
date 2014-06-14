import os.path
import subprocess 

# The top argument for walk. The
# Python27/Lib/site-packages folder in my case
 
topdir = "/media/famcloud_media/iTunes Music/Yellowcard/When You're Through Thinking, Say Yes"
 
# The arg argument for walk, and subsequently ext for step
exten = '.m4a'
 
def step(ext, dirname, names):
    ext = ext.lower()
 
    for name in names:
        if name.lower().endswith(extern):
            # if the file is a .m4a file then we should convert it.
            subprocess.call([
                "avconv", "-i",
                os.path.join(dirname, name),
                #os.path.join(path, filename),
                #"-acodec", "libmp3lame", "-ab", "256k",
                os.path.join(dirname,'%s.mp3' % name[:-4])
                #os.path.join(OUTPUT_DIR, '%s.mp3' % filename[:-4])
                ])
            print("Converted: " + name)
 
# Start the walk
os.path.walk(topdir, step, exten)