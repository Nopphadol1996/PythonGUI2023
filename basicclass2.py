from basicclass1 import Product  # (basicclass1 คือชื่อ) (Product คือชื่อของ Class)

# เหมาะสมหรับค่าที่ไม่เปลี่ยนแปลง ตลอดจนปิดโปรแกม
class StaticClass:
    def run(): # static ไม่ต้องใส่ self , ไม่ต้องสร้าง Object,instance เรียกชื่อ class ได้เลย
        print('นี่คือเมธอด static')

# การเรียกใช้งาน Modul ภายนอก Class
# if __name__ == '__main__': คือการตรวจสอบว่า อยู่ใน file ว่าอยู่ใน Modul เดียวกันหรือเปล่า 
# สามารถเลือก Run code ได้ตามที่เราเลือกไม่จำเป็นต้อง Runทั้งหมด
if __name__ == '__main__':
    product = Product('กระทิงแดง',2,10) # อย่าลืมส่งค่า Parameter
    print(product.name)
    print(product.quantity)
    print(product.price)

    print('--------------------------')
    StaticClass.run()


### สรุปการสร้าง Class
# Medthod ที่ไม่เป็น Static ทั้งในและนอก Class ต้องสร้าง Instance , Constructor
# Medthod ที่ static ต้องสร้าง Object,instance