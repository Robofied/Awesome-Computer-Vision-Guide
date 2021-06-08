'''
Output : Flip the frame , capture a video and saving each and every frame 
         saving a video in the form of .avi extension
'''

# Import package
import cv2


def main():

    cap = cv2.VideoCapture(0)

    # fourcc is a 4-byte code used to specify the video codec.
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')

    # 1.video name 3.frame per sec 4.window size
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    while True:
        # Read frame
        ret, frame = cap.read()

        # Flip the frame
        flip_frame = cv2.flip(frame, 0)

        out.write(frame)
        cv2.imshow('frame', frame)
        cv2.imshow('Flip Frame', flip_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # u can choose any key
            break

    cap.release()
    out.release()  # video capture stop
    cv2.destroyAllWindows()


main()
