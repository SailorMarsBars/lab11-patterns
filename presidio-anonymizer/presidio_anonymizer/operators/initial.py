from typing import Dict
from presidio_anonymizer.operators import Operator
from presidio_anonymizer.operators import OperatorType

class Initial(Operator):
    """
    Anonymizes text by replacing it with its first initial.
    """

    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        Replace the text with its first character.

        :param text: The text to be anonymized.
        :param params: Optional parameters (not used in this minimal example).
        :return: The first character of the text.
        """
        if not text:
            return ""
        
        # Return the first character (Initial)
        return text[0]

    def validate(self, params: Dict = None) -> None:
        """
        Validate the parameters for the operator.
        
        Since this is a minimal operator with no params, 
        we perform a pass.
        """
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize