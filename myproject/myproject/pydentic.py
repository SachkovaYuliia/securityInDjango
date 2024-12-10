# main.py
# from pydentic import BaseModel, validate
#
#
# class User(BaseModel):
#     id: int
#     name: str
#     email: str
#     @validator("age")
#     def validate_age(cls, value):
#         if(value<10):
#             raise ValueError("ВІка має бути більше 18")
#         return value
    
#
# user1 = User(id=1, name="Ivan", email='ivan@gmail.com')
# data = {"id"=2, "name"= "MAxim", "email": "eee@gmail.com"}
# try:
#     user2 = User(**data)
#     print("Дані провалідовано успішно")
# except ValueError as e:
# print(e)