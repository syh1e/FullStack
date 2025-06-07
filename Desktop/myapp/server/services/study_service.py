from repositories.study_repository import StudyRepository
from models.study import Study
from typing import List

class StudyService:
    def __init__(self):
        self.repository = StudyRepository()

    def create_study(self, name: str, description: str, schedule: str, week_count: int, leader_id: str) -> Study:
        study = Study(
            id=0,  # Will be set by database
            name=name,
            description=description,
            schedule=schedule,
            week_count=week_count,
            leader_id=leader_id,
            created_at=None  # Will be set by database
        )
        self.repository.create(study)
        return study

    def get_all_studies(self) -> List[Study]:
        return self.repository.get_all()

    def get_study_by_id(self, study_id: int) -> Study:
        study = self.repository.get_by_id(study_id)
        if not study:
            raise ValueError('존재하지 않는 스터디입니다.')
        return study

    def get_studies_by_leader(self, leader_id: str) -> List[Study]:
        return self.repository.get_by_leader(leader_id)

    def get_joined_studies(self, user_id: str) -> List[Study]:
        return self.repository.get_joined_studies(user_id)

    def update_study(self, study_id: int, name: str, description: str, schedule: str, week_count: int) -> None:
        study = self.get_study_by_id(study_id)
        study.name = name
        study.description = description
        study.schedule = schedule
        study.week_count = week_count
        self.repository.update(study)

    def delete_study(self, study_id: int) -> None:
        self.repository.delete(study_id)

    def join_study(self, study_id: int, user_id: str) -> None:
        if self.repository.is_participant(study_id, user_id):
            raise ValueError('이미 참여 중인 스터디입니다.')
        self.repository.add_participant(study_id, user_id)

    def leave_study(self, study_id: int, user_id: str) -> None:
        if not self.repository.is_participant(study_id, user_id):
            raise ValueError('참여 중이 아닌 스터디입니다.')
        self.repository.remove_participant(study_id, user_id) 