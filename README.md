# ImgToASCII

You need to specify three arguments when calling the script:
- path to the image from the working directory,
- height of a chunk,
- width of a chunk.

The script splits the image into chunks and converts to ASCII based on the average brightness of each chunk.
You can try height = 3 and width = 2 for a big and detailed image or height = 16 and width = 6 for a smaller and less detailed one.
You will be given an option to equalize the image histogram before conversion. 
It can, for example, improve the contour, but sometimes it adds a lot of artifacts.