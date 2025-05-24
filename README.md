이 시퀀스 다이어그램은 사용자가 캘린더 앱을 통해 일정을 추가하는 흐름을 시각화한 것입니다.  
일정 입력 → 입력값 검증 → 저장 요청 → 사용자에게 응답하는 전형적인 절차를 모델링했습니다.

- **User**: 일정을 입력하고 추가 요청을 보냅니다.  
- **CalendarApp**: 입력값을 검증하고 저장 요청을 처리합니다.  
- **Storage**: 실제 일정 데이터를 저장합니다.

유효한 입력일 경우 일정이 저장되고 완료 메시지를 사용자에게 반환하며,  
유효하지 않으면 오류 메시지가 출력됩니다.

![시퀸스 다이어그램](https://github.com/user-attachments/assets/fc90dc31-2dd9-4c46-80c8-88855acd0c07)

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
