
#Martin Barker
#www.martinradio.com
#dst = where to save album artwork for the currently playing song
dst = "C:/Users/marti/Desktop/MRL/cover/art.jpg"
#save_path = where to save text file of album art / title / artist text
#save_path = "C:\Users\marti\Desktop\Martin Radio Livestream"
save_path = "C:/Users/marti/Desktop/Martin Radio Livestream"


#need to import requests


print("--------------")
print(" Martin Radio ")
#print(" Input options: 's'(start), 'e'(end) ")
print("--------------")
from shutil import copyfile
from sys import exit
import os
import os.path
import requests
import time
from PIL import Image

def save_img(src): #resizes image and saves it to dst folder
#    print("in func")

    #resize album art, save to dst
    basewidth = 1000
    img = Image.open(src)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(dst)
    print("~~dst image saved to src~~")
    return

def find(searchterm): #this will find any of the terms passed into function
#    print("In find function, looking for "+searchterm)
    s = requests.Session()
    s.auth = ('', 'password') # Username is blank, just provide the password
    r = s.get('http://localhost:8080/requests/status.xml', verify=False)
#    print(len(searchterm))
    loc = r.text.find(searchterm)
    if loc < 1:
        tag = " "
    else:
        rough_loc = r.text[(loc+((len(searchterm))+2)):(loc+300)]
#        print(rough_loc)
        loc_end = rough_loc.find("/info");
        tag = r.text[(loc+((len(searchterm))+2)):(loc+loc_end+(len(searchterm))+1)]
    return tag

def parse():
#    print("in parse function")
    s = requests.Session()
    s.auth = ('', 'password') # Username is blank, just provide the password
    r = s.get('http://localhost:8080/requests/status.xml', verify=False)
    str2 = "artwork_url"
    loc = r.text.find(str2) #loc = index location of where artwork_url begins
    rough_loc = r.text[(loc+21):(loc+300)] #rough_loc = location string, no ending
    loc_end = rough_loc.find("/info"); #loc_end = index point where pic source ends
    art_location = r.text[(loc+21):(loc+loc_end+20)]
    #replace any weird characters
    new = art_location.replace("%20"," ")
    new = new.replace("%5B","[")
    new = new.replace("%26","&")
    new = new.replace("%5D","]")
    new = new.replace("%27","'")
    new = new.replace("%28","(")
    new = new.replace("%29",")")
    return new

def song_info():
#    print("In song info function")

    searchterm = "<info name=\'title"
    title = find(searchterm)
    print("Song Title: "+title)

    searchterm = "<info name=\'artist"
    artist = find(searchterm)
    print("Artist: "+artist)

    searchterm = "<info name=\'album"
    album = find(searchterm)
    print("Album: "+album)

    searchterm = "<info name=\'date"
    date = find(searchterm)
    print("Date: "+date)

    searchterm = "<info name=\'genre"
    genre = find(searchterm)
    print("Genre: "+genre)

#    save_path = "C:\Users\marti\Desktop\Martin Radio Livestream"
    completeName = os.path.join(save_path, "song_info"+".txt")
    file1 = open(completeName, "w")

    toFile = title + " - " + artist + "\n" + album + " ("+date+")\n" + genre


    file1.write(toFile)
    file1.close()
    return


starttime=time.time()

#print("beginning")
song_info()




check = 0;
loop = 1;
while loop == 1:
#    print("begining first loop")
    if check == 0:
        print(parse())
        #get initial image source location as string
        first_img = parse()
        print(first_img)
        save_img(first_img)

    check = 0;
    while check == 0:
        #check for new image locatione very 2 seconds
        time.sleep(2.0 - ((time.time() - starttime) % 2.0))
        new_img = parse()
        print("     new_img:")
        print("     " + new_img + "\n")

        #compare initial art locaion to new art location (see if they differ)
        if first_img != new_img:
            check = 1
            save_img(new_img)
            save_img(new_img)
            song_info()
            first_img = new_img

#    loop = 2;
#continues loop forever, cannot currently exit the loop
