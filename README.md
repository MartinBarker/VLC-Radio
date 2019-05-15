# VLC-Radio Python script
### A tool to export the albumart and metadata of the currently playing song in VLC media player ###

Built for Python 3.6

install with 
```pip install vlcradio```

when running, specify the path where you want to save the image, path where you want to save the text file containing song metadata, and url of VLC's web status [instructions to enable this are below]

run the program:
``` python -m vlcradio "imgPath" "metadataPath" "url" ```

example command:
``` python -m vlcradio "E:/Martin Radio/Martin Radio Live/streamAlbumArt/art.jpg" "E:/Martin Radio/Martin Radio Live/metadata/song_info.txt" "http://localhost:8080/status.xml"  ```


# How to use
While VLC Media player is playing audio, run the vlcradio package. The song info will be exported into a text file at the location specified in the "metadataPath" command line argument. The album art will be resized and exported to the location specified in the  "imgPath" command line argument.

You can see a working example by clicking on the image or link below. 
[![images](https://user-images.githubusercontent.com/27025504/34912889-a3a5e304-f8a1-11e7-98e5-ddc1c06f4a61.png)(https://www.youtube.com/watch?v=DW2mUMJ_63A](https://www.youtube.com/watch?v=DW2mUMJ_63A)

I used OBS studio for broadcasting, and set it up to display the jpg titled art.jpg in a folder, as well as display the contents of a specific text file. The album art and text file are automatically updated when their contents are changed.

# VLC Setup
You will need to enable a web interface for VLC media player for this program. You can find instructions on how to do so in this post:
https://stackoverflow.com/questions/24178980/how-to-monitor-vlc-media-player-on-windows-7-using-python

This link will describe how to:
- Activating web interface: Open VLC, go to Tools -> All -> Interface -> Main Interfaces 
Ensure that 'web' is checked.

- Main Interfaces -> Lua
Enter a password, and verify that you have a status.xml file at the location that you provided in the source directory.

- Start VLC and play some file. Visit http://localhost:8080/status.xml and you should see a login page, leave the username field blank and enter the password that you entered in the VLC. If you logged in successfully you shall see the XML file!


