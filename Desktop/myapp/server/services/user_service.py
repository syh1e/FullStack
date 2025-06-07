from repositories.user_repository import UserRepository
from models.user import User
from typing import Optional

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def register(self, user_id: str, password: str, name: str, school: str) -> None:
        if not self.repository.is_id_available(user_id):
            raise ValueError('이미 사용 중인 아이디입니다.')

        user = User(
            id=user_id,
            password=password,  # 실제로는 여기서 비밀번호 해싱을 해야 합니다
            name=name,
            school=school
        )
        self.repository.create(user)

    def login(self, user_id: str, password: str) -> Optional[User]:
        user = self.repository.get_by_id(user_id)
        if not user:
            return None

        if user.password != password:  # 실제로는 해시된 비밀번호를 비교해야 합니다
            return None

        return user 