from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

Fname = None
Email = None
Pword = None

KV = """
ScreenManager:
    LandingPageScreen:
    LoginScreen:
    SignupScreen:
    HomeScreen:

<LandingPageScreen>:
    name: 'landing_page'
    MDBoxLayout:
        orientation: 'vertical'
        padding: [0, 0, 0, dp(60)]
        MDTopAppBar:
            title: 'Welcome to Jollibee'
            md_bg_color: 1, 0, 0, 1
            specific_text_color: 1, 1, 1, 1

        Widget:

        Image:
            source: 'jollibee.png'
            size_hint: None, None
            size: dp(200), dp(150)
            pos_hint: {"center_x": 0.5}

        MDLabel:
            text: 'Sign up today to get access to exclusive deals, faster ordering, and more!'
            halign: 'center'
            theme_text_color: 'Secondary'
            size_hint_y: None
            height: dp(60)
            padding: dp(20)

        MDFillRoundFlatButton:
            text: 'SIGN UP WITH EMAIL'
            md_bg_color: 1, 0, 0, 1
            text_color: 1, 1, 1, 1
            size_hint_x: 0.8
            pos_hint: {'center_x': 0.5}
            on_release: app.go_to_signup()

        MDLabel:
            text: 'OR'
            halign: 'center'
            theme_text_color: 'Secondary'
            size_hint_y: None
            height: dp(30)

        MDFillRoundFlatButton:
            text: 'CONTINUE WITH FACEBOOK'
            md_bg_color: 0, 0, 1, 1
            text_color: 1, 1, 1, 1
            size_hint_x: 0.8
            pos_hint: {'center_x': 0.5}

        MDLabel:
            text: 'Already have an account? [ref=login][color=ff0000]Log in[/color][/ref]'
            markup: True
            halign: 'center'
            markup: True
            theme_text_color: 'Primary'
            size_hint_y: None
            height: dp(30)
            on_ref_press: app.go_to_login()

<LoginScreen>:
    name: 'login'
    MDBoxLayout:
        orientation: 'vertical'
        padding: [0, 0, 0, dp(40)]
        MDTopAppBar:
            title: 'Welcome to Jollibee'
            md_bg_color: 1, 0, 0, 1
            specific_text_color: 1, 1, 1, 1
        Widget:
        Image:
            source: 'jollibee.png'
            size_hint: None, None
            size: dp(200), dp(150)
            pos_hint: {"center_x": 0.5}

        MDLabel:
            text: 'Login to Your Account'
            halign: 'center'
            theme_text_color: 'Primary'
            font_style: 'H5'

        MDTextField:
            id: email
            hint_text: 'Email'
            icon_right: 'email'
            size_hint_x: 0.9
            pos_hint: {'center_x': 0.5}

        MDTextField:
            id: password
            hint_text: 'Password'
            icon_right: 'eye-off'
            password: True
            size_hint_x: 0.9
            pos_hint: {'center_x': 0.5}

        MDFillRoundFlatButton:
            text: 'LOGIN'
            md_bg_color: 1, 0, 0, 1
            text_color: 1, 1, 1, 1
            size_hint_x: 0.9
            pos_hint: {'center_x': 0.5}
            on_release: app.login()

        MDLabel:
            text: "Don't have an account? [ref=landing_page][color=ff0000]Sign Up[/color][/ref]"
            markup: True  
            halign: 'center'
            markup: True
            theme_text_color: 'Secondary'
            size_hint_y: None
            height: dp(30)
            on_ref_press: app.go_to_landing_page()

            
<SignupScreen>:
    name: 'signup'
    MDBoxLayout:
        orientation: 'vertical'
        padding: [0, 0, 0, dp(40)]
        MDTopAppBar:
            title: 'Welcome to Jollibee'
            md_bg_color: 1, 0, 0, 1
            specific_text_color: 1, 1, 1, 1
        Widget:
        Image:
            source: 'jollibee.png'
            size_hint: None, None
            size: dp(200), dp(150)
            pos_hint: {"center_x": 0.5}

        MDLabel:
            text: 'Sign up Your Account'
            halign: 'center'
            theme_text_color: 'Primary'
            font_style: 'H5'

        MDTextField:
            id: fullname
            hint_text: 'Fullname'
            icon_right: 'account'
            size_hint_x: 0.9
            pos_hint: {'center_x': 0.5}

        MDTextField:
            id: email
            hint_text: 'Email'
            icon_right: 'email'
            size_hint_x: 0.9
            pos_hint: {'center_x': 0.5}

        MDTextField:
            id: password
            hint_text: 'Password'
            icon_right: 'eye-off'
            password: True
            size_hint_x: 0.9
            pos_hint: {'center_x': 0.5}

        MDFillRoundFlatButton:
            text: 'SIGN UP'
            md_bg_color: 1, 0, 0, 1
            text_color: 1, 1, 1, 1
            size_hint_x: 0.9
            pos_hint: {'center_x': 0.5}
            on_release: app.signup()

        MDLabel:
            text: "Already have an account? [ref=login][color=ff0000]Log in[/color][/ref]"
            markup: True  
            halign: 'center'
            markup: True
            theme_text_color: 'Secondary'
            size_hint_y: None
            height: dp(30)
            on_ref_press: app.go_to_login()

<HomeScreen>:
    name: 'home'
    MDBoxLayout:
        orientation: 'vertical'
        padding: [0, 0, 0, dp(40)]
        MDTopAppBar:
            orientation: 'horizontal'
            title: 'Jollibee'
            md_bg_color: 1, 0, 0, 1
            specific_text_color: 1, 1, 1, 1
            
        Widget:
        MDLabel:
            id: welcome_label
            text: "Welcome!"
            font_style: "H5"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
"""

class LandingPageScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

class JollibeeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(KV)

    def go_to_landing_page(self):
        self.root.current = 'landing_page'
        
    def go_to_login(self):
        self.root.current = 'login'
           
    def go_to_signup(self):
        self.root.current = 'signup'
        
    def signup(self):
        global Fname 
        global Email 
        global Pword 

        Fname = self.root.get_screen('signup').ids.fullname.text
        Email = self.root.get_screen('signup').ids.email.text
        Pword = self.root.get_screen('signup').ids.password.text

        self.root.current = 'login'
        
    def login(self):
        email = self.root.get_screen('login').ids.email.text
        password = self.root.get_screen('login').ids.password.text

        if email == Email and password == Pword:  # Missing colon added
            self.root.current = 'home'
            welcome_label = self.root.get_screen('home').ids.welcome_label
            welcome_label.text = f"Welcome, {Fname}!"  # Set the full name here
    
        else:
            self.show_login_failed_dialog()

    def show_login_failed_dialog(self):
        if not hasattr(self, 'dialog'):
            self.dialog = MDDialog(
                title="Login Failed",
                text="Invalid email or password.",
                buttons=[
                    MDFlatButton(
                        text="CLOSE",
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                ],
            )
        self.dialog.open()

if __name__ == "__main__":
    JollibeeApp().run()
