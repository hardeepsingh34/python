import mysql.connector

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

# Sample data
addresses = [
    (1, 1, '123 Main Street', 'Patiala', 'Punjab', '147001'),
    (2, 2, '45 Green Avenue', 'Chandigarh', 'Chandigarh', '160017'),
    (3, 3, '78 MG Road', 'Bengaluru', 'Karnataka', '560001'),
    (4, 4, '12 Park Street', 'Kolkata', 'West Bengal', '700016'),
    (5, 5, '56 Marine Drive', 'Mumbai', 'Maharashtra', '400020'),
    (6, 6, '89 Anna Salai', 'Chennai', 'Tamil Nadu', '600002'),
    (7, 7, '34 Civil Lines', 'Jaipur', 'Rajasthan', '302006'),
    (8, 8, '67 Hazratganj', 'Lucknow', 'Uttar Pradesh', '226001'),
    (9, 9, '90 Banjara Hills', 'Hyderabad', 'Telangana', '500034'),
    (10, 10, '21 Ashram Road', 'Ahmedabad', 'Gujarat', '380009'),
    (11, 11, '15 Connaught Place', 'New Delhi', 'Delhi', '110001'),
    (12, 12, '42 FC Road', 'Pune', 'Maharashtra', '411004'),
    (13, 13, '88 Residency Road', 'Bengaluru', 'Karnataka', '560025'),
    (14, 14, '19 Sector 17', 'Chandigarh', 'Chandigarh', '160017'),
    (15, 15, '73 Mall Road', 'Amritsar', 'Punjab', '143001'),
    (16, 16, '25 Lalbagh Road', 'Bhopal', 'Madhya Pradesh', '462001'),
    (17, 17, '61 Fraser Road', 'Patna', 'Bihar', '800001'),
    (18, 18, '38 Civil Lines', 'Dehradun', 'Uttarakhand', '248001'),
    (19, 19, '52 Panaji Market', 'Panaji', 'Goa', '403001'),
    (20, 20, '14 Beach Road', 'Visakhapatnam', 'Andhra Pradesh', '530001')
]

# Insert records
query = """
INSERT INTO addresses (id, user_id, street, city, state, pincode)
VALUES (%s, %s, %s, %s, %s, %s)
"""

cursor.executemany(query, addresses)

# Commit changes
conn.commit()

print(cursor.rowcount, "records inserted successfully!")

# Close connection
cursor.close()
conn.close()