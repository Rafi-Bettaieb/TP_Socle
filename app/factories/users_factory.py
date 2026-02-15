import json
from typing import List
from app.factories.users_factory_protocol import UserFactoryProtocol
from app.models.user_model import UserModel

class UsersFactory(UserFactoryProtocol):

    def create_users(self, file_path: str) -> List[UserModel]:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        if "users" not in data:
            raise ValueError("no users found")
            
        return [UserModel(**user) for user in data["users"]]