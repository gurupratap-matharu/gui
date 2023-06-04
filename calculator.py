from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    """Our main calculator app"""

    operators = ("/", "*", "+", "-")
    buttons = (
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("C", "0", ".", "+"),
    )
    pos_hint = {"center_x": 0.5, "center_y": 0.5}

    def build(self):
        self.last_command = None
        self.last_was_operator = None

        layout = BoxLayout(orientation="vertical")

        self.solution = TextInput(
            text="0", readonly=True, halign="right", font_size=125, multiline=False
        )
        layout.add_widget(self.solution)

        for row in self.buttons:
            h_layout = BoxLayout()

            for label in row:
                button = Button(text=label, pos_hint=self.pos_hint)
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)

            layout.add_widget(h_layout)

        equals_button = Button(text="=", pos_hint=self.pos_hint)
        equals_button.bind(on_press=self.on_solution_press)

        layout.add_widget(equals_button)

        return layout

    def on_button_press(self, instance):
        command = instance.text
        current_solution = self.solution.text
        is_operator = command in self.operators

        if command == "C":
            self.solution.text = "0"

        else:
            if self.last_was_operator and is_operator:
                # don't add two operators
                return
            else:
                if self.solution.text == "0":
                    self.solution.text = command
                else:
                    self.solution.text += command

        self.last_command = command
        self.last_was_operator = is_operator

    def on_solution_press(self, instance):
        """
        Calculate the results of an operation on a calculator.
        Typically triggered with the `=` symbol.
        """

        text = self.solution.text

        if text:
            print(f"evaluating {text}...")
            solution = str(eval(text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()
