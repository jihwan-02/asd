class Storage:
    """일정을 저장하는 클래스 (DB 역할)"""
    def __init__(self):
        self.events = []

    def save_event(self, event: str):
        self.events.append(event)
        return True


class CalendarApp:
    """일정 검증 및 저장 처리"""
    def __init__(self, storage: Storage):
        self.storage = storage

    def is_valid_event(self, event: str) -> bool:
        # 유효성 검사: 공백 제거 후 길이 확인 + 날짜 포함 여부 간단 검사
        return bool(event.strip()) and any(char.isdigit() for char in event)

    def add_event(self, event: str):
        print("[CalendarApp] 일정 유효성 검사 중...")
        if self.is_valid_event(event):
            print("[CalendarApp] 유효한 일정입니다. 저장 요청 중...")
            success = self.storage.save_event(event)
            if success:
                print("[CalendarApp] ✅ 일정이 저장되었습니다.")
        else:
            print("[CalendarApp] ❌ 유효하지 않은 일정입니다. 다시 입력해주세요.")


class User:
    """일정을 입력하고 앱에 전달하는 사용자 역할"""
    def __init__(self, calendar_app: CalendarApp):
        self.calendar_app = calendar_app

    def create_event(self, event: str):
        print(f"[User] '{event}' 일정 추가 요청")
        self.calendar_app.add_event(event)


# 실행 예시
if __name__ == "__main__":
    storage = Storage()
    app = CalendarApp(storage)
    user = User(app)

    # 테스트: 유효한 일정
    user.create_event("2025-05-24 과제 제출하기")

    print("\n---\n")

    # 테스트: 유효하지 않은 일정
    user.create_event("     ")