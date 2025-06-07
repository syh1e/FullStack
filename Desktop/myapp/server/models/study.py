from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Study:
    id: int
    name: str
    description: str
    schedule: str
    week_count: int
    leader_id: str
    created_at: datetime
    leader_name: Optional[str] = None
    participant_count: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            schedule=data['schedule'],
            week_count=data['week_count'],
            leader_id=data['leader_id'],
            created_at=datetime.fromisoformat(data['created_at']),
            leader_name=data.get('leader_name'),
            participant_count=data.get('participant_count')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'schedule': self.schedule,
            'week_count': self.week_count,
            'leader_id': self.leader_id,
            'created_at': self.created_at.isoformat(),
            'leader_name': self.leader_name,
            'participant_count': self.participant_count
        } 