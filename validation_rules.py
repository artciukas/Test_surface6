validation_rules = {
    'validator': {
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['customer', 'product', 'quantity', 'price', 'date', 'status'],
            'properties': {
                'customer': {
                    'bsonType': 'string',
                    'description': 'Customer must be string',
                },
                'product': {
                    'bsonType': 'string',
                    'description': 'Product must by string',
                },
                'quantity': {
                    'bsonType': 'int',
                    'description': 'quantity must be integer',
                },
                'price': {
                    'bsonType': 'int',
                    'description': 'price must integer',
                },
                'date': {
                    'bsonType': 'string',
                    'description': 'date must be string',
                },
                'status': {
                    'bsonType': 'string',
                    'description': 'status must be string',
                },
            }
        }
    }
}