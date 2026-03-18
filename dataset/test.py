import os
import re

images_dir = r"C:\Users\User\Documents\keepproject\learningcondainYolo\dataset\images\train"
labels_dir = r"C:\Users\User\Documents\keepproject\learningcondainYolo\dataset\labels\train"

# Rename images: "new_cola (1).jpg.jpg" -> "new_cola_1.jpg"
for fname in os.listdir(images_dir):
    if fname.endswith(".jpg") or fname.endswith(".png"):
        new_name = fname
        # แก้นามสกุลซ้ำ .jpg.jpg
        new_name = re.sub(r'\.(jpg|png)\.(jpg|png)$', r'.\1', new_name)
        # แก้วงเล็บ (1) -> _1
        new_name = re.sub(r'\s*\((\d+)\)', r'_\1', new_name)
        # แก้ space เป็น _
        new_name = new_name.replace(" ", "_")

        if fname != new_name:
            os.rename(
                os.path.join(images_dir, fname),
                os.path.join(images_dir, new_name)
            )
            print(f"Image: {fname} -> {new_name}")

# Rename labels: "1f53c97e-new_cola_5.jpg.txt" -> "new_cola_5.txt"
for fname in os.listdir(labels_dir):
    if fname.endswith(".txt"):
        new_name = fname
        # ลบ prefix hash เช่น "1f53c97e-"
        new_name = re.sub(r'^[a-f0-9]+-', '', new_name)
        # แก้ .jpg.txt -> .txt
        new_name = re.sub(r'\.jpg\.txt$', '.txt', new_name)
        new_name = re.sub(r'\.png\.txt$', '.txt', new_name)

        if fname != new_name:
            os.rename(
                os.path.join(labels_dir, fname),
                os.path.join(labels_dir, new_name)
            )
            print(f"Label: {fname} -> {new_name}")

print("\nเสร็จแล้ว! ตรวจสอบชื่อไฟล์อีกครั้ง")