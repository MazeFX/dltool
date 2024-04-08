from dltool.project_management.classes import Project


def test_project_object():
    config = "test_config"
    io = "test_io"
    test_project = Project(config, io)

    assert test_project._config == config
    assert test_project._io == io
