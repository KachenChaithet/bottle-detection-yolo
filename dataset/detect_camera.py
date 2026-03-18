import cv2
from ultralytics import YOLO

# ใช้โมเดล default ที่ detect bottle ได้
model = YOLO("yolo11n.pt")

# เปิดกล้องด้วย MSMF backend
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

print("เปิดกล้องแล้ว กด 'q' เพื่อออก")

while True:
    ret, frame = cap.read()
    if not ret:
        print("อ่านภาพไม่ได้")
        break

    # detect เฉพาะ bottle (class 39)
    results = model(frame, conf=0.70, device=0, classes=[39],)

    # วาด bounding box
    annotated = results[0].plot(line_width=3)

    cv2.imshow("Cola Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()