'''
Output : Flip the frame , capture a video and saving each and every frame 
         saving a video in the form of .avi extension
         Difference between cv2.waitKey(0) and cv2.waitKey(1)
'''

# Import package
import cv2


def main():

    # Use cv2.VideoCapture() to get a video capture object for the camera.        
    cap = cv2.VideoCapture('../Images and Videos/nature.mp4')    

    # fourcc is a 4-byte code used to specify the video codec.
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')

    # 1.video name 3.frame per sec 4.window size
    out = cv2.VideoWriter('Original_frame.avi', fourcc, 20.0, (1280, 720))
    
    while True:

        # Capture video, frame by frame
        ret, frame = cap.read()

        # Flip the frame
        flip_frame = cv2.flip(frame, 0)

        out.write(flip_frame)
        cv2.imshow('frame', frame)
        cv2.imshow('Flip frame', flip_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # u can choose any key
            break
    
    # When everything done, release the video write objects and video capture object
    cap.release()
    out.release()  # video capture stop
    cv2.destroyAllWindows()

main()

