class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return 'value is not a float'
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer_value = 0

        for i in range(len(value)):
            if roman_values[value[i]] > roman_values[value[i - 1]]:
                integer_value += roman_values[value[i]] - 2 * roman_values[value[i - 1]]
            else:
                integer_value += roman_values[value[i]]

        return cls(integer_value)

    @classmethod
    def from_string(cls, string_value: str):
        if not isinstance(string_value, str):
            return f'wrong type'
        return cls(int(string_value))
