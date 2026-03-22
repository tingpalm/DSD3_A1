import cv2

def main():
    # Initialize the webcam (0 is usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return

    print("Webcam started successfully.")
    print("Press 'q' on your keyboard to quit the application.")

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame from the webcam.")
            break

        # Display the frame in a window named 'Webcam'
        cv2.imshow('Webcam', frame)

        # Wait for 1 ms and check if 'q' is pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting...")
            break

    # Release the webcam resource and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
