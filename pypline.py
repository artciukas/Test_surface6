from typing import Dict, Any

pipeline: Dict[str, Any] = [
    {
        '$match': {
            'product': 'Tablet',  # Filter documents by the 'category' field
            'quantity': {'$gte': 3}      # Filter documents where 'price' is greater than or equal to 500
        }
    },
    {
        '$sort': {'status': 1}         # Sort documents by 'price' in descending order
    },
    {
        '$project': {
            '_id': 0,                   # Exclude the '_id' field from the projection
            'customer': 1,
            "product": 1,               # Include the 'name' field in the projection
            'date': 1,                 # Include the 'price' field in the projection
                        # Include the 'brand' field in the projection
        }
    }
]
