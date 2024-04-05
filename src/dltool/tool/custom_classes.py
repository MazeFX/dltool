from __future__ import annotations

from pydantic.fields import FieldInfo


class CustomFieldInfo(FieldInfo):
    question_text: str = None

    def __init__(self, question_text, **kwargs) -> None:
        self.question_text = question_text
        super().__init__(**kwargs)
