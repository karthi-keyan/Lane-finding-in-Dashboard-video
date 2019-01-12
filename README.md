# Lane-finding-in-Dashboard-video
Finding lanes in the self driving car
it is the part of Udacity's self driving car course
finding lanes from dashboard view involves following steps:
1.for each frame in video:
      1.converting the frame into grayscale
      2.smoothening of frame in order to remove noise
      3.applying canny ie. it finds the gradient in the image to detect the edges
      4.applying houghlinespace in order to find the possible lane lines
      5.normalize all the possible lines into one line for each side of the line
      4.display the line in the output video
2.do this until the last frame of video 
