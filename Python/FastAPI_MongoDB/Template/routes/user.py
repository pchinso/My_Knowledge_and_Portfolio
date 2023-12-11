from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()

# get  endpoints
@user.get('/users')
def find_all_user():
  return usersEntity(conn.local.user.find())

@user.get('/users/{id}')
def find_user():
  return('List of users')

# post endpoints
@user.post('/users')
def create_user(user:User):
  new_user = dict(user)
  del new_user['id']

  id = conn.local.user.insert_one(new_user).inserted_id

  user = conn.local.user.find_one({'_id': id})
  
  return userEntity(user)


# put endpoints
@user.get('/users/{id}')
def update_user():
  return('List of users')

# delete endpoint
@user.delete('/users/{id}')
def delete_user():
  return('List of users')