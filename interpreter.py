class Interpreter:
    def __init__(self, code):
        self.code = code
        self.variables = {}

    def interpret(self):
        for line in self.code.splitlines():
            line = line.strip()  # Удалить пробелы в начале и конце строки
            if line.startswith("console.say("):
                message = line[13:-2]  # Extract the message from the console.say() call
                self.process_message(message)
            elif line.startswith("console.input("):
                prompt = line[14:-2]  # Extract the prompt from the console.input() call
                self.process_input(prompt)
            elif "=" in line:  # Проверить, содержит ли строка знак равенства
                self.process_assignment(line)
            elif "math(" in line:  # Проверить, содержит ли строка функцию math
                self.process_math(line)

    def process_math(self, line):
        expression = line[5:-1].strip()  # Extract the expression from the math() call
        result = self.evaluate_expression(expression)
        print(result)

    def process_assignment(self, line):
        parts = line.split("=")
        var_name = parts[0].strip()
        var_value = parts[1].strip()
        self.variables[var_name] = var_value

    def process_message(self, message):
        for var_name, var_value in self.variables.items():
            message = message.replace(var_name, var_value)
        print(message)

    def process_input(self, prompt):
        prompt = prompt.strip('"')  # Remove quotes from the prompt
        user_input = input(prompt)
        self.variables["input"] = user_input

    def evaluate_expression(self, expression):
        if "==" in expression:
            parts = expression.split("==")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            if isinstance(arg1, str) and isinstance(arg2, str):
                return arg1 == arg2
            elif isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
                return arg1 == arg2
            else:
                raise ValueError("Cannot compare values of different types")
        elif "!=" in expression:
            parts = expression.split("!=")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            if isinstance(arg1, str) and isinstance(arg2, str):
                return arg1 != arg2
            elif isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
                return arg1 != arg2
            else:
                raise ValueError("Cannot compare values of different types")
        elif ">" in expression:
            parts = expression.split(">")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
                raise ValueError("Cannot compare non-numeric values")
            return arg1 > arg2
        elif "<" in expression:
            parts = expression.split("<")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
                raise ValueError("Cannot compare non-numeric values")
            return arg1 < arg2
        elif "+" in expression:
            parts = expression.split("+")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
                raise ValueError("Cannot add non-numeric values")
            return arg1 + arg2
        elif "-" in expression:
            parts = expression.split("-")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
                raise ValueError("Cannot subtract non-numeric values")
            return arg1 - arg2
        elif "*" in expression:
            parts = expression.split("*")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
                raise ValueError("Cannot multiply non-numeric values")
            return arg1 * arg2
        elif "/" in expression:
            parts = expression.split("/")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
                raise ValueError("Cannot divide non-numeric values")
            if arg2 == 0:
                return "Error: division by zero"
            return arg1 / arg2
        else:
            return self.get_value(expression)

    def get_value(self, value):
        if value in self.variables:
            return str(self.variables[value])
        else:
            try:
                return float(value)
            except ValueError:
                return value

__version__ = "0.1"

def run():
    command = input("")
    parts = command.split()
    if len(parts) == 2 and parts[0] == "nslash1":
        file_name = parts[1]
        try:
            with open(file_name, "r") as f :
                code = f.read()
            interpreter = Interpreter(code)
            interpreter.interpret()
        except FileNotFoundError:
            print("File not found!")
    elif len(parts) == 1 and parts[0] == "-v":
        print(f"N/Script {__version__}")

run()