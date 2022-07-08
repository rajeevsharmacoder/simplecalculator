import math
from kivy import utils
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'width', '420')
Config.set('graphics', 'height', '720')
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.graphics.vertex_instructions import RoundedRectangle


class CalculatorLayout(BoxLayout):

    value1 = None
    value2 = None
    operation = None
    operation_moved = False
    result = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, v1, v2, op):
        try:
            if op == '+':
                return round(v1 + v2, 9)
            elif op == '-':
                return round(v1 - v2, 9)
            elif op == 'X':
                return round(v1 * v2, 9)
            elif op == '/':
                if v2 == 0:
                    return "Division By Zero Error"
                return round(v1 / v2, 9)
            else:
                return "Invalid Operation"
        except:
            return "Error"

    def interim_evaluate(self, main_output_label):
        try:
            if self.value1 is not None and self.operation is not None:
                self.value2 = float(main_output_label.text)
                self.result = self.clean_result(self.evaluate(self.value1, self.value2, self.operation))
                main_output_label.text = self.result
                try:
                    self.value1 = float(main_output_label.text)
                except:
                    self.value1 = None
            self.value2 = None
            self.operation = None
            self.result = None
            self.operation_moved = False
        except:
            print("Line 53")
            main_output_label.text = "Error"

    def clean_result(self, value):
        try:
            if '.' in str(value):
                decimal_part = str(value).split('.')[1]
                if float(decimal_part) == 0:
                    return str(int(value))
            return str(value)
        except:
            return "Error"

    def on_c_ac_press(self, c_ac_button, main_output_label):
        with c_ac_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#97550A')))
            RoundedRectangle(size=c_ac_button.size, pos=c_ac_button.pos, radius=[20])
        try:
            main_output_label.text = ""
            self.value1 = None
            self.value2 = None
            self.operation = None
            self.operation_moved = False
            self.result = None
        except:
            main_output_label.text = "Error"

    def on_c_ac_release(self, c_ac_button, main_output_label):
        with c_ac_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#B9770E')))
            RoundedRectangle(size=c_ac_button.size, pos=c_ac_button.pos, radius=[20])

    def on_plus_minus_press(self, plus_minus_button, main_output_label):
        with plus_minus_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#700900')))
            RoundedRectangle(size=plus_minus_button.size, pos=plus_minus_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if '-' not in main_output_label.text:
                    main_output_label.text = "-" + main_output_label.text
                else:
                    main_output_label.text = main_output_label.text[1:]
        except:
            main_output_label.text = "Error"

    def on_plus_minus_release(self, plus_minus_button, main_output_label):
        with plus_minus_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#922B21')))
            RoundedRectangle(size=plus_minus_button.size, pos=plus_minus_button.pos, radius=[20])

    def on_square_root_press(self, square_root_button, main_output_label):
        with square_root_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#0C406B')))
            RoundedRectangle(size=square_root_button.size, pos=square_root_button.pos, radius=[20])
        try:
            if main_output_label.text != "" and main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                self.interim_evaluate(main_output_label)
                value = self.clean_result(math.sqrt(float(main_output_label.text)))
                main_output_label.text = value
        except:
            main_output_label.text = "Error"

    def on_square_root_release(self, square_root_button, main_output_label):
        with square_root_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#1F618D')))
            RoundedRectangle(size=square_root_button.size, pos=square_root_button.pos, radius=[20])

    def on_percentage_press(self, percentage_button, main_output_label):
        with percentage_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#0C406B')))
            RoundedRectangle(size=percentage_button.size, pos=percentage_button.pos, radius=[20])
        try:
            if main_output_label.text != "" and main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                self.interim_evaluate(main_output_label)
                value = self.clean_result(str(float(main_output_label.text)/100))
                main_output_label.text = value
                self.value1 = None
                self.value2 = None
                self.operation = None
                self.operation_moved = False
                self.result = None
        except:
            main_output_label.text = "Error"

    def on_percentage_release(self, percentage_button, main_output_label):
        with percentage_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#1F618D')))
            RoundedRectangle(size=percentage_button.size, pos=percentage_button.pos, radius=[20])

    def on_seven_press(self, seven_button, main_output_label):
        with seven_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#280138')))
            RoundedRectangle(size=seven_button.size, pos=seven_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text = "7"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "7"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "7"
        except:
            main_output_label.text = "Error"

    def on_seven_release(self, seven_button, main_output_label):
        with seven_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=seven_button.size, pos=seven_button.pos, radius=[20])

    def on_eight_press(self, eight_button, main_output_label):
        with eight_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#280138')))
            RoundedRectangle(size=eight_button.size, pos=eight_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text = "8"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "8"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "8"
        except:
            main_output_label.text = "Error"

    def on_eight_release(self, eight_button, main_output_label):
        with eight_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=eight_button.size, pos=eight_button.pos, radius=[20])

    def on_nine_press(self, nine_button, main_output_label):
        with nine_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#280138')))
            RoundedRectangle(size=nine_button.size, pos=nine_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text = "9"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "9"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "9"
        except:
            main_output_label.text = "Error"

    def on_nine_release(self, nine_button, main_output_label):
        with nine_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=nine_button.size, pos=nine_button.pos, radius=[20])

    def on_divide_press(self, divide_button, main_output_label):
        with divide_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#0C6499')))
            RoundedRectangle(size=divide_button.size, pos=divide_button.pos, radius=[20])
        try:
            if main_output_label.text != "" and main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                self.interim_evaluate(main_output_label)
                self.value1 = float(main_output_label.text)
                self.operation = '/'
        except:
            main_output_label.text = "Error"

    def on_divide_release(self, divide_button, main_output_label):
        with divide_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#2E86C1')))
            RoundedRectangle(size=divide_button.size, pos=divide_button.pos, radius=[20])

    def on_four_press(self, four_button, main_output_label):
        with four_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#280138')))
            RoundedRectangle(size=four_button.size, pos=four_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text = "4"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "4"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "4"
        except:
            main_output_label.text = "Error"

    def on_four_release(self, four_button, main_output_label):
        with four_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=four_button.size, pos=four_button.pos, radius=[20])

    def on_five_press(self, five_button, main_output_label):
        with five_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#280138')))
            RoundedRectangle(size=five_button.size, pos=five_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text = "5"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "5"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "5"
        except:
            main_output_label.text = "Error"

    def on_five_release(self, five_button, main_output_label):
        with five_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=five_button.size, pos=five_button.pos, radius=[20])

    def on_six_press(self, six_button, main_output_label):
        with six_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#280138')))
            RoundedRectangle(size=six_button.size, pos=six_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text = "6"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "6"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "6"
        except:
            main_output_label.text = "Error"

    def on_six_release(self, six_button, main_output_label):
        with six_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=six_button.size, pos=six_button.pos, radius=[20])

    def on_multiply_press(self, multiply_button, main_output_label):
        with multiply_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#0C6499')))
            RoundedRectangle(size=multiply_button.size, pos=multiply_button.pos, radius=[20])
        try:
            if main_output_label.text != "" and main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                self.interim_evaluate(main_output_label)
                self.value1 = float(main_output_label.text)
                self.operation = 'X'
        except:
            main_output_label.text = "Error"

    def on_multiply_release(self, multiply_button, main_output_label):
        with multiply_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#2E86C1')))
            RoundedRectangle(size=multiply_button.size, pos=multiply_button.pos, radius=[20])

    def on_one_press(self, one_button, main_output_label):
        with one_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#280138')))
            RoundedRectangle(size=one_button.size, pos=one_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text = "1"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "1"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "1"
        except:
            main_output_label.text = "Error"

    def on_one_release(self, one_button, main_output_label):
        with one_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=one_button.size, pos=one_button.pos, radius=[20])

    def on_two_press(self, two_button, main_output_label):
        with two_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#230138')))
            RoundedRectangle(size=two_button.size, pos=two_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text = "2"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "2"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "2"
        except:
            main_output_label.text = "Error"

    def on_two_release(self, two_button, main_output_label):
        with two_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=two_button.size, pos=two_button.pos, radius=[20])

    def on_three_press(self, three_button, main_output_label):
        with three_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#280138')))
            RoundedRectangle(size=three_button.size, pos=three_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text = "3"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "3"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "3"
        except:
            main_output_label.text = "Error"

    def on_three_release(self, three_button, main_output_label):
        with three_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=three_button.size, pos=three_button.pos, radius=[20])

    def on_minus_press(self, minus_button, main_output_label):
        with minus_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#0C6499')))
            RoundedRectangle(size=minus_button.size, pos=minus_button.pos, radius=[20])
        try:
            if main_output_label.text != "" and main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                self.interim_evaluate(main_output_label)
                self.value1 = float(main_output_label.text)
                self.operation = '-'
        except:
            main_output_label.text = "Error"

    def on_minus_release(self, minus_button, main_output_label):
        with minus_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#2E86C1')))
            RoundedRectangle(size=minus_button.size, pos=minus_button.pos, radius=[20])

    def on_zero_press(self, zero_button, main_output_label):
        with zero_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#280138')))
            RoundedRectangle(size=zero_button.size, pos=zero_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if main_output_label.text == "0":
                    main_output_label.text == "0"
                elif not self.operation_moved and self.operation is not None:
                    main_output_label.text = "0"
                    self.operation_moved = True
                else:
                    main_output_label.text = main_output_label.text + "0"
        except:
            main_output_label.text = "Error"

    def on_zero_release(self, zero_button, main_output_label):
        with zero_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#4A235A')))
            RoundedRectangle(size=zero_button.size, pos=zero_button.pos, radius=[20])

    def on_decimal_press(self, decimal_button, main_output_label):
        with decimal_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#5A1827')))
            RoundedRectangle(size=decimal_button.size, pos=decimal_button.pos, radius=[20])
        try:
            if main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                if '.' not in main_output_label.text:
                    if main_output_label != "":
                        main_output_label.text = main_output_label.text + "."
                    else:
                        main_output_label.text = "0."
                elif '.' in main_output_label.text and self.operation is not None and self.value1 is not None:
                    main_output_label.text = "0."
                    self.operation_moved = True

        except:
            main_output_label.text = "Error"

    def on_decimal_release(self, decimal_button, main_output_label):
        with decimal_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#7C4049')))
            RoundedRectangle(size=decimal_button.size, pos=decimal_button.pos, radius=[20])

    def on_equal_press(self, equal_button, main_output_label):
        with equal_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#23917B')))
            RoundedRectangle(size=equal_button.size, pos=equal_button.pos, radius=[20])
        try:
            if main_output_label.text != "" and main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                self.value2 = float(main_output_label.text)
                if (self.value1 is not None and self.value2 is not None and self.operation is not None):
                    main_output_label.text = self.clean_result(self.evaluate(self.value1, self.value2, self.operation))
                    try:
                        self.value1 = float(main_output_label.text)
                    except:
                        self.value1 = None
                    self.value2 = None
                    self.operation = None
                    self.operation_moved = False
                    self.result = None
                else:
                    main_output_label.text = main_output_label.text
        except:
            main_output_label.text = "Error"

    def on_equal_release(self, equal_button, main_output_label):
        with equal_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#45B39D')))
            RoundedRectangle(size=equal_button.size, pos=equal_button.pos, radius=[20])

    def on_plus_press(self, plus_button, main_output_label):
        with plus_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#0C6499')))
            RoundedRectangle(size=plus_button.size, pos=plus_button.pos, radius=[20])
        try:
            if main_output_label.text != "" and main_output_label.text != "Division By Zero Error" and main_output_label.text != "Invalid Operation" and main_output_label.text != "Error":
                self.interim_evaluate(main_output_label)
                self.value1 = float(main_output_label.text)
                self.operation = '+'
        except:
            main_output_label.text = "Error"

    def on_plus_release(self, plus_button, main_output_label):
        with plus_button.canvas.before:
            Color(rgba=(utils.get_color_from_hex('#2E86C1')))
            RoundedRectangle(size=plus_button.size, pos=plus_button.pos, radius=[20])


class CalculatorApp(App):
    pass


CalculatorApp().run()
