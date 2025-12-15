import re
from typing import Dict
from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    """
    Anonymizes text by replacing it with its initials.
    Preserves non-alphanumeric prefixes.
    Example: "@abc" -> "@A."
    """

    def operate(self, text: str = None, params: Dict = None) -> str:
        """
        Replace the text with the initials of each word.
        
        :param text: The text to be anonymized.
        :param params: Optional parameters (not used).
        :return: The initials of the text.
        """
        if not text:
            return ""
        
        words = text.split()
        initials_list = []

        for word in words:
            # Regex Explanation:
            # ^([^a-zA-Z0-9]*) -> Group 1: Match 0 or more non-alphanumeric chars at start
            # ([a-zA-Z0-9])    -> Group 2: Match the very first alphanumeric char
            match = re.search(r'^([^a-zA-Z0-9]*)([a-zA-Z0-9])', word)

            if match:
                prefix = match.group(1)
                initial = match.group(2).upper()
                initials_list.append(f"{prefix}{initial}.")
            else:
                # Fallback: if no alphanumeric char is found (e.g. "!!!"), 
                # we preserve the word as is, or you could return "" depending on preference.
                # Here we preserve it to be safe.
                initials_list.append(word)

        return " ".join(initials_list)

    def validate(self, params: Dict = None) -> None:
        pass

    def operator_name(self) -> str:
        return "initial"

    def operator_type(self) -> OperatorType:
        return OperatorType.Anonymize