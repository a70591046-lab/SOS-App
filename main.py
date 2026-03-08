from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from plyer import gps
from plyer import sms
from plyer import call
import webbrowser

KV = '''

BoxLayout:
    orientation:"vertical"

    BoxLayout:
        size_hint_y:.1
        padding:10

        Button:
            text:"☰"
            size_hint_x:.2
            on_press: app.open_menu()

        Label:
            text:"SOS APP"
            font_size:22

    ScreenManager:
        id:screen_manager

        Screen:
            name:"register"

            BoxLayout:
                orientation:"vertical"
                padding:20
                spacing:10

                Label:
                    text:"Registratsiya"

                TextInput:
                    id:name
                    hint_text:"Ismingiz"

                TextInput:
                    id:phone
                    text:"+998"

                Button:
                    text:"Saqlash"
                    on_press: app.save_user()

        Screen:
            name:"home"

            BoxLayout:
                orientation:"vertical"

                Widget:

                Button:
                    text:"SOS"
                    font_size:40
                    size_hint:.6,.3
                    pos_hint:{"center_x":.5}
                    on_press: app.start_sos()

                Widget:

                Label:
                    text:"by codex-coder"
                    size_hint_y:.1

        Screen:
            name:"profile"

            BoxLayout:
                orientation:"vertical"
                padding:20

                Label:
                    text:"Profil"

                TextInput:
                    id:pname
                    hint_text:"Ism"

                TextInput:
                    id:pnumber
                    hint_text:"+998..."

                Button:
                    text:"Raqam qo'shish"
                    on_press: app.add_number()

                Button:
                    text:"Saqlash"
                    on_press: app.save_profile()

        Screen:
            name:"about"

            BoxLayout:
                orientation:"vertical"
                padding:20

                Label:
                    text:"SOS APP"

                Label:
                    text:"Emergency yordam dasturi"

                Label:
                    text:"Telegram: @codex_coder"

                Label:
                    text:"Programist: @codex_coding"

                Label:
                    text:"by codex-coder"
'''

class SOSApp(App):

    numbers=[]
    location="Location unknown"

    def build(self):
        return Builder.load_string(KV)

    def open_menu(self):
        print("menu")

    def save_user(self):
        self.root.ids.screen_manager.current="home"

    def start_sos(self):
        self.get_location()
        Clock.schedule_once(self.send_sos,5)

    def get_location(self):
        try:
            gps.configure(on_location=self.update_location)
            gps.start()
        except:
            print("GPS ishlamadi")

    def update_location(self,**kwargs):
        lat=kwargs['lat']
        lon=kwargs['lon']
        self.location=f"https://maps.google.com/?q={lat},{lon}"

    def send_sos(self,dt):
        message=f"SOS! Mening joylashuvim: {self.location}"

        for num in self.numbers:
            try:
                sms.send(recipient=num,text=message)
            except:
                print("SMS yuborilmadi")

    def add_number(self):
        num=self.root.ids.pnumber.text
        self.numbers.append(num)
        print("Added:",num)

    def save_profile(self):
        self.root.ids.screen_manager.current="home"

SOSApp().run()
