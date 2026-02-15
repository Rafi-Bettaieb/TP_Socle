from typing import Protocol, List
from app.models.user_model import UserModel

class UserFactoryProtocol(Protocol):
    
    def create_users(self, file_path: str) -> List[UserModel]:
        ...