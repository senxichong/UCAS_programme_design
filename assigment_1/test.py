class Student:
    def __init__(self, student_id, name, major, year):
        self.student_id = student_id  # 学号
        self.name = name  # 姓名
        self.major = major  # 专业
        self.year = year  # 年级
        self.borrowed_books = []  # 当前借阅的书籍列表

    def borrow_book(self, book):
        """学生借书，加入借阅的书籍列表"""
        if book.is_available():
            self.borrowed_books.append(book)
            book.borrow(self.student_id)
            print(f"{self.name} 已成功借阅 {book.title}")
        else:
            print(f"{book.title} 当前不可借阅")

    def return_book(self, book):
        """学生还书，从借阅的书籍列表中移除"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"{self.name} 已成功归还 {book.title}")
        else:
            print(f"{self.name} 没有借阅此书")

    def view_borrowed_books(self):
        """查看已借阅的书籍"""
        if self.borrowed_books:
            print(f"{self.name} 当前借阅的书籍:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print(f"{self.name} 当前没有借阅书籍")
class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title  # 书名
        self.author = author  # 作者
        self.isbn = isbn  # 国际标准书号
        self.total_copies = total_copies  # 总复本数量
        self.borrowed_copies = 0  # 已借出的复本数量

    def is_available(self):
        """判断是否还有可借的复本"""
        return self.total_copies > self.borrowed_copies

    def borrow(self, student_id):
        """借书，增加借出的复本数量"""
        if self.is_available():
            self.borrowed_copies += 1
        else:
            print(f"{self.title} 已无可借复本")

    def return_book(self):
        """还书，减少借出的复本数量"""
        if self.borrowed_copies > 0:
            self.borrowed_copies -= 1

    def get_availability(self):
        """获取书籍当前可用的复本数"""
        available_copies = self.total_copies - self.borrowed_copies
        return available_copies
class Librarian:
    def __init__(self, librarian_id, name):
        self.librarian_id = librarian_id  # 管理员编号
        self.name = name  # 姓名
        self.books_managed = {}  # 图书管理列表 (书名: 书籍对象)

    def add_book(self, book):
        """添加新书到图书馆"""
        self.books_managed[book.title] = book
        print(f"{book.title} 已添加到图书馆")

    def remove_book(self, book_title):
        """从图书馆移除一本书"""
        if book_title in self.books_managed:
            del self.books_managed[book_title]
            print(f"{book_title} 已从图书馆移除")
        else:
            print(f"图书馆中没有 {book_title}")

    def view_all_books(self):
        """查看图书馆中所有的书籍信息"""
        if self.books_managed:
            print("图书馆中的书籍:")
            for title, book in self.books_managed.items():
                available_copies = book.get_availability()
                print(f"- {title} (可借复本: {available_copies}/{book.total_copies})")
        else:
            print("图书馆当前没有书籍")
class CarManufacturer:
    def __init__(self, brand, model, year, engine_type, production_quantity):
        self.brand = brand  # 品牌
        self.model = model  # 车型
        self.year = year  # 出厂年份
        self.engine_type = engine_type  # 发动机类型（如汽油、电动等）
        self.production_quantity = production_quantity  # 生产数量

    def produce_car(self, quantity):
        """增加生产数量"""
        self.production_quantity += quantity
        print(f"{self.brand} {self.model} 增加生产了 {quantity} 台车")

    def get_car_info(self):
        """获取汽车型号信息"""
        return f"{self.year} {self.brand} {self.model}, Engine: {self.engine_type}, Produced: {self.production_quantity} units"
class CarOwner:
    def __init__(self, owner_name, license_plate, car_model, mileage, fuel_level):
        self.owner_name = owner_name  # 车主姓名
        self.license_plate = license_plate  # 车牌号
        self.car_model = car_model  # 车型
        self.mileage = mileage  # 里程
        self.fuel_level = fuel_level  # 油量百分比 (0-100)

    def drive(self, distance):
        """驾驶汽车，增加里程，减少油量"""
        fuel_consumed = distance * 0.1  # 每10公里消耗1%的油
        if self.fuel_level >= fuel_consumed:
            self.mileage += distance
            self.fuel_level -= fuel_consumed
            print(f"{self.owner_name} 驾驶 {self.car_model} 行驶了 {distance} 公里。")
        else:
            print("油量不足，请加油！")

    def refuel(self, amount):
        """加油，增加油量"""
        if self.fuel_level + amount <= 100:
            self.fuel_level += amount
            print(f"已加油 {amount}%，当前油量为 {self.fuel_level}%")
        else:
            print("加油量超出最大油箱容量")

    def get_car_status(self):
        """获取汽车当前状态（里程和油量）"""
        return f"车主: {self.owner_name}, 车牌: {self.license_plate}, 型号: {self.car_model}, 里程: {self.mileage} 公里, 油量: {self.fuel_level}%"
class TrafficAuthority:
    def __init__(self, license_plate, registration_status, inspection_status, violations):
        self.license_plate = license_plate  # 车牌号
        self.registration_status = registration_status  # 登记状态（有效/无效）
        self.inspection_status = inspection_status  # 年检状态（已通过/未通过）
        self.violations = violations  # 交通违规记录（列表）

    def register_car(self):
        """登记车辆"""
        if self.registration_status == "无效":
            self.registration_status = "有效"
            print(f"车牌号 {self.license_plate} 已登记")
        else:
            print(f"车牌号 {self.license_plate} 已经有效登记")

    def inspect_car(self):
        """年检车辆"""
        if self.inspection_status == "未通过":
            self.inspection_status = "已通过"
            print(f"车牌号 {self.license_plate} 已通过年检")
        else:
            print(f"车牌号 {self.license_plate} 已通过年检，无需再次年检")

    def add_violation(self, violation):
        """增加交通违规记录"""
        self.violations.append(violation)
        print(f"车牌号 {self.license_plate} 新增了违规记录：{violation}")

    def get_car_status(self):
        """获取车辆在交通管理机构的状态"""
        return f"车牌: {self.license_plate}, 登记状态: {self.registration_status}, 年检状态: {self.inspection_status}, 违规记录: {self.violations}"
