from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from playsound import playsound
import random
import threading

# アラーム音を再生する関数
def play_alarm():
    playsound("alarm.mp3")

class AlarmApp(App):
    def build(self):
        # 質問と答えのリスト
        self.questions = [
            {"question": "What is the capital of France?", "answer": "paris"},
            {"question": "How do you say 'ありがとう' in English?", "answer": "thank you"},
            {"question": "Spell the word 'elephant'.", "answer": "elephant"},
        ]
        self.current_question = random.choice(self.questions)

        # レイアウト
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # 質問ラベル
        self.question_label = Label(
            text=f"Question: {self.current_question['question']}",
            font_size=24,
            size_hint=(1, 0.2),
        )
        self.layout.add_widget(self.question_label)

        # ユーザー入力
        self.answer_input = TextInput(
            hint_text="Type your answer here",
            multiline=False,
            font_size=20,
            size_hint=(1, 0.2),
        )
        self.layout.add_widget(self.answer_input)

        # ボタン
        self.submit_button = Button(
            text="Submit",
            font_size=20,
            size_hint=(1, 0.2),
            on_press=self.check_answer,
        )
        self.layout.add_widget(self.submit_button)

        # メッセージラベル
        self.message_label = Label(
            text="",
            font_size=20,
            size_hint=(1, 0.2),
        )
        self.layout.add_widget(self.message_label)

        # アラーム音再生（バックグラウンドスレッド）
        self.alarm_thread = threading.Thread(target=play_alarm)
        self.alarm_thread.start()

        return self.layout

    def check_answer(self, instance):
        user_answer = self.answer_input.text.strip().lower()
        if user_answer == self.current_question["answer"]:
            self.message_label.text = "Correct! Alarm stopped."
            # アラーム音を停止
            self.alarm_thread = None
        else:
            self.message_label.text = "Incorrect. Try again!"

# アプリ起動
if __name__ == "__main__":
    AlarmApp().run()
