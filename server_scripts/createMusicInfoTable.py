import os
import sys
from mutagen.m4a import M4A
from mutagen.mp3 import MP3
import MySQLdb
 
topdir = "/media/famcloud_media/Music"

def seconds_to_min_sec( secs ):
  "Return a minutes:seconds string representation of the given number of seconds."
  mins = int(secs) / 60
  secs = int(secs - (mins * 60))
  return "%d:%02d" % (mins, secs)


db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="uxd6Hp!3", db="music")
cursor = db.cursor()

# We are going to be very simple and just delete all the entries in the table and re add them.
try:
    # Execute the SQL command
    cursor.execute("TRUNCATE TABLE music_info")
    cursor.execute("TRUNCATE TABLE artists")
    cursor.execute("TRUNCATE TABLE albums")
except:
    print "Error: unable to delete the table entries"

#----------------------------------------------------------------------
failedFiles = []
for dirName, subdirList, fileList in os.walk(topdir):
    validFile = False
    for file in fileList:
        extension = os.path.splitext(file)[1].lower()
        try:
            if extension == ".m4a":
                # We will process the audio track as an mp4
                audio = M4A(os.path.join(dirName, file))
                try:
                    songtitle = audio["\xa9nam"]
                except:
                    songtitle = ""
                try:
                    artist = audio["\xa9ART"]
                except:
                    artist = ""
                try:
                    album = audio["\xa9alb"]
                except:
                    album = ""
                try:
                    pubYear = audio["\xa9day"]
                except:
                    pubYear = ""
                try:
                    trackNum = audio["trkn"][0]
                except:
                    trackNum = ""
                try:
                    genre = audio["\xa9gen"]
                except:
                    genre = ""
                try:
                    totalTrack = audio["trkn"][1]
                except:
                    totalTrack = ""
                try:
                    trackLength = seconds_to_min_sec(audio.info.length)
                except:
                    trackLength = ""
                sql = "INSERT INTO music_info (track, artist, album, release_year, track_num, genre, track_length, total_tracks, file_format) VALUES(\"%s\", \"%s\"," \
                      " \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" %  (songtitle, artist, album, pubYear, trackNum, genre, trackLength, totalTrack, "m4a")
            
                cursor.execute("SELECT artist FROM artists WHERE artist = \"" + str(artist) + "\"")
                data = cursor.fetchall()
                if len(data) == 0:
                    sql_artists = "INSERT INTO artists (artist) VALUES(\"%s\")" % (artist)
                else:
                    sql_artists = ""
            
                cursor.execute("SELECT album, artist FROM albums WHERE artist=\"" + str(artist) + "\" AND album=\"" + str(album) + "\"")
                data = cursor.fetchall()
                if len(data) == 0:
                    sql_album = "INSERT INTO albums (album, artist) VALUES(\"%s\", \"%s\")" % (album, artist)
                else:
                    sql_album = ""
            
                try:
                    # Execute the SQL command
                    cursor.execute(sql)
                    db.commit()
                    if (sql_artists != ""):
                        cursor.execute(sql_artists)
                        db.commit()
                    if (sql_album != ""):
                        cursor.execute(sql_album)
                        db.commit()
                except:
                    print "Error: unable to add entry!"
                    print "MYSQL ERROR::", sys.exc_info()[0]
            
            if extension == ".mp3":
                # We will process the audio track as an mp3
                audio = MP3(os.path.join(dirName, file))
                try:
                    songtitle = audio["TIT2"]
                except:
                    songtitle = ""
                try:
                    artist = audio["TPE1"]
                except:
                    artist = ""
                try:
                    album = audio["TALB"]
                except:
                    album = ""
                try:
                    pubYear = audio["TDRC"]
                except:
                    pubYear = ""
                try:
                    trackNum = audio["TRCK"]
                    trackNum = str(trackNum).split("/")[0]
                except:
                    trackNum = ""
                try:
                    genre = audio["TCON"]
                except:
                    genre = ""
                try:
                    trackLength = seconds_to_min_sec(audio.info.length)
                except:
                    trackLength = ""
                sql = "INSERT INTO music_info (track, artist, album, release_year, track_num, genre, track_length, file_format) VALUES(\"%s\", \"%s\"," \
                      " \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")" % (songtitle, artist, album, pubYear, trackNum, genre, trackLength, "mp3")
                cursor.execute("SELECT artist FROM artists WHERE artist=\"" + str(artist) + "\"")
                data = cursor.fetchall()
                if len(data) == 0:
                    sql_artists = "INSERT INTO artists (artist) VALUES(\"%s\")" % (artist)
                else:
                    sql_artists = ""
            
                cursor.execute("SELECT album, artist FROM albums WHERE artist=\"" + str(artist) + "\" AND album=\"" + str(album) + "\"")
                data = cursor.fetchall()
                if len(data) == 0:
                    sql_album = "INSERT INTO albums (album, artist) VALUES(\"%s\", \"%s\")" % (album, artist)
                else:
                    sql_album = ""
            
                try:
                    # Execute the SQL command
                    cursor.execute(sql)
                    db.commit()
                    if (sql_artists != ""):
                        cursor.execute(sql_artists)
                        db.commit()
                    if (sql_album != ""):
                        cursor.execute(sql_album)
                        db.commit()
                except:
                    print "Error: unable to add entry!"
                    print "MYSQL ERROR::", sys.exc_info()[0]
        except:
           print os.path.join(dirName, file) + " -- FAILED"
           failedFiles.append(os.path.join(dirName, file))

print "Done storing song data into MySQL"
if len(failedFiles) > 0:
    print "The following files failed: "
    for file in failedFiles:
        print file
else:
    print "All files were stored successfully"
print "---------------------"
