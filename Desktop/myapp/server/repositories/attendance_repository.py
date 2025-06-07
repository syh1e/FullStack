from utils.database import DatabaseConnection
from models.attendance import Attendance, AttendanceVerification
from datetime import datetime, timedelta
import random
from typing import List, Optional

class AttendanceRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def start_attendance(self, study_id: int) -> AttendanceVerification:
        # Generate random code and expiration time
        code = str(random.randint(1000, 9999))
        expires_at = datetime.now() + timedelta(minutes=10)
        today = datetime.now().date()

        # Delete existing records
        self.db.execute('DELETE FROM attendance_verification WHERE study_id = %s', (study_id,))
        self.db.execute('DELETE FROM attendance WHERE study_id = %s AND date = %s',
                       (study_id, today.isoformat()))

        # Insert new verification
        query = '''
            INSERT INTO attendance_verification (study_id, code, expires_at)
            VALUES (%s, %s, %s)
        '''
        self.db.execute(query, (study_id, code, expires_at.isoformat()))
        verification_id = self.db.cursor.lastrowid

        # Get leader ID
        leader_result = self.db.fetch_one('SELECT leader_id FROM studies WHERE id = %s', (study_id,))
        if leader_result:
            leader_id = leader_result['leader_id']
            # Get all participants excluding leader
            participants = self.db.fetch_all('''
                SELECT user_id FROM study_participants
                WHERE study_id = %s AND user_id != %s
            ''', (study_id, leader_id))

            # Insert initial 'absent' records
            for participant in participants:
                self.db.execute('''
                    INSERT INTO attendance (study_id, user_id, status, date)
                    VALUES (%s, %s, %s, %s)
                ''', (study_id, participant['user_id'], 'absent', today.isoformat()))

        return AttendanceVerification(
            study_id=study_id,
            code=code,
            expires_at=expires_at,
            verification_id=verification_id
        )

    def verify_attendance(self, study_id: int, user_id: str, code: str) -> bool:
        # Check verification code
        verification = self.get_active_verification(study_id)
        if not verification:
            raise ValueError('인증이 시작되지 않았습니다.')

        if verification.code != code:
            raise ValueError('잘못된 인증 코드입니다.')

        if datetime.now() > verification.expires_at:
            raise ValueError('인증 시간이 만료되었습니다.')

        # Check if already verified
        if self.is_verified(study_id, user_id, verification.verification_id):
            raise ValueError('이미 출석했습니다.')

        # Record attendance
        today = datetime.now().date()
        self.db.execute('''
            INSERT INTO attendance (study_id, user_id, status, date, attendance_verification_id)
            VALUES (%s, %s, %s, %s, %s)
        ''', (study_id, user_id, 'present', today.isoformat(), verification.verification_id))

        return True

    def get_active_verification(self, study_id: int) -> Optional[AttendanceVerification]:
        query = '''
            SELECT id as verification_id, study_id, code, expires_at
            FROM attendance_verification
            WHERE study_id = %s AND expires_at > NOW()
            ORDER BY expires_at DESC LIMIT 1
        '''
        result = self.db.fetch_one(query, (study_id,))
        return AttendanceVerification.from_dict(result) if result else None

    def is_verified(self, study_id: int, user_id: str, verification_id: int) -> bool:
        query = '''
            SELECT 1 FROM attendance
            WHERE study_id = %s AND user_id = %s AND attendance_verification_id = %s
        '''
        result = self.db.fetch_one(query, (study_id, user_id, verification_id))
        return result is not None

    def get_attendance_records(self, study_id: int) -> List[Attendance]:
        query = '''
            SELECT a.*, u.name
            FROM attendance a
            JOIN users u ON a.user_id = u.id
            WHERE a.study_id = %s
            ORDER BY a.date DESC
        '''
        results = self.db.fetch_all(query, (study_id,))
        return [Attendance.from_dict(result) for result in results]

    def end_attendance(self, study_id: int) -> None:
        self.db.execute('DELETE FROM attendance_verification WHERE study_id = %s', (study_id,)) 