from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: str
    password: str
    name: str
    school: str
    created_at: datetime = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            password=data['password'],
            name=data['name'],
            school=data['school'],
            created_at=datetime.fromisoformat(data['created_at']) if data.get('created_at') else None
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'school': self.school,
            'created_at': self.created_at.isoformat() if self.created_at else None
        } 