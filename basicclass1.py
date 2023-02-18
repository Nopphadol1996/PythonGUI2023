## จำลองคลาสร้านขายของ
class Product:
	# Attibute : จะบอกลักษณะต่างๆที่เกี่ยวกับ Product
	# name = 'water' # ชื่อร้านขายน้ำดื่ม
	# quantity = 3
	# price = 8.50

	# Constructor แบ่งออกเป็น 2 ประเภท (1) แบบไม่มี paremeter (2)แบบมี parameter

	# นี่คือการใส่ paremeter จร้า และ สามารถกำหนด defult ได้จ้า 
	# def __init__(self,name='water',quantity=3,price=8.50):
	def __init__(self,name,quantity,price):
		self.name = name	# self. คือ keyword ที่อ้างถึงตัวแปรที่อยู่ใน class 
		self.quantity = quantity
		self.price = price	

	# Method มันก็คือฟังก์ชั่นนั้นแหละ แต่เพียงมาอยู่ใน class จะเรียกว่า Method
	def hello(self):
		print("สวัสดีคุณลูกค้า Uncle Shop")


	# การสืบทอด Class/ Inheritance
class Customer(Product):
	# fullname = ชื่อลูกค้า
	# money = จำนวนเงิน
	def __init__(self,fullname,money,name,quantity,price): # ให้คลาสลูกเรียกคลาสแม่ต้องใส่ Parameter ด้วย name,quantity,price ของคลาสแม่
		super().__init__(name,quantity,price) #ต้องใช้คำสั่งพิเศษ super()
		self.fullname = fullname
		self.money = money
	
	def calculate(self): # คำนวนราคาจาก method
		self.total  = self.quantity * self.price
		self.money -= self.total
		print(f'เหลือเงิน {self.money} บาท')

class StaticClass:
    def run(): # static ไม่ต้องใส่ self , ไม่ต้องสร้าง Object,instance เรียกชื่อ class ได้เลย
        print('นี่คือเมธอด static')


# Instance  คือตัวแปรที่มาจาก object
# product1 = Product('water',3,8.50) # นี่คือการสร้าง Instance
product1 = Product('Coffe',3,15)
# การเรียกใช้ Attibute  กับ Method จาก class product
print(product1.name)
print(product1.quantity)
print(product1.price)
print('-----------------')
# การเรียกใช้งาน Method
product1.hello()
product2 = Product('Juice',5,20)
print(product2.name)
print(product2.quantity)
print(product2.price)

# print(type(product1))
# print(type(product2))

print('-----------------')


customer1 = Customer('สมชาย สบายดี',500,'water', 2, 8.50) # อย่าลืมส่งค่าให้กับ Parameter 
print(customer1.fullname)
print(customer1.money)
customer1.calculate()

customer2 = Customer('สมศรี สบายใจ',1000, 'Coffee', 3 , 15)
print(customer2.fullname)
print(customer2.money)
customer2.calculate()
print('-----------------')

# ในการสืบทอด Class ลูกสามารถใช้ Attibute ของคลาสแม่ได้
customer3 = Customer('ลุง วิศวะกร',10000,'Green Tea',2,20)
print(customer3.name)
print(customer3.quantity)
print(customer3.price)
customer3.calculate()