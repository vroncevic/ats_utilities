from your_module_name import VerboseRoot, auto_str
import pytest


@auto_str
class ExampleClass(metaclass=VerboseRoot):
    def __init__(self, value) -> None:
        self.value = value


def test_verbose_root_creation() -> None:
    instance = ExampleClass('test_value')
    assert instance.verbose == 'ATS_UTILITIES'
    assert str(instance) == "ExampleClass(value=test_value)"


def test_verbose_root_module_path() -> None:
    class ExampleClassWithPath(metaclass=VerboseRoot):
        __module__ = 'ATS_UTILITIES.submodule'

    instance = ExampleClassWithPath()
    assert instance.verbose == 'ATS_UTILITIES::submodule'
    assert str(instance) == "ExampleClassWithPath()"


def test_verbose_root_no_module_path() -> None:
    class ExampleClassNoPath(metaclass=VerboseRoot):
        pass

    instance = ExampleClassNoPath()
    assert instance.verbose == 'ATS_UTILITIES'
    assert str(instance) == "ExampleClassNoPath()"


def test_verbose_root_instance_str() -> None:
    class ExampleClassWithStr(metaclass=VerboseRoot):
        def __str__(self):
            return "Custom __str__ method"

    instance = ExampleClassWithStr()
    assert instance.verbose == 'ATS_UTILITIES'
    assert str(instance) == "Custom __str__ method"


def test_verbose_root_invalid_package_name() -> None:
    class InvalidPackage(metaclass=VerboseRoot):
        package_name = None

    with pytest.raises(AttributeError):
        InvalidPackage()


def test_auto_str_invalid_usage() -> None:
    with pytest.raises(AttributeError):
        @auto_str
        class InvalidUsage:
            pass
