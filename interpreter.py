class Interpreter:
    def __init__(self, code):
        self.code = code
        self.variables = {}

    def interpret(self):
        for line in self.code.splitlines():
            line = line.strip()
            if line.startswith("console.say("):
                message = line[13:-2]
                self.process_message(message)
            elif line.startswith("console.input("):
                prompt = line[14:-2]
                self.process_input(prompt)
            elif "=" in line:
                self.process_assignment(line)
            elif "math(" in line:
                self.process_math(line)

    def process_math(self, line):
        expression = line[5:-1].strip()
        result = self.evaluate_expression(expression)
        print(result)

    def process_assignment(self, line):
        parts = line.split("=")
        var_name = parts[0].strip()
        var_value = parts[1].strip()
        if not var_name.startswith("var."):
            raise ValueError("Variable name must be in the format 'var.x'")
        var_name = var_name[4:]
        self.variables[var_name] = var_value

    def process_message(self, message):
        for var_name, var_value in self.variables.items():
            message = message.replace(f"var.{var_name}", var_value)
        print(message)

    def process_input(self, prompt):
        prompt = prompt.strip('"')
        user_input = input(prompt)
        self.variables["input"] = user_input

    def evaluate_expression(self, expression):
        if "==" in expression:
            parts = expression.split("==")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            return arg1 == arg2
        elif "!=" in expression:
            parts = expression.split("!=")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            return arg1 != arg2
        elif ">" in expression:
            parts = expression.split(">")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            return arg1 > arg2
        elif "<" in expression:
            parts = expression.split("<")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            return arg1 < arg2
        elif "+" in expression:
            parts = expression.split("+")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            return arg1 + arg2
        elif "-" in expression:
            parts = expression.split("-")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            return arg1 - arg2
        elif "*" in expression:
            parts = expression.split("*")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            return arg1 * arg2
        elif "/" in expression:
            parts = expression.split("/")
            arg1 = self.get_value(parts[0].strip())
            arg2 = self.get_value(parts[1].strip())
            if arg2 == 0:
                return "Error: division by zero"
            return arg1 / arg2
        else:
            return self.get_value(expression)

    def get_value(self, value):
        if value.startswith("var."):
            var_name = value[4:]
            if var_name in self.variables:
                try:
                    return float(self.variables[var_name])
                except ValueError:
                    return self.variables[var_name]
            else:
                raise ValueError(f"Variable '{var_name}' not found")
        else:
            try:
                return float(value)
            except ValueError:
                return value

__version__ = "0.2"

def run():
    while True:
        command = input(">: ")
        parts = command.split()
        if len(parts) == 2 and parts[0] == "nslash":
            file_name = parts[1]
            try:
                with open(file_name, "r") as f:
                    code = f.read()
                interpreter = Interpreter(code)
                interpreter.interpret()
            except FileNotFoundError:
                print("File not found!")
        elif len(parts) == 1 and parts[0] == "-v":
            print(f"N/Script {__version__}")
        elif len(parts) == 1 and parts[0] == "-exit":
            break
        else:
            print("Invalid command!")

run()