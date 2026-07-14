from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO("models/object_detector_v1.pt")

# Open webcam (0 = default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO detection
    results = model.predict(frame)
    results = model.predict(frame, conf=0.80)

    # Draw detections   
    annotated_frame = results[0].plot()

    # Show video
    cv2.imshow("YOLO Live Detection", annotated_frame)

    # Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
