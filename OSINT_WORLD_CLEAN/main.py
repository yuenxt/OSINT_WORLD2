__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.06, 0.08, 1)


def button(text, callback):
    b = Button(text=text, size_hint_y=None, height=52)
    b.bind(on_release=callback)
    return b


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", padding=20, spacing=12)
        box.add_widget(Label(text="[b]OSINT WORLD[/b]", markup=True, font_size=30, size_hint_y=None, height=70))
        box.add_widget(Label(text="Фиктивная игровая OSINT-платформа", font_size=16, size_hint_y=None, height=40))
        box.add_widget(button("Профиль", lambda *_: self.manager.current = "profile"))
        box.add_widget(button("Задания", lambda *_: self.manager.current = "tasks"))
        box.add_widget(button("Чат", lambda *_: self.manager.current = "chat"))
        box.add_widget(button("Маркет", lambda *_: self.manager.current = "market"))
        box.add_widget(button("Инфо-терминал", lambda *_: self.manager.current = "terminal"))
        box.add_widget(button("Выйти", lambda *_: self.manager.current = "login"))
        self.add_widget(box)


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", padding=25, spacing=12)
        box.add_widget(Label(text="[b]OSINT WORLD[/b]", markup=True, font_size=32, size_hint_y=None, height=70))
        self.name = TextInput(hint_text="Имя игрока", multiline=False, size_hint_y=None, height=50)
        box.add_widget(self.name)
        box.add_widget(button("Войти", self.login))
        box.add_widget(Label(text="Это игровая симуляция. Реальные аккаунты и реальные данные не используются."))
        self.add_widget(box)

    def login(self, *_):
        name = self.name.text.strip() or "Игрок"
        self.manager.get_screen("profile").player_name = name
        self.manager.current = "home"


class ProfileScreen(Screen):
    player_name = "Игрок"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=12)
        self.title = Label(text="", font_size=26, size_hint_y=None, height=60)
        self.layout.add_widget(self.title)
        self.layout.add_widget(Label(text="Уровень: 1\nРепутация: 0\nБаланс: 1000 CR"))
        self.layout.add_widget(button("Назад", lambda *_: setattr(self.manager, "current", "home")))
        self.add_widget(self.layout)

    def on_pre_enter(self, *args):
        self.title.text = f"[b]{self.player_name}[/b]",


class TasksScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", padding=20, spacing=10)
        box.add_widget(Label(text="[b]Задания[/b]", markup=True, font_size=26, size_hint_y=None, height=60))
        for text in [
            "1. Найди связь между двумя вымышленными профилями",
            "2. Проверь игровой цифровой след",
            "3. Расшифруй подсказку терминала",
        ]:
            box.add_widget(Label(text=text, size_hint_y=None, height=55))
        box.add_widget(button("Назад", lambda *_: setattr(self.manager, "current", "home")))
        self.add_widget(box)


class ChatScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", padding=15, spacing=10)
        self.messages = Label(text="Система: Добро пожаловать в игровой чат.\n", halign="left", valign="top")
        self.messages.bind(size=self.messages.setter("text_size"))
        scroll = ScrollView()
        scroll.add_widget(self.messages)
        box.add_widget(scroll)
        row = BoxLayout(size_hint_y=None, height=52, spacing=8)
        self.input = TextInput(hint_text="Сообщение", multiline=False)
        row.add_widget(self.input)
        row.add_widget(button("Отправить", self.send))
        box.add_widget(row)
        box.add_widget(button("Назад", lambda *_: setattr(self.manager, "current", "home")))
        self.add_widget(box)

    def send(self, *_):
        text = self.input.text.strip()
        if text:
            self.messages.text += f"Вы: {text}\n"
            self.input.text = ""


class MarketScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", padding=20, spacing=10)
        box.add_widget(Label(text="[b]Маркет[/b]", markup=True, font_size=26, size_hint_y=None, height=60))
        for item in ["Анонимный VPN — 250 CR", "Премиум-терминал — 500 CR", "Набор аналитика — 300 CR"]:
            box.add_widget(button(item, lambda *_: None))
        box.add_widget(button("Назад", lambda *_: setattr(self.manager, "current", "home")))
        self.add_widget(box)


class TerminalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = BoxLayout(orientation="vertical", padding=20, spacing=10)
        box.add_widget(Label(text="[b]Игровой инфо-терминал[/b]", markup=True, font_size=24, size_hint_y=None, height=60))
        self.query = TextInput(hint_text="Введите игровой запрос", multiline=False, size_hint_y=None, height=50)
        box.add_widget(self.query)
        self.result = Label(text="Результат появится здесь.")
        box.add_widget(self.result)
        box.add_widget(button("Проверить", self.check))
        box.add_widget(button("Назад", lambda *_: setattr(self.manager, "current", "home")))
        self.add_widget(box)

    def check(self, *_):
        q = self.query.text.strip()
        if q:
            self.result.text = f"Игровой результат для «{q}»:\nСовпадений не найдено."
        else:
            self.result.text = "Введите запрос."


class OSINTWorldApp(App):
    title = "OSINT WORLD"

    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ProfileScreen(name="profile"))
        sm.add_widget(TasksScreen(name="tasks"))
        sm.add_widget(ChatScreen(name="chat"))
        sm.add_widget(MarketScreen(name="market"))
        sm.add_widget(TerminalScreen(name="terminal"))
        return sm


if __name__ == "__main__":
    OSINTWorldApp().run()
