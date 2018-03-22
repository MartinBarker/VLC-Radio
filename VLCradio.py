
#Martin Barker
#www.martinradio.com
#dst = where to save album artwork for the currently playing song
dst = "C:/Users/martin/Documents/MartinRadioLive/Script/art.jpg"
#save_path = where to save text file of album art / title / artist text
save_path = "C:/Users/martin/Documents/MartinRadioLive"

#pip install opencv-python

#libraries to help encode / decode utf-8 chars to their corresponding ascii
#from unidecode import  unidecode
from urllib.parse import unquote
import html
import html.parser

#import sys
#import os
#decode a gzipped response:
#import gzip
#import io

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

def cleanup(url):
    try:
        return unquote(url, errors='strict')
    except UnicodeDecodeError:
        return unquote(url, encoding='latin-1')

def save_img(src): #resizes image and saves it to dst folder
    print("in save_img func")

    #resize album art, save to dst
    basewidth = 1000
    img = Image.open(src)
    print("img opened")
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    print("saving img")
    img.save(dst)
    print("~~dst image saved to src~~")
    return

def find(searchterm): #this will find any of the terms passed into function
#    print("In find function, looking for "+searchterm)
    s = requests.Session()
    s.auth = ('', '1234') # Username is blank, just provide the password
    r = s.get('http://localhost:8080/requests/status.xml', verify=False)

#    print("-------")
#    print(r)
#    print("-------")
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
    print("in parse function")
    s = requests.Session()
    s.auth = ('', '1234') # Username is blank, just provide the password
    r = s.get('http://localhost:8080/requests/status.xml', verify=False)
    str2 = "artwork_url"
    loc = r.text.find(str2) #loc = index location of where artwork_url begins
    rough_loc = r.text[(loc+21):(loc+300)] #rough_loc = location string, no ending
    loc_end = rough_loc.find("/info"); #loc_end = index point where pic source ends
    art_location = r.text[(loc+21):(loc+loc_end+20)]
    print("art_location = ", art_location)

    new = cleanup(art_location)
    print("new = ", new)


    return new
#    return art_location;

def replace(title):
#    title = title.replace("&amp;#39;", "'")
#    title = title.replace("amp;amp;", "")
#    title = title.replace("&amp;quot;", "\"")
#    print("In replace: "+title)
    return cleanup(title) #title

def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s



def htmlcleapup(input):

    input = html_decode(input)
    html_parser = html.parser.HTMLParser()
    output = html_parser.unescape(input)
    print("output = ", output)
    return output

def gettitle():
    searchterm = "<info name=\'title"
    title = find(searchterm)
    title = replace(title)
    title = htmlcleapup(title)
#    print("Song Title: "+title)
    return title

def song_info():
    print("In song info function")

    searchterm = "<info name=\'title"
    title = find(searchterm)
    title = replace(title)
    title = htmlcleapup(title)
    print("Song Title: "+title)

    searchterm = "<info name=\'artist"
    artist = find(searchterm)
    artist = replace(artist)
    artist = htmlcleapup(artist)
    print("Artist: "+artist)

    searchterm = "<info name=\'album"
    album = find(searchterm)
    album = replace(album)
    album = htmlcleapup(album)
    print("Album: "+album)

    searchterm = "<info name=\'date"
    date = find(searchterm)
    date = replace(date)
    date = htmlcleapup(date)
    print("Date: "+date)

    searchterm = "<info name=\'genre"
    genre = find(searchterm)
    genre = replace(genre)
    genre = htmlcleapup(genre)
    print("Genre: "+genre)

    save_path = "C:/Users/martin/Documents/MartinRadioLive"
    completeName = os.path.join(save_path, "song_info"+".txt")
    file1 = open(completeName, "w")

    toFile = title + "\n" + artist + "\n\n" + album + "\n"+date+"\n" + genre


    file1.write(toFile)
    file1.close()
    return

print("start")
starttime=time.time()

#print("beginning")
song_info()
print("done parseing song info")



check = 0;
loop = 1;
while loop == 1:
    print("begining first loop")
    if check == 0:
        print(parse())
        print("get initial image source location as string")
        first_img = parse()
        first_title = gettitle()
        print(first_img)
        save_img(first_img)
        save_img(first_img)
        save_img(first_img)
        print("done with initial save")
    check = 0;
    while check == 0:
        #check for new image locatione very 2 seconds
        time.sleep(2.0 - ((time.time() - starttime) % 2.0))
        new_img = parse()
        second_title = gettitle()
        print("     new_img:")
        print("     " + new_img + "\n")

        #parse for song info and save to file every 2 seconds
        song_info()

        #compare initial art locaion to new art location (see if they differ)
        #if first_img != new_img:
        if first_title != second_title:
            check = 1
            save_img(new_img)
            save_img(new_img)
            song_info()
            first_img = new_img

#    loop = 2;
#continues loop forever, cannot currently exit the loop
