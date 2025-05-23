이 프로젝트는 사용자로부터 일정을 입력받아 검증 후 저장하는 기능을 가진 간단한 콘솔 앱입니다.  
시퀀스 다이어그램과 샘플 코드를 기반으로 모듈 응집도 및 결합도 평가를 진행하였습니다.

- 언어: Python
- 주요 파일: `calendar_app.py`
- 구조: `User → CalendarApp → Storage`
- 실행 예시: 콘솔에서 `python calendar_app.py` 실행

응집도 평가

Storage: 일정 저장만 담당 → 높은 응집도

CalendarApp: 일정 검증과 저장 요청 → 높은 응집도

User: 사용자 입력 전달만 담당 → 높은 응집도

결합도 평가

User → CalendarApp: 메서드 호출만으로 동작 → 낮은 결합도

CalendarApp → Storage: 구체적인 내부 동작을 알 필요 없이 사용할 수 있음 → 낮은 결합도
