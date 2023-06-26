from main import Employee
from typing import Dict, List, Any
from pymongo.cursor import Cursor
from pypline import pipeline

mongo_host = "0.0.0.0"
mongo_port = 27017
mongo_db_name = "Sales"
collection='Sales_PC'

db = Employee(mongo_host, mongo_port, mongo_db_name, collection)

client = db.connect_to_db()
if client is not None:
    print("Connected to MongoDB successfully.")
else:
    print("Failed to connect to MongoDB.")


while True:

    choice = input("1 - enter data to DB \n2 - find status done\n3 - sort by customer\n4 - Filter: Desctop or Keyboard quantity < 20\n5 - Show only customer, product, quantity\n6 - Return Product tablet, quantity > 3 sort from a to z\n0 - exit\n")

    match choice:
        case '1':
            document = db.get_document()
            answer = db.enable_validation_and_write_to_db(collection, document)
            print(f'Document was created!!!\nGenerated id is: {answer}')
            print("#####################=- END -=#####################")
            
        case '2': 
            criteria = {'status': 'done'}
            result = db.filter_documents(criteria)
            print("#####################=- filter by done -=#####################")
            for doc in result:
                print(doc)
            print("#####################=- END -=#####################")

        case '3':
            print("#####################=- sorted by customer -=#####################")
            criteria: Dict[str, int] = {'customer': 1} 

            try:
                result = db.sort_documents(criteria)
            except Exception as e:
                print(f"Failed to insert document: {e}")

            for doc in result:
                print(doc)
            print("#####################=- END -=#####################")

        case '4':
            print("#####################=- Desctop or Keyboard quantity < 20 -=#####################")
            criteria: List[Dict[str, Any]] = [
                {'status': 'active'},
                {'$or': [{'product': 'Desctop'}, {'product': 'Keyboard'}]},
            ]
            try:
                result: Cursor = db.filter_documents_by_products(criteria)
            except Exception as e:
                print(f"Failed to insert document: {e}")

            for doc in result:
                print(doc)
            print("#####################=- END -=#####################")

        case '5':
            print("#####################=- Show only customer, product, quantity -=#####################")
    
            projection: Dict[str, int] = {
                '_id': 0,
                'customer': 1,
                'product': 1,
                "quantity": 1
            }
            try:
                result: Cursor =  db.project_documents(projection) 
            except Exception as e:
                print(f"Failed to insert document: {e}")

            for doc in result:
                print(doc)
            print("#####################=- END -=#####################")
        case '6':
            print("#####################=- Return Product tablet, quantity > 3 sort from a to z.-=#####################")
    
            result: Cursor = db.aggregate_documents(pipeline)
            
            for doc in result:
                print(doc)
            print("#####################=- END -=#####################")
        case '0':
            print("Goodbye")
            break

        case other:
            print("Wrong command!!!")