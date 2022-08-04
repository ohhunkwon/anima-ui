from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_file("styles.kv")

    def process(self):
        text = self.root.ids.input.text
        print(text)


if __name__ == '__main__':
    MainApp().run()