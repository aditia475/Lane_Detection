# Lane_Detection
*Real-Time Lane Detection*

Problem Statement : -
> The task that we wish to perform is that of real-time lane detection in a 
> video, we are doing so using the popular OpenCV Library in Python for 
> Image processing.


Theoretical details: -
> *The core part of the detection is to correctly extract the lines of the road from all the rest of the images. 
> We can do this applying the Hsv color detection. 
> In this way we can detect object by their colors, as the lines of a road can be only yellow or white, we extract the part of the images that contains either of 
> these two colors only. 
> Once we have the mask we find the edges, we use the ‘Hough 
transform method’.*

Code: -
> Python Code.py
