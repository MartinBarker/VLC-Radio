# VLC-Radio Python script
### A tool for streamers to cleanly display song info from VLC Media Player.
Built for Python 3.6

install with 
```pip install VLCtagExporter ```

and run with 
``` python -m VLCtagExporter ```

# Requirements
The following python packages need to be installed, you can install them using these commands:
``` 
pip install Image   
```
``` 
pip install requests 
```

# How to use
Firstly, change the image and text file save directories. 
![images](https://user-images.githubusercontent.com/27025504/34912841-409f2c9e-f8a0-11e7-8164-ceebe02c58e1.png)

Then, while VLC Media player is playing audio, run the program. The song info will be exported into a text file at the location for 'songInfoSaveLocation' specified in the image above. The album art will be resized and exported to the location specified in the 'artSaveLocation' value shown above.

You can see a working example by clicking on the image or link below. 
[![images](https://user-images.githubusercontent.com/27025504/34912889-a3a5e304-f8a1-11e7-98e5-ddc1c06f4a61.png)(https://www.youtube.com/watch?v=DW2mUMJ_63A](https://www.youtube.com/watch?v=DW2mUMJ_63A)

I used OBS studio for broadcasting, and set it up to display the jpg titled art.jpg in a folder, as well as display the contents of a specific text file. The album art and text file are automatically updated when their contents are changed.

# VLC Setup
You will need to enable a web interface for VLC media player for this program. You can find instructions on how to do so in this post:
https://stackoverflow.com/questions/24178980/how-to-monitor-vlc-media-player-on-windows-7-using-python

This link will describe how to:
- Activating web interface: Open VLC goto Tools--->Preferences-----> Main Interface as shown below tick mark the web option. 
- Then click on Lua option on the left pane. Enter the password in the password field and enter C:\Program Files\VideoLAN\VLC\lua\http in the source directory field as shown below. Verify that you have status.xml file at the location that you provided in the source directory.
- Start the VLC player and play some file. Visit http://localhost:8080/requests/status.xml and you shall see a login page, leave the username field blank and enter the password that you entered in the VLC. If you logged in successfully you shall see the XML file!
If you don't see any thing then do the following as shown in the image below: goto View--->Add Interface----->Select web 

