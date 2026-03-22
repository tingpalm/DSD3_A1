# DSD3_A1
# Python Webcam Reader (OpenCV)

โปรแกรมนี้แสดงวิธีการใช้ภาษา Python และไลบรารี OpenCV เพื่อเข้าถึงและอ่านภาพจากกล้อง Webcam

## สิ่งที่ต้องเตรียม (Prerequisites)
- Python 3.6 ขึ้นไป
- กล้อง Webcam ที่สามารถใช้งานได้กับคอมพิวเตอร์

## วิธีการติดตั้งและการใช้งาน

### 1. การสร้าง Virtual Environment
เปิด Terminal หรือ Command Prompt ไปที่โฟลเดอร์ `Day2_Camera` จากนั้นรันคำสั่งเหล่านี้:

สร้างโฟลเดอร์ `venv` สำหรับเก็บ Environment:
```bash
python -m venv venv
```

เปิดใช้งาน (Activate) Virtual Environment (สำหรับ Windows):
```bash
venv\Scripts\activate
```

เมื่อเปิดใช้งานสำเร็จ จะมีคำว่า `(venv)` ขึ้นมาที่หน้า Command Prompt

### 2. การติดตั้งไลบรารี OpenCV
รันคำสั่งเพื่อติดตั้งแพ็กเกจที่ใช้ในการอ่านกล้อง:
```bash
pip install opencv-python
```

### 3. รันโปรแกรม
ใช้คำสั่งต่อไปนี้เพื่อรันโปรแกรม:
```bash
python camera.py
```

### การควบคุมโปรแกรม
- โปรแกรมจะแสดงหน้าต่างภาพจากกล้อง Webcam ชื่อ **Webcam**
- คุณสามารถกดปุ่ม **`q`** บนคีย์บอร์ด หรือปิดหน้าต่าง เพื่อหยุดการทำงานของโปรแกรม
