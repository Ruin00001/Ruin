from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse

class User:
    def __init__(
            self,
            id: int,
            user_name: str,
            status: str
    ):
        self.id = id
        self.user_name = user_name
        self.status = status

users = []

def find_all():
    return users


def create(user_create):
    for user in users:
        if user.user_name == user_create.get("user_name"):
            #update
            user.status = user_create.get("status")
            return "user is updated!"
    new_user = User(
        id = len(users)+1,
        user_name = user_create.get("user_name"),
        status = user_create.get("status")
    )
    print(new_user)
    users.append(new_user)
    return "user is created"
        
    
    


