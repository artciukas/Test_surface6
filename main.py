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
from typing import Dict, Any



class Employee:

    def __init__(self, host: str, port: int, db_name: str, collection: str):
        self.client = MongoClient(host, port)
        self.db= self.client[db_name]
        self.collection = self.db[collection]
        # return self.database
    
    def write_document_to_db(self, document, collection):
        result = self.db[collection].insert_one(document)
        return str(result.inserted_id)
    
    
    def get_document(self):
        document = {}
        name = input("Please enter your name: ")
        working_time = input("Please enter working time: ")
        specialization = input("Please enter specialization: ")
        hourly_rate = input("Please enter hourly_rate: ")
        salary = input("Please enter salary: ")
        document["name"]  = name
        document["working_time"] = working_time
        document["specialization"] = specialization
        document["hourly_rate"] = hourly_rate
        document["salary"] = salary
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
  

if __name__ == "__main__":
    
    mongo_host = "0.0.0.0"
    mongo_port = 27017
    mongo_db_name = "Employee_DB"
    collection='employee'
    

    db = Employee(mongo_host, mongo_port, mongo_db_name, collection)
    # document = db.get_document()
    # db.write_document_to_db(collection='employee', document=document)

    # filter by specialization
    # criteria = {'specialization': 'IT'}
    # result = db.filter_documents(criteria)

    criteria: Dict[str, int] = {'working_time': 1} 
    result = db.sort_documents(criteria)

    for doc in result:
        print(doc)

