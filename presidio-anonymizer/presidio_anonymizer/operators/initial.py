from typing import Dict
from presidio_anonymizer.operators import Operator
from presidio_anonymizer.operators import OperatorType

class Initial(Operator):
    """
    Anonymizes text by replacing it with its initials.
    Example: "John Smith" -> "J. S."
    """

    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        Replace the text with the initials of each word.

        :param text: The text to be anonymized.
        :param params: Optional parameters (not used).
        :return: The initials of the text (e.g., "J. S.").
        """
        if not text:
            return ""
        
        # 1. Split the text into individual words
        words = text.split()

        # 2. Get first letter of each word and add a dot
        #    "John" -> "J."
        initials_list = [word[0] + "." for word in words]

        # 3. Join them with a space
        #    ["J.", "S."] -> "J. S."
        return " ".join(initials_list)

    def validate(self, params: Dict = None) -> None:
        """
        Validate the parameters for the operator.
        """
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize