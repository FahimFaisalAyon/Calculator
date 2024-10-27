from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
import math

# KV layout definition as a string
kv = '''
<MainWidget>:
    rows: 6
    display_text: ""

    Label:
        text: root.display_text
        font_size: 32
        size_hint_y: None
        height: 100

    GridLayout:
        cols: 4
        Button:
            text: "%"
            on_press: root.click(self.text)
        Button:
            text: "^"
            on_press: root.click(self.text)
        Button:
            text: "C"
            on_press: root.click(self.text)
        Button:
            text: "/"
            on_press: root.click(self.text)

    GridLayout:
        cols: 4
        Button:
            text: "7"
            on_press: root.click(self.text)
        Button:
            text: "8"
            on_press: root.click(self.text)
        Button:
            text: "9"
            on_press: root.click(self.text)
        Button:
            text: "x"
            on_press: root.click(self.text)

    GridLayout:
        cols: 4
        Button:
            text: "4"
            on_press: root.click(self.text)
        Button:
            text: "5"
            on_press: root.click(self.text)
        Button:
            text: "6"
            on_press: root.click(self.text)
        Button:
            text: "-"
            on_press: root.click(self.text)

    GridLayout:
        cols: 4
        Button:
            text: "1"
            on_press: root.click(self.text)
        Button:
            text: "2"
            on_press: root.click(self.text)
        Button:
            text: "3"
            on_press: root.click(self.text)
        Button:
            text: "+"
            on_press: root.click(self.text)

    GridLayout:
        cols: 4
        Button:
            text: "√"
            on_press: root.click(self.text)
        Button:
            text: "0"
            on_press: root.click(self.text)
        Button:
            text: "."
            on_press: root.click(self.text)
        Button:
            text: "="
            on_press: root.click(self.text)
'''


class TheLabApp(App):
    def build(self):
        Builder.load_string(kv)  # Load the KV string
        return MainWidget()


class MainWidget(GridLayout):
    display_text = StringProperty("")

    def click(self, button_text):
        if button_text == "C":
            self.display_text = ""
        elif button_text == "=":
            # Handle the evaluation of the expression
            try:
                expression = self.display_text.replace('x', '*')  # Replace 'x' with '*' for multiplication
                if expression.startswith("√"):
                    value = float(expression[1:])
                    if value < 0:
                        self.display_text = "Error"
                    else:
                        y = math.sqrt(value)
                        self.display_text = str(y)
                else:
                    # Evaluate the expression
                    self.display_text = str(eval(expression))
            except Exception:
                self.display_text = "Error"
        elif button_text == "√":
            if not self.display_text:
                self.display_text += "√"
        else:
            self.display_text += button_text


if __name__ == '__main__':
    TheLabApp().run()
