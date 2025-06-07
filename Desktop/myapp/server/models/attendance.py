from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Attendance:
    id: int
    study_id: int
    user_id: str
    status: str
    date: datetime
    attendance_verification_id: Optional[int] = None
    name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            study_id=data['study_id'],
            user_id=data['user_id'],
            status=data['status'],
            date=datetime.fromisoformat(data['date']),
            attendance_verification_id=data.get('attendance_verification_id'),
            name=data.get('name')
        )

    def to_dict(self):
        return {
            'id': self.id,
            'study_id': self.study_id,
            'user_id': self.user_id,
            'status': self.status,
            'date': self.date.isoformat(),
            'attendance_verification_id': self.attendance_verification_id,
            'name': self.name
        }

@dataclass
class AttendanceVerification:
    study_id: int
    code: str
    expires_at: datetime
    verification_id: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            study_id=data['study_id'],
            code=data['code'],
            expires_at=datetime.fromisoformat(data['expires_at']),
            verification_id=data.get('verification_id')
        )

    def to_dict(self):
        return {
            'study_id': self.study_id,
            'code': self.code,
            'expires_at': self.expires_at.isoformat(),
            'verification_id': self.verification_id
        } 