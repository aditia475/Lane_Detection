import cv2
import numpy as np

# Create a VideoCapture object and read from input file
video = cv2.VideoCapture(r'C:\Users\aditi\Documents\Semester 5\road_car_view_Trim1.mp4')

# Check if camera opened successfully
if (video.isOpened()== False):
        print("Error opening video file")
        
while True:
        ret,orig_frame =video.read()
        if ret == True:
        
            frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            low_yellow = np.array([10, 100, 140])
            up_yellow = np.array([48, 255, 255])
            mask = cv2.inRange(hsv, low_yellow, up_yellow)
            edges = cv2.Canny(mask, 75, 150)

            lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
            if lines is not None:
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                cv2.imshow("frame", frame)
                cv2.imshow("edges", edges)

                # Press Q on keyboard to exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
        # Break the loop
        else:
            break
            
# When everything done, release
# the video capture object
video.release()

# Closes all the frames
cv2.destroyAllWindows()
