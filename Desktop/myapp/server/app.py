from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from services.user_service import UserService
from services.study_service import StudyService
from services.attendance_service import AttendanceService
from datetime import timedelta

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # 실제 운영 환경에서는 환경 변수로 관리해야 합니다
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
jwt = JWTManager(app)

user_service = UserService()
study_service = StudyService()
attendance_service = AttendanceService()

# 인증 관련 엔드포인트
@app.route('/api/auth/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user_service.register(
            data['id'],
            data['password'],
            data['name'],
            data['school']
        )
        return jsonify({'message': '회원가입이 완료되었습니다.'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = user_service.login(data['id'], data['password'])
        if not user:
            return jsonify({'error': '아이디 또는 비밀번호가 일치하지 않습니다.'}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'user': user.to_dict()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 스터디 관련 엔드포인트
@app.route('/api/studies', methods=['POST'])
@jwt_required()
def create_study():
    try:
        data = request.get_json()
        user_id = get_jwt_identity()
        study = study_service.create_study(
            data['name'],
            data['description'],
            data['schedule'],
            data['week_count'],
            user_id
        )
        return jsonify(study.to_dict())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/studies', methods=['GET'])
def get_studies():
    try:
        studies = study_service.get_all_studies()
        return jsonify([study.to_dict() for study in studies])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/studies/<int:study_id>', methods=['GET'])
def get_study(study_id):
    try:
        study = study_service.get_study_by_id(study_id)
        return jsonify(study.to_dict())
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/studies/<int:study_id>', methods=['PUT'])
@jwt_required()
def update_study(study_id):
    try:
        data = request.get_json()
        user_id = get_jwt_identity()
        study = study_service.get_study_by_id(study_id)
        
        if study.leader_id != user_id:
            return jsonify({'error': '스터디장만 수정할 수 있습니다.'}), 403

        study_service.update_study(
            study_id,
            data['name'],
            data['description'],
            data['schedule'],
            data['week_count']
        )
        return jsonify({'message': '스터디 정보가 수정되었습니다.'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/studies/<int:study_id>', methods=['DELETE'])
@jwt_required()
def delete_study(study_id):
    try:
        user_id = get_jwt_identity()
        study = study_service.get_study_by_id(study_id)
        
        if study.leader_id != user_id:
            return jsonify({'error': '스터디장만 삭제할 수 있습니다.'}), 403

        study_service.delete_study(study_id)
        return jsonify({'message': '스터디가 삭제되었습니다.'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/studies/<int:study_id>/join', methods=['POST'])
@jwt_required()
def join_study(study_id):
    try:
        user_id = get_jwt_identity()
        study_service.join_study(study_id, user_id)
        return jsonify({'message': '스터디에 참여했습니다.'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 출석 관련 엔드포인트
@app.route('/api/studies/<int:study_id>/start-attendance', methods=['POST'])
@jwt_required()
def start_attendance(study_id):
    try:
        user_id = get_jwt_identity()
        study = study_service.get_study_by_id(study_id)
        
        if study.leader_id != user_id:
            return jsonify({'error': '스터디장만 출석을 시작할 수 있습니다.'}), 403

        verification = attendance_service.start_attendance(study_id)
        return jsonify(verification.to_dict())
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/studies/<int:study_id>/verify-attendance', methods=['POST'])
@jwt_required()
def verify_attendance(study_id):
    try:
        data = request.get_json()
        user_id = get_jwt_identity()
        
        attendance_service.verify_attendance(study_id, user_id, data['code'])
        return jsonify({'message': '출석이 확인되었습니다.'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/studies/<int:study_id>/attendance', methods=['GET'])
@jwt_required()
def get_attendance(study_id):
    try:
        records = attendance_service.get_attendance_records(study_id)
        return jsonify([record.to_dict() for record in records])
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/studies/<int:study_id>/end-attendance', methods=['POST'])
@jwt_required()
def end_attendance(study_id):
    try:
        user_id = get_jwt_identity()
        study = study_service.get_study_by_id(study_id)
        
        if study.leader_id != user_id:
            return jsonify({'error': '스터디장만 출석을 종료할 수 있습니다.'}), 403

        attendance_service.end_attendance(study_id)
        return jsonify({'message': '출석 인증이 종료되었습니다.'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 