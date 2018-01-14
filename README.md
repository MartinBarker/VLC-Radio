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
First, change the image and text file save directories. 
![images](https://user-images.githubusercontent.com/27025504/34912841-409f2c9e-f8a0-11e7-8164-ceebe02c58e1.png)

Then, while VLC Media player is playing audio, run the program. The song info will be exported into a text file at the location for 'songInfoSaveLocation' specified in the image above. The album art will be resized and exported to the location specified in the 'artSaveLocation' value shown above.

You can see a working example by clicking on this image, or the link below. 

https://user-images.githubusercontent.com/27025504/34912889-a3a5e304-f8a1-11e7-98e5-ddc1c06f4a61.png
https://www.youtube.com/watch?v=DW2mUMJ_63A

[![images](https://user-images.githubusercontent.com/27025504/34912841-409f2c9e-f8a0-11e7-8164-ceebe02c58e1.png)(https://www.youtube.com/watch?v=DW2mUMJ_63A](https://www.youtube.com/watch?v=DW2mUMJ_63A)

I used OBS studio for broadcasting, and set it up to display the jpg titled art.jpg in a folder, as well as display the contents of a specific text file. The album art and text file are automatically updated when their contents are changed.

# VLC Setup
To setup VLC Media Player, you will need to enable an online connection. You can find instructions on how to do so in this post:
https://stackoverflow.com/questions/24178980/how-to-monitor-vlc-media-player-on-windows-7-using-python

If you follow this guide, you will set a password for your vlc web interface, in the python file make sure you enter that same password in the s.auth = ('', 'password') field
