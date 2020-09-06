class FractionResult(dict):
    def __init__(self, numerator: str, denominator: str = "1"):
        super().__init__(numerator=numerator, denominator=denominator)

    @classmethod
    def parse_from_number_and_result(cls, number: int, result: str):
        """
        Returns FractionResult or None for undefined result
        """
        if number >= 0:
            return cls(result)
        elif number < 0:
            numerator = "-1" if number % 2 else "1"
            return cls(numerator, result)
