from dltool.tool.custom_classes import CustomFieldInfo


def test_CustomFieldInfo_creation():
    new_field = CustomFieldInfo(question_text="What?")

    assert new_field.question_text == "What?"
