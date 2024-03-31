import pprint
from pathlib import Path

import structlog

from dltool.config import get_tool_path
from dltool.tool.custom_classes import CustomFieldInfo

# from dltool.tool.custom_classes import CustomField as Field


logger = structlog.get_logger(__name__)


class Project:

    def __init__(self, config, io) -> None:
        self._io = io
        self._config = config

    output_folder: Path = None

    def get_project_inputs(self) -> dict:
        fields = self._config.model_fields

        try:

            for field, item in fields.items():
                _input = {"input_name": field, "question_text": item.question_text, "default": item.default}

                input_value = self._get_project_input(_input)

        except Exception as e:
            logger.exception("Failed")

        return {}

    def _get_project_input(self, input):

        # TODO - standardize styling elements?
        separator = "<comment> -> </comment>"

        write_str = f"{input['question_text']} <debug>({input['default']})</debug>{separator}"

        # Ask the question
        self._io.write(write_str)

        # Get the value
        value = self._io.read_line()

        return value

    def output_templates(self):

        templates_folder_path = get_tool_path("templates")
        print(f"templates folder = {templates_folder_path}")

        template = Path(templates_folder_path, "main_dlt_project")
        print(f"Template = {template}")

        extra_context = self._config.model_json_schema()
        pprint.pprint(extra_context)

        extra_context = self._config.model_fields
        pprint.pprint(extra_context)

        # print(f'Extra context value: {extra_context}')

        output_dir = Path("./")

        # try:
        #     cookiecutter(
        #         str(template),
        #         no_input=True,
        #         extra_context=extra_context,
        #         # replay=replay,
        #         # overwrite_if_exists=overwrite_if_exists,
        #         output_dir=output_dir,
        #         # config_file=config_file,
        #         # default_config=default_config,
        #         # password=os.environ.get('COOKIECUTTER_REPO_PASSWORD'),
        #         # directory=directory,
        #         # skip_if_file_exists=skip_if_file_exists,
        #         # accept_hooks=_accept_hooks,
        #         # keep_project_on_failure=keep_project_on_failure,
        #         )

        # except Exception as e:
        #     logger.exception("Cookiecutter failed to initialize.")
        #     sys.exit(1)


class ProjectConfig(BaseModel):

    project_name: str = CustomFieldInfo(
        default="Delta Live Tool Demo",
        question_text="What is the <comment>name</comment> of your <info>project</info>?",
    )
    project_slug: str = CustomFieldInfo(
        default="delta_live_tool_demo",
        question_text="What is the <comment>slug name</comment> of your <info>project</info>?",
    )
    author: str = CustomFieldInfo(
        default="some author function to get github email and name",
        question_text="What is the <comment>name</comment> of your <info>author</info>?",
    )

    @classmethod
    def from_yaml(cls, file_path: Path = None):
        pass
