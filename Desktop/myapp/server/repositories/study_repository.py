from utils.database import DatabaseConnection
from models.study import Study
from typing import List

class StudyRepository:
    def __init__(self):
        self.db = DatabaseConnection()

    def create(self, study: Study) -> None:
        query = '''
            INSERT INTO studies (name, description, schedule, week_count, leader_id)
            VALUES (%s, %s, %s, %s, %s)
        '''
        self.db.execute(query, (
            study.name,
            study.description,
            study.schedule,
            study.week_count,
            study.leader_id
        ))

    def get_all(self) -> List[Study]:
        query = '''
            SELECT s.*, u.name as leader_name,
                (SELECT COUNT(*) FROM study_participants WHERE study_id = s.id) + 1 as participant_count
            FROM studies s
            JOIN users u ON s.leader_id = u.id
            ORDER BY s.created_at DESC
        '''
        results = self.db.fetch_all(query)
        return [Study.from_dict(result) for result in results]

    def get_by_id(self, study_id: int) -> Study:
        query = '''
            SELECT s.*, u.name as leader_name,
                (SELECT COUNT(*) FROM study_participants WHERE study_id = s.id) + 1 as participant_count
            FROM studies s
            JOIN users u ON s.leader_id = u.id
            WHERE s.id = %s
        '''
        result = self.db.fetch_one(query, (study_id,))
        return Study.from_dict(result) if result else None

    def get_by_leader(self, leader_id: str) -> List[Study]:
        query = '''
            SELECT s.*, u.name as leader_name,
                (SELECT COUNT(*) FROM study_participants WHERE study_id = s.id) + 1 as participant_count
            FROM studies s
            JOIN users u ON s.leader_id = u.id
            WHERE s.leader_id = %s
            ORDER BY s.created_at DESC
        '''
        results = self.db.fetch_all(query, (leader_id,))
        return [Study.from_dict(result) for result in results]

    def get_joined_studies(self, user_id: str) -> List[Study]:
        query = '''
            SELECT s.*, u.name as leader_name,
                (SELECT COUNT(*) FROM study_participants WHERE study_id = s.id) + 1 as participant_count
            FROM studies s
            JOIN users u ON s.leader_id = u.id
            JOIN study_participants sp ON s.id = sp.study_id
            WHERE sp.user_id = %s AND s.leader_id != %s
            ORDER BY s.created_at DESC
        '''
        results = self.db.fetch_all(query, (user_id, user_id))
        return [Study.from_dict(result) for result in results]

    def update(self, study: Study) -> None:
        query = '''
            UPDATE studies
            SET name = %s, description = %s, schedule = %s, week_count = %s
            WHERE id = %s
        '''
        self.db.execute(query, (
            study.name,
            study.description,
            study.schedule,
            study.week_count,
            study.id
        ))

    def delete(self, study_id: int) -> None:
        # Delete related records first
        self.db.execute('DELETE FROM study_participants WHERE study_id = %s', (study_id,))
        self.db.execute('DELETE FROM studies WHERE id = %s', (study_id,))

    def add_participant(self, study_id: int, user_id: str) -> None:
        query = 'INSERT INTO study_participants (study_id, user_id) VALUES (%s, %s)'
        self.db.execute(query, (study_id, user_id))

    def remove_participant(self, study_id: int, user_id: str) -> None:
        query = 'DELETE FROM study_participants WHERE study_id = %s AND user_id = %s'
        self.db.execute(query, (study_id, user_id))

    def is_participant(self, study_id: int, user_id: str) -> bool:
        query = 'SELECT 1 FROM study_participants WHERE study_id = %s AND user_id = %s'
        result = self.db.fetch_one(query, (study_id, user_id))
        return result is not None 