from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "mysql+mysqlconnector://root:tde1234@localhost/mydb"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    idEmployees = Column(Integer, primary_key=True)
    nameEmployee = Column(String(50))
    age = Column(Integer)
    cellphoneNumber = Column(String(20))
    address = Column(String(100))
    position = Column(String(50))

class ClientPeople(Base):
    __tablename__ = 'clients_people'
    idClient_People = Column(Integer, primary_key=True)
    name = Column(String(50))
    category = Column(String(50))
    addressJob = Column(String(100))
    delivery_PickUp = Column(String(100))
    driver = Column(String(50))

class ClientCompany(Base):
    __tablename__ = 'clients_company'
    idCompany = Column(Integer, primary_key=True)
    name = Column(String(50))
    cnpj = Column(String(20))
    category = Column(String(50))
    addressJob = Column(String(100))
    deliveryPickUp = Column(String(100))
    driver = Column(String(50))

class ChemicalToilet(Base):
    __tablename__ = 'chemical_toilets'
    idToilet = Column(Integer, primary_key=True)
    model = Column(String(50))
    category = Column(String(50))
    alocated = Column(String(50))

class Truck(Base):
    __tablename__ = 'trucks'
    idTruck = Column(Integer, primary_key=True)
    model = Column(String(50))
    brand = Column(String(50))
    driver = Column(String(50))


def employees():
    option = int(input("What do you want to change in the employees?\n Type 1 to add employees.\n Type 2 to update an employee's information.\n Type 3 to read an employee's information.\n Type 4 to delete an employee from the database!\n"))

    if option == 1:
        name = input("Enter the name of the new employee: ")
        age = int(input("Enter the age of the new employee: "))
        cellphone = input("Enter the cellphone number of the new employee: ")
        address = input("Enter the address of the new employee: ")    
        position = input("Enter the position of the new employee: ")
        
        new_employee = Employee(nameEmployee=name, age=age, cellphoneNumber=cellphone, address=address, position=position)
        session.add(new_employee)
        session.commit()
    
    elif option == 2:
        changes = int(input("What do you want to change in your employee's database?\n Type 1 to change the employee's name.\n Type 2 to change the employee's age.\n Type 3 to change the employee's cellphone number.\n Type 4 to change the employee's address.\n Type 5 to change the employee's position.\n"))
        id = int(input("Enter the ID of the employee you want to change: "))
        employee = session.query(Employee).filter(Employee.idEmployees == id).first()

        if changes == 1:
            newName = input("Enter the new employee's name: ")
            employee.name = newName
        elif changes == 2:
            newAge = int(input("Update your employee's age: "))
            employee.age = newAge
        elif changes == 3:
            newPhone = input("Update your employee's cellphone number: ")
            employee.cellphoneNumber = newPhone
        elif changes == 4:
            newAddress = input("Update your employee's address: ")
            employee.address = newAddress
        elif changes == 5:
            newPosition = input("Enter your employee's new position: ")
            employee.position = newPosition
        else:
            print("Enter a valid value!")
        
        session.commit()
    
    elif option == 3:
        employees = session.query(Employee).all()
        for emp in employees:
            print(f"{emp.idEmployees}: {emp.nameEmployee}, {emp.age}, {emp.cellphoneNumber}, {emp.address}, {emp.position}")
    
    elif option == 4:
        id = int(input("Enter the ID of the employee you want to remove: "))
        employee = session.query(Employee).filter(Employee.idEmployees == id).first()
        session.delete(employee)
        session.commit()

    else:
        print("Enter a valid value!")



def clientsPeople():
    option = int(input("What do you want to change in the clients?\n Type 1 to add client.\n Type 2 to update a client's information.\n Type 3 to read a client's information.\n Type 4 to delete a client from the database!\n"))

    if option == 1:
        name = str(input("Enter the name of the new client: "))
        category = str(input("Enter the category of your client job: "))
        address = str(input("Enter the address of the client: "))
        deliveryPickUp = str(input("Enter the date to Delivery the Chemical Toilet and the date to Pick Up: "))
        driver = str(input("Enter the Driver who is in charge of this job: "))
        new_client = ClientPeople(name=name, category=category, addressJob=address, delivery_PickUp=deliveryPickUp, driver=driver)
        session.add(new_client)
        session.commit()

    elif option == 2:
        id = int(input("Enter the ID of the client you want to update: "))
        client = session.query(ClientPeople).filter(ClientPeople.idClient_People == id).first()
        if client:
            changes = int(input("What do you want to change?\n1. Name\n2. Category\n3. Address\n4. Delivery and PickUp\n5. Driver\n"))
            if changes == 1:
                new_name = input("Enter the new name: ")
                client.name = new_name
            elif changes == 2:
                new_category = input("Enter the new category: ")
                client.category = new_category
            elif changes == 3:
                new_address = input("Enter the new address: ")
                client.addressJob = new_address
            elif changes == 4:
                new_delivery_pickup = input("Enter the new delivery and pick-up: ")
                client.delivery_PickUp = new_delivery_pickup
            elif changes == 5:
                new_driver = input("Enter the new driver: ")
                client.driver = new_driver
            session.commit()

    elif option == 3:
        clients = session.query(ClientPeople).all()
        for client in clients:
            print(f"{client.idClient_People}: {client.name}, {client.category}, {client.addressJob}, {client.delivery_PickUp}, {client.driver}")

    elif option == 4:
        id = int(input("Enter the ID of the client you want to delete: "))
        client = session.query(ClientPeople).filter(ClientPeople.idClient_People == id).first()
        if client:
            session.delete(client)
            session.commit()


def clientsCompany():
    option = int(input("What do you want to change in the company?\n Type 1 to add a company.\n Type 2 to update a company's information.\n Type 3 to read a company's information.\n Type 4 to delete a company from the database!\n"))

    if option == 1:
        name = str(input("Enter the name of the company: "))
        category = str(input("Enter the category of your client job: "))
        cnpj = str(input("Enter the company CNPJ: "))
        address = str(input("Enter the address of the company: "))
        deliveryPickUp = str(input("Enter the date for delivery and pick-up: "))
        driver = str(input("Enter the driver responsible: "))
        new_company = ClientCompany(name=name, category=category, cnpj=cnpj, addressJob=address, deliveryPickUp=deliveryPickUp, driver=driver)
        session.add(new_company)
        session.commit()

    elif option == 2:
        id = int(input("Enter the ID of the company you want to update: "))
        company = session.query(ClientCompany).filter(ClientCompany.idCompany == id).first()
        if company:
            changes = int(input("What do you want to change?\n1. Name\n2. CNPJ\n3. Category\n4. Address\n5. Delivery and PickUp\n6. Driver\n"))
            if changes == 1:
                company.name = input("Enter the new name: ")
            elif changes == 2:
                company.cnpj = input("Enter the new CNPJ: ")
            elif changes == 3:
                company.category = input("Enter the new category: ")
            elif changes == 4:
                company.addressJob = input("Enter the new address: ")
            elif changes == 5:
                company.deliveryPickUp = input("Enter the new delivery and pick-up: ")
            elif changes == 6:
                company.driver = input("Enter the new driver: ")
            session.commit()

    elif option == 3:
        companies = session.query(ClientCompany).all()
        for company in companies:
            print(f"{company.idCompany}: {company.name}, {company.cnpj}, {company.category}, {company.addressJob}, {company.deliveryPickUp}, {company.driver}")

    elif option == 4:
        id = int(input("Enter the ID of the company you want to delete: "))
        company = session.query(ClientCompany).filter(ClientCompany.idCompany == id).first()
        if company:
            session.delete(company)
            session.commit()


def chemicalToilets():
    option = int(input("What do you want to change in the Chemical Toilets?\n Type 1 to add a Chemical Toilet.\n Type 2 to update a Chemical Toilet's information.\n Type 3 to read a Chemical Toilet's information.\n Type 4 to delete a Chemical Toilet from the database!\n"))

    if option == 1:
        model = input("Enter the model of the Chemical Toilet: ")
        category = input("Enter the category: ")
        alocated = input("Enter the Truck allocated to the Chemical Toilet: ")
        new_toilet = ChemicalToilet(model=model, category=category, alocated=alocated)
        session.add(new_toilet)
        session.commit()

    elif option == 2:
        id = int(input("Enter the ID of the Chemical Toilet you want to update: "))
        toilet = session.query(ChemicalToilet).filter(ChemicalToilet.idToilet == id).first()
        if toilet:
            changes = int(input("What do you want to change?\n1. Model\n2. Category\n3. Truck Allocated\n"))
            if changes == 1:
                toilet.model = input("Enter the new model: ")
            elif changes == 2:
                toilet.category = input("Enter the new category: ")
            elif changes == 3:
                toilet.alocated = input("Enter the new truck allocated: ")
            session.commit()

    elif option == 3:
        toilets = session.query(ChemicalToilet).all()
        for toilet in toilets:
            print(f"{toilet.idToilet}: {toilet.model}, {toilet.category}, {toilet.alocated}")

    elif option == 4:
        id = int(input("Enter the ID of the Chemical Toilet you want to delete: "))
        toilet = session.query(ChemicalToilet).filter(ChemicalToilet.idToilet == id).first()
        if toilet:
            session.delete(toilet)
            session.commit()


def trucks():
    option = int(input("What do you want to change in the Trucks?\n Type 1 to add a Truck.\n Type 2 to update a Truck's information.\n Type 3 to read a Truck's information.\n Type 4 to delete a Truck from the database!\n"))

    if option == 1:
        model = input("Enter the model of the truck: ")
        brand = input("Enter the brand: ")
        driver = input("Enter the driver's name: ")
        new_truck = Truck(model=model, brand=brand, driver=driver)
        session.add(new_truck)
        session.commit()

    elif option == 2:
        id = int(input("Enter the ID of the Truck you want to update: "))
        truck = session.query(Truck).filter(Truck.idTruck == id).first()
        if truck:
            changes = int(input("What do you want to change?\n1. Model\n2. Brand\n3. Driver\n"))
            if changes == 1:
                truck.model = input("Enter the new model: ")
            elif changes == 2:
                truck.brand = input("Enter the new brand: ")
            elif changes == 3:
                truck.driver = input("Enter the new driver: ")
            session.commit()

    elif option == 3:
        trucks = session.query(Truck).all()
        for truck in trucks:
            print(f"{truck.idTruck}: {truck.model}, {truck.brand}, {truck.driver}")

    elif option == 4:
        id = int(input("Enter the ID of the Truck you want to delete: "))
        truck = session.query(Truck).filter(Truck.idTruck == id).first()
        if truck:
            session.delete(truck)
            session.commit()

def main():
    print("\n Welcome to your BWC Quimico's Software.\n")
    action = int(input("Please choose an option.\n Enter 1 to manage your employees.\n Enter 2 to manage your Clients.\n Enter 3 to manage your Warehouse.\n"))
    
    if action == 1:
        employees()
    elif action == 2:
        option = int(input("Enter 1 to manage individual clients or 2 to manage company clients: "))
        if option == 1:
            clientsPeople()
        elif option == 2:
            clientsCompany()
    elif action == 3:
        option = int(input("Enter 1 to manage Chemical Toilets or 2 to manage Trucks: "))
        if option == 1:
            chemicalToilets()
        elif option == 2:
            trucks()


main()


session.close()
