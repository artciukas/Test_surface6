"""
Create a project to test all pipelines we talked today. 
Project has to have a description, full explanation with subtasks. 
Code must have full project lifecycle (github with all explanations, 
env, brnaching etc.) . 
Pymongo implementation should contain OOP implementation, 
schema validation if applicable and error handling. 
Every pipeline has to have non identical database.
"""

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.errors import ConnectionFailure, PyMongoError, ServerSelectionTimeoutError, OperationFailure
from typing import Dict, Any
from validation_rules import validation_rules
from data_pc import sales
from typing import List




class Employee:

    product_price = {'Laptop': 1000, 'Desctop': 3000, 'Tablet': 300, 'Keyboard': 30, 'Mouse': 33}

    def __init__(self, host: str, port: int, db_name: str, collection: str):
        self.host = host
        self.port = port
        self.client = MongoClient(host, port)
        self.db= self.client[db_name]
        self.collection = self.db[collection]
        # return self.database
    

    def connect_to_db(self) -> MongoClient:
        connection = f"{self.host}:{self.port}"
        try:
            client = MongoClient(f"mongodb://{connection}",serverSelectionTimeoutMS=5000)
            client.server_info()
            return client
        except ServerSelectionTimeoutError as e:
            print("Connection failure:", str(e))
            return None
        except PyMongoError as e:
            print("An error occurred:", str(e))
            return None


    def enable_validation_and_write_to_db(self, collection,document):
        try:    
            self.db.command("collMod", self.collection.name, **validation_rules)
            print("Schema validation enabled.")
            result = self.write_document_to_db(collection = collection, document=document)
        except OperationFailure as e:
            print(f"Failed to enable schema validation: {e.details['errmsg']}")
        return result

    def write_many_documents_to_db(self, document, collection):
        print('Hello')
        result = self.db[collection].insert_many(document)
        return str(result.inserted_ids)
    
    def write_document_to_db(self, document, collection):
        result = self.db[collection].insert_one(document)
        return str(result.inserted_id)

    # getting data from user

    def get_customer_form_user(self):
        while True:
            try:
                customer_input = input("Please enter Customer name: ")
                break
            except Exception as e:
                print(f"Error: {e}")  
        return customer_input

    def get_product_form_user(self):
        while True:
            try:
                list_of_varaints = ['Laptop', 'Desctop', 'Tablet','Keyboard', 'Mouse']
                print('Laptop', 'Desctop', 'Tablet','Keyboard', 'Mouse')
                product_input = input("Please enter product : ")
                if product_input not in list_of_varaints:
                    print('Avable products are: Laptop, Desctop, Tablet, Keyboard , Mouse')
                else:
                    break
            except Exception as e:
                print(f"Error: {e}") 
        return product_input


    def get_quantity_form_user(self):
        while True:
            try:
                quantity_input = int(input("Please enter quantity: "))
                break
            except ValueError:
                print('Quantity must by integer') 
        return quantity_input


    def get_price_from_product(self, product_input):
        price = self.product_price.get(product_input)
        return price

        
    def get_document(self):
        document = {}
        customer = self.get_customer_form_user()
        product = self.get_product_form_user()
        quantity = self.get_quantity_form_user()
        price = self.get_price_from_product(product)
        date = '2023-06-26'
        document["customer"]  = customer
        document["product"] = product
        document["quantity"] = quantity
        document["price"] = price
        document["date"] = date
        document["status"] = 'active'
        return document
    



    def filter_documents(self, filter_criteria: Dict[str, Any]) -> Cursor:
        pipeline = [
            {
                '$match': filter_criteria
            }
        ]
        return self.collection.aggregate(pipeline)
    
    def sort_documents(self, sort_criteria: Dict[str, int]) -> Cursor:
        pipeline = [
            {
                '$sort': sort_criteria
            }
        ]
        return self.collection.aggregate(pipeline)
    
    def filter_documents_by_products(self, filter_criteria: List[Dict[str, Any]]) -> Cursor:
        pipeline = [
            {
                '$match': {
                    '$and': filter_criteria
                }
            }
        ]
        return self.collection.aggregate(pipeline)
    
    def project_documents(self, projection_fields: Dict[str, int]) -> Cursor:
        pipeline = [
            {
                '$project': projection_fields
            }
        ]
        return self.collection.aggregate(pipeline)
    

    def aggregate_documents(self, pipeline: Dict[str, Any]) -> Cursor:
        return self.collection.aggregate(pipeline)


  

if __name__ == "__main__":
    pass

    
