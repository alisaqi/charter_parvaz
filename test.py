"""
Test file for flight data structures.
This file contains sample data structures for testing purposes.
"""

# Sample flight result structure
result = {
    1: {
        'Price': '7,406,100',
        'freeSeats': '5',
        'departure': '20:00',
        'company': 'هواپیمایی معراج',
        'flightNumber': '4805'
    },
    2: {
        'Price': '7,406,100',
        'freeSeats': '5',
        'departure': '22:00',
        'company': 'هواپیمایی آتا',
        'flightNumber': '6609'
    },
    3: {
        'Price': '7,406,100',
        'freeSeats': '3',
        'departure': '08:00',
        'company': 'هواپیمایی آتا',
        'flightNumber': '6619'
    }
}

if __name__ == "__main__":
    # Test accessing first and last keys
    print("First key:", list(result.keys())[0])
    print("Last key:", list(result.keys())[-1])