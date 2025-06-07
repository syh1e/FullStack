from utils.database import DatabaseConnection
from models.user import User

class UserRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def create(self, user: User) -> None:
        query = '''
            INSERT INTO users (id, password, name, school)
            VALUES (%s, %s, %s, %s)
        '''
        self.db.execute(query, (user.id, user.password, user.name, user.school))

    def get_by_id(self, user_id: str) -> User:
        query = 'SELECT * FROM users WHERE id = %s'
        result = self.db.fetch_one(query, (user_id,))
        return User.from_dict(result) if result else None

    def is_id_available(self, user_id: str) -> bool:
        return self.get_by_id(user_id) is None 