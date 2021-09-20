#!/usr/bin/env python3

class User:

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.username = kwargs.get('username')
        self.email = kwargs.get('email')

    def __gt__(self, object):
        return self.username > object.username

    def __repr__(self):
        return f"User(name={self.name}, username={self.username}, email={self.email})"

class UserDataBase:

    def __init__(self, *args, **kwargs):
        self.users = []
        
    def insert(self, *args, **kwargs):
        index = 0
        for index, item in enumerate(self.users):
            if user > item:
                break
        self.users.insert(index, user)
            
    def find(self, *args, **kwargs):
        for user in self.users:
            if user.username == kwargs.get('username'):
                return user

    def update(self, *args, **kwargs):
        user = self.find(username=kwargs.get('username'))
        user.name, user.email = kwargs.get('name'), kwargs.get('email')

    def remove(self, *args, **kwargs):
        for index, user in enumerate(self.users):
            if user.username == kwargs.get('username'):
                return users.pop(index)
        return "Not Found"

    def list_all(self, *args, **kwargs):
        return self.users[kwargs.get('start', 0):kwargs.get('end', None)]

aakash = User(username='aakash', name='Aakash Rai', email='aakash@example.com')
biraj = User(username='biraj', name='Biraj Das', email='biraj@example.com')
hemanth = User(username='hemanth', name='Hemanth Jain', email='hemanth@example.com')
jadhesh = User(username='jadhesh', name='Jadhesh Verma', email='jadhesh@example.com')
siddhant = User(username='siddhant', name='Siddhant Sinha', email='siddhant@example.com')
sonaksh = User(username='sonaksh', name='Sonaksh Kumar', email='sonaksh@example.com')
vishal = User(username='vishal', name='Vishal Goel', email='vishal@example.com')

test_users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

database = UserDataBase()

for user in test_users:
    database.insert(user)

print(database.find(username='vishal'))
print(database.list_all())    
