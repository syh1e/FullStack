from repositories.attendance_repository import AttendanceRepository
from repositories.study_repository import StudyRepository
from models.attendance import AttendanceVerification, Attendance
from typing import List

class AttendanceService:
    def __init__(self):
        self.attendance_repo = AttendanceRepository()
        self.study_repo = StudyRepository()

    def start_attendance(self, study_id: int) -> AttendanceVerification:
        # Verify study exists
        if not self.study_repo.get_by_id(study_id):
            raise ValueError('존재하지 않는 스터디입니다.')
        return self.attendance_repo.start_attendance(study_id)

    def verify_attendance(self, study_id: int, user_id: str, code: str) -> bool:
        # Verify study exists and user is participant
        if not self.study_repo.get_by_id(study_id):
            raise ValueError('존재하지 않는 스터디입니다.')
        if not self.study_repo.is_participant(study_id, user_id):
            raise ValueError('해당 스터디의 참여자가 아닙니다.')
        return self.attendance_repo.verify_attendance(study_id, user_id, code)

    def get_attendance_records(self, study_id: int) -> List[Attendance]:
        if not self.study_repo.get_by_id(study_id):
            raise ValueError('존재하지 않는 스터디입니다.')
        return self.attendance_repo.get_attendance_records(study_id)

    def end_attendance(self, study_id: int) -> None:
        if not self.study_repo.get_by_id(study_id):
            raise ValueError('존재하지 않는 스터디입니다.')
        self.attendance_repo.end_attendance(study_id) 