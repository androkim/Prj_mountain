# main.py
# -*- coding: utf-8 -*-
import os

# KivyMD 앱 및 UI 관련 임포트
# from kivy.lang import Builder # .kv 파일을 사용하지 않으므로 주석 처리
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.clock import Clock
# from kivymd.uix.dialog import MDDialog # 현재 사용하지 않으므로 주석 처리
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
# from kivy.metrics import dp # 현재 사용하지 않으므로 주석 처리
# Kivy의 EventDispatcher를 사용하여 화면 간 신호 전달 (현재는 주석 처리)
# from kivy.event import EventDispatcher
# from kivy.properties import NumericProperty, StringProperty

# --- [수정] 모든 화면 임포트 주석 처리 ---
# from screens.main_screen import MainScreen
# from screens.announce_main_screen import AnnounceMainScreen
# from screens.settings_main_screen import SettingsMainScreen
# from screens.compass_screen import CompassScreen
# from screens.information_main_screen import InformationMainScreen
# from screens.mypage_main_screen import MyPageMainScreen
# from screens.tracking_main_screen import TrackingMainScreen
# from screens.settings_main_screen import SettingsMainScreen
# from screens.mountain_sub_tracking_screen import MountainSubTrackingScreen
# from screens.olle_sub_tracking_screen import OlleSubTrackingScreen
# from screens.mountain_info_screen import MountainInfoScreen
# from screens.olle_info_screen import OlleInfoScreen
# from screens.mountain_data_update_screen import MountainDataUpdateScreen
# from screens.olle_data_update_screen import OlleDataUpdateScreen
# ----------------------------------------------------

# 앱 화면 크기 설정 (유지)
Window.size = (360, 640)

# --- 한글 폰트 등록 (유지하되, 파일 존재 여부 더 명확히 확인) ---
# 프로젝트 루트에 'fonts' 폴더를 만들고 'NotoSansKR-Regular.ttf'를 넣어주세요.
font_name = "NotoSansKR"
font_filename = "NotoSansKR-Regular.ttf"
font_dir = os.path.join(os.path.dirname(__file__), 'fonts')
font_path = os.path.join(font_dir, font_filename)

if not os.path.exists(font_dir):
    os.makedirs(font_dir, exist_ok=True) # fonts 폴더가 없으면 생성

if os.path.exists(font_path):
    LabelBase.register(name=font_name, fn_regular=font_path)
    LabelBase.register(DEFAULT_FONT, font_path) # Kivy의 기본 폰트도 NotoSansKR로 지정
    print(f"DEBUG: Korean font registered as {font_name} and DEFAULT_FONT: {font_path}")
else:
    print(f"WARNING: Korean font '{font_filename}' not found at {font_path}. Fallback to default Kivy font.")
    print("WARNING: Please ensure the font file is in the 'fonts' folder next to main.py.")
# --------------------

# --- [추가] ApiUpdateProgress 클래스와 관련 로직은 현재 사용하지 않으므로 주석 처리 ---
# class ApiUpdateProgress(EventDispatcher):
#     progress_value = NumericProperty(0)
#     progress_text = StringProperty("준비 중...")
#     is_running = NumericProperty(0)
#     total_items_to_fetch = NumericProperty(0)
#     current_items_fetched = NumericProperty(0)
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.register_event_type('on_progress_update')
#     def on_progress_update(self, *args):
#         pass
# -------------------------------------------------------------------

class ChungAhmMountainApp(MDApp):
    # API 키 및 URL 관련 속성은 현재 사용하지 않으므로 주석 처리
    # FOREST_API_KEY = "76586aad2943c239fec03cf5a33319ec3005db010e91f6902772cd854d1a1c3a"
    # MOUNTAIN_INFO_API_URL = "https://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoOpenAPI2"
    # API_PAGE_SIZE = 100
    # announcements_data = []
    # toast_dialog = None
    # api_update_progress = ApiUpdateProgress() # <--- ApiUpdateProgress 인스턴스 생성

    def build(self):
        self.title = "걷고 오르고"
        print("DEBUG: Minimal KivyMD app building.")
        
        # `chungahmalpine.kv` 파일이나 `ScreenManager` 없이, 간단한 MDBoxLayout 반환
        layout = MDBoxLayout(orientation='vertical', spacing=10, padding=30)
        layout.add_widget(MDLabel(
            text="[b]걷고 오르고[/b]", 
            halign="center", 
            font_style="H4", 
            font_name=DEFAULT_FONT,
            markup=True
        ))
        layout.add_widget(MDLabel(
            text="새로운 시작을 환영합니다!", 
            halign="center", 
            font_style="Body1", 
            font_name=DEFAULT_FONT
        ))
        layout.add_widget(MDLabel(
            text="로컬 앱 실행 확인 완료. 이제 APK 빌드를 준비해봅시다.", 
            halign="center", 
            font_style="Caption", 
            font_name=DEFAULT_FONT
        ))
        print("DEBUG: Minimal MDBoxLayout returned as root widget.")
        return layout

    # on_start 및 기타 메서드들은 현재 사용하지 않으므로 주석 처리
    def on_start(self):
        Clock.schedule_once(self._post_build_init, 0)
        # API 업데이트 진행 상황 이벤트 리스너 등록 (ApiUpdateProgress 주석 처리로 인해 주석 처리)
        # self.api_update_progress.bind(
        #     progress_value=self._update_progress_ui,
        #     progress_text=self._update_progress_ui,
        #     is_running=self._update_progress_ui,
        #     total_items_to_fetch=self._update_progress_ui,
        #     current_items_fetched=self._update_items_fetched
        # )

    def _post_build_init(self, dt):
        """앱의 모든 UI 요소가 빌드된 후 실행될 초기화 작업 (현재 내용 없음)"""
        print("DEBUG: _post_build_init called. No complex initialization needed yet.")
        # self.load_announcements_from_file()

    # 토스트 메시지 관련 메서드들은 현재 사용하지 않으므로 주석 처리
    # def show_toast(self, text, duration=2):
    #     if self.toast_dialog:
    #         self.toast_dialog.dismiss()
    #         self.toast_dialog = None
    #     toast_content = MDBoxLayout(
    #         orientation='vertical',
    #         size_hint_y=None,
    #         height=dp(48)
    #     )
    #     toast_content.add_widget(
    #         MDLabel(
    #             text=text,
    #             halign="center",
    #             font_name=DEFAULT_FONT,
    #             markup=True,
    #             theme_text_color="Custom",
    #             text_color=(1, 1, 1, 1)
    #         )
    #     )
    #     self.toast_dialog = MDDialog(
    #         type="custom",
    #         content_cls=toast_content,
    #         auto_dismiss=False,
    #         md_bg_color=(0.2, 0.2, 0.2, 0.8),
    #     )
    #     self.toast_dialog.open()
    #     Clock.schedule_once(lambda *args: self.dismiss_toast(), duration)
    # def dismiss_toast(self):
    #     if self.toast_dialog:
    #         self.toast_dialog.dismiss()
    #         self.toast_dialog = None

    # 데이터 저장/로드 관련 메서드들은 현재 사용하지 않으므로 주석 처리
    # def _get_data_dir_path(self):
    #     data_dir = os.path.join(os.path.dirname(__file__), 'data')
    #     os.makedirs(data_dir, exist_ok=True)
    #     return data_dir
    # def _get_announcements_file_path(self):
    #     return os.path.join(self._get_data_dir_path(), 'announcements.json')
    # def _get_mountain_data_file_path(self):
    #     return os.path.join(self._get_data_dir_path(), 'mountain_data.json')
    # def load_announcements_from_file(self):
    #     file_path = self._get_announcements_file_path()
    #     print(f"DEBUG: Attempting to load announcements from: {file_path}")
    #     if os.path.exists(file_path):
    #         with open(file_path, 'r', encoding='utf-8') as f:
    #             try:
    #                 self.announcements_data = json.load(f)
    #                 print(f"DEBUG: Successfully loaded {len(self.announcements_data)} announcements.")
    #             except json.JSONDecodeError as e:
    #                 print(f"ERROR: announcements.json decoding failed: {e}. Initializing with empty list.")
    #                 self.announcements_data = []
    #                 self.show_toast("공지사항 파일 손상! 새로 생성됩니다.", duration=3)
    #     else:
    #         print("DEBUG: announcements.json not found. Initializing with empty list.")
    #         self.announcements_data = []
    #         self.save_announcements_to_file()
    #         self.show_toast("공지사항 파일이 없어 새로 생성되었습니다.", duration=3)
    # def save_announcements_to_file(self):
    #     file_path = self._get_announcements_file_path()
    #     print(f"DEBUG: Saving {len(self.announcements_data)} announcements to: {file_path}")
    #     try:
    #         with open(file_path, 'w', encoding='utf-8') as f:
    #             json.dump(self.announcements_data, f, ensure_ascii=False, indent=4)
    #         print("DEBUG: Announcements saved successfully.")
    #     except Exception as e:
    #         print(f"ERROR: Failed to save announcements to file: {e}")
    #         self.show_toast("공지사항 저장 실패!", duration=3)
    # def save_json_data(self, file_path, data):
    #     print(f"DEBUG: Saving data to: {file_path}")
    #     try:
    #         with open(file_path, 'w', encoding='utf-8') as f:
    #             json.dump(data, f, ensure_ascii=False, indent=4)
    #         print(f"DEBUG: Data saved successfully to {file_path}")
    #         return True
    #     except Exception as e:
    #         print(f"ERROR: Failed to save data to {file_path}: {e}")
    #         return False

    # API 업데이트 진행 상황 UI 업데이트 메서드도 현재 사용하지 않으므로 주석 처리
    # def _update_progress_ui(self, instance, value):
    #     settings_screen = self.root.get_screen('settings_main')
    #     if settings_screen:
    #         if self.api_update_progress.is_running == 1:
    #             total = self.api_update_progress.total_items_to_fetch
    #             current = self.api_update_progress.current_items_fetched
    #             progress = (current / total) * 100 if total > 0 else 0
    #             if settings_screen.ids.get('update_progress_bar'):
    #                 settings_screen.ids.update_progress_bar.value = progress
    #             if settings_screen.ids.get('update_status_label'):
    #                 settings_screen.ids.update_status_label.text = \
    #                     f"산 정보 업데이트 중... {current}/{total}개 ({int(progress)}%)"
    #         elif self.api_update_progress.is_running == 2:
    #             if settings_screen.ids.get('update_progress_bar'):
    #                 settings_screen.ids.update_progress_bar.value = 100
    #             if settings_screen.ids.get('update_status_label'):
    #                 settings_screen.ids.update_status_label.text = "업데이트 완료!"
    #         elif self.api_update_progress.is_running == -1:
    #             if settings_screen.ids.get('update_status_label'):
    #                 settings_screen.ids.update_status_label.text = "업데이트 실패!"
    #         else:
    #             if settings_screen.ids.get('update_progress_bar'):
    #                 settings_screen.ids.update_progress_bar.value = 0
    #             if settings_screen.ids.get('update_status_label'):
    #                 settings_screen.ids.update_status_label.text = "준비 중..."

# --------------------------------------------------------------------------------------
if __name__ == "__main__":
    ChungAhmMountainApp().run()