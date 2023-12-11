from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SalaryApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.label_salary = Label(text="Digite seu salário:")
        self.input_salary = TextInput(multiline=False, input_type='number')

        self.label_increase = Label(text="Digite o aumento (%):")
        self.input_increase = TextInput(multiline=False, input_type='number')

        self.result_label = Label(text="O valor atual do seu salário é: ")

        self.calculate_button = Button(text="Calcular", on_press=self.calculate_salary)

        self.layout.add_widget(self.label_salary)
        self.layout.add_widget(self.input_salary)
        self.layout.add_widget(self.label_increase)
        self.layout.add_widget(self.input_increase)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.calculate_button)

        return self.layout

    def calculate_salary(self, instance):
        try:
            salary = float(self.input_salary.text)
            increase_percentage = float(self.input_increase.text)
            increase_amount = (increase_percentage / 100) * salary
            new_salary = salary + increase_amount
            self.result_label.text = f"O valor atual do seu salário é: {new_salary:.2f}"
        except ValueError:
            self.result_label.text = "Por favor, insira valores válidos."

if __name__ == '__main__':
    SalaryApp().run()
