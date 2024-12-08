import tkinter as tk
from PIL import Image, ImageTk

def Color():
    # ดึงค่าจากช่อง input และจัดเรียงลำดับคำ
    user_input = color_input.get()
    sorted_input = "+".join(sorted(user_input.split("+")))  # จัดเรียงลำดับคำ
    
    # กำหนดรูปภาพที่จะแสดง
    if sorted_input == "น้ำเงิน+แดง":  # RED + BLUE
        image_path = "c:/Pro Color/Real_Pink.png"
        try:
            img = Image.open(image_path)
            img_tk = ImageTk.PhotoImage(img)  # แปลงรูปภาพเป็น PhotoImage
            image_label.config(image=img_tk)  # อัปเดตรูปภาพใน Label
            image_label.image = img_tk  # เก็บอ้างอิงรูปภาพ
            output_label.config(text="สีที่ผสม: สีชมพู")
        except FileNotFoundError:
            output_label.config(text=f"ไม่พบรูปภาพที่ path: {image_path}")
    
    elif sorted_input == "เขียว+แดง":  # RED + GREEN
        image_path = "c:/Pro Color/Yellow.png"
        try:
            img = Image.open(image_path)
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk
            output_label.config(text="สีที่ผสม: เหลือง")
        except FileNotFoundError:
            output_label.config(text=f"ไม่พบรูปภาพที่ path: {image_path}")
    
    elif sorted_input == "น้ำเงิน+เขียว":  # GREEN + BLUE
        image_path = "c:/Pro Color/Sky_Blue.png"
        try:
            img = Image.open(image_path)
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk
            output_label.config(text="สีที่ผสม: ฟ้า")
        except FileNotFoundError:
            output_label.config(text=f"ไม่พบรูปภาพที่ path: {image_path}")
    
    else:
        output_label.config(text="ไม่ได้เลือกสีที่กำหนดไว้")

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("Super Color Mother MIX!")
window.geometry("600x600")  # กำหนดขนาดหน้าต่าง

# สร้างป้ายชื่อ
title_label = tk.Label(window, text="ผสมสี", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# สร้างช่องใส่ข้อความ
color_input = tk.Entry(
    window, 
    font=("Arial", 14),
    width=30
) 
color_input.pack()

# สร้างปุ่ม และผูกกับฟังก์ชัน Color
mix_button = tk.Button(
    window, 
    text="Mix", 
    command=Color, 
    bg="lightblue",  # สีพื้นหลัง
    fg="darkblue",    # สีข้อความ
    width=20,        # จำนวนตัวอักษรกว้าง
    height=2         # จำนวนบรรทัดสูง
)
mix_button.pack(pady=10)

# สร้างป้ายชื่อสำหรับแสดงผลลัพธ์
output_label = tk.Label(window, text="ผลลัพธ์จะแสดงที่นี่", font=("Arial", 12))
output_label.pack()

# สร้าง Label สำหรับแสดงรูปภาพ
image_label = tk.Label(window)  # สร้าง Label ที่ใช้สำหรับแสดงรูปภาพ
image_label.pack(pady=20)

# รันโปรแกรม
window.mainloop()
