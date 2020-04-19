from Stack import Stack as stack


class IntegerToBinary:
    def __init__(self):
        self.binary = ""
        self.myStack = stack()

    def convert_unsigned_integer_to_binary(self, value):
        if value is 0:
            return "0"
        elif str(value).isnumeric() is False:
            return "Invalid Input"
        else:
            while (value >= 1):
                quo = value // 2
                self.myStack.push(value % 2)
                value = quo

            self._build_binary_string()
            return self.binary

    def _build_binary_string(self):
        while (self.myStack.peek() is not None):
            self.binary = self.binary + str(self.myStack.pop())
