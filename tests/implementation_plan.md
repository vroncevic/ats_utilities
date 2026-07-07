# Restructure tests/ by Modules (1-to-1 Test Mapping)

This plan describes restructuring the `tests/` directory layout to mirror the source code layout under `ats_utilities/`. Each source file will have a corresponding unit test file in the matching subpackage, and large multi-component test files will be split into individual 1-to-1 test modules.

## Proposed Changes

### 1. New Test Subdirectories & Packages

We will create the following subdirectories under `tests/` to mirror `ats_utilities/` layout, including empty `__init__.py` files to support recursive test discovery:
* `tests/base/`
* `tests/checker/`
* `tests/checker/context/`
* `tests/checker/reporter/`
* `tests/checker/type/`
* `tests/config_io/`
* `tests/config_io/cfg/`
* `tests/config_io/ini/`
* `tests/config_io/json/`
* `tests/config_io/xml/`
* `tests/config_io/yaml/`
* `tests/config_setup/`
* `tests/exceptions/`
* `tests/generator/`
* `tests/generator/scheme/`
* `tests/generator/tar/`
* `tests/generator/template/`
* `tests/info/`
* `tests/info/build_date/`
* `tests/info/info_ok/`
* `tests/info/licence/`
* `tests/info/logo/`
* `tests/info/name/`
* `tests/info/organization/`
* `tests/info/repository/`
* `tests/info/use_github/`
* `tests/info/version/`
* `tests/logging/`
* `tests/logging/logger/`
* `tests/option/`
* `tests/option/command/`
* `tests/option/parser/`
* `tests/option/strategy/`
* `tests/reporter/`
* `tests/reporter/theme/`
* `tests/splasher/`
* `tests/splasher/external/`
* `tests/splasher/progressbar/`
* `tests/splasher/property/`
* `tests/splasher/terminal/`

---

### 2. Splitting Large Multi-Component Test Files

We will split existing flat test files containing tests for multiple components/modules into individual test files mirroring the source files one-to-one:

#### `tests/ats_bundles_test.py`
Splits into:
* `tests/config_io/ats_config_file_bundle_test.py` -> tests `ConfigFileBundle`
* `tests/config_io/ats_config_loader_bundle_test.py` -> tests `ConfigLoaderBundle`
* `tests/config_io/ats_file_bundle_test.py` -> tests `FileBundle`
* `tests/logging/logger/ats_logger_bundle_test.py` -> tests `LoggerBundle`
* `tests/logging/ats_component_bundle_test.py` -> tests `LoggingComponentBundle`
* `tests/option/ats_component_bundle_test.py` -> tests `OptionComponentBundle`
* `tests/base/ats_component_bundle_test.py` -> tests `BaseComponentBundle`
* `tests/checker/ats_component_bundle_test.py` -> tests `CheckerComponentBundle`
* `tests/splasher/ats_component_bundle_test.py` -> tests `SplashComponentBundle`
* `tests/splasher/ats_splash_center_bundle_test.py` -> tests `SplashCenterBundle`

#### `tests/ats_processors_test.py`
Splits into:
* `tests/config_io/cfg/ats_cfg_processor_test.py` -> tests `CFGProcessor`
* `tests/config_io/ini/ats_ini_processor_test.py` -> tests `INIProcessor`
* `tests/config_io/json/ats_json_processor_test.py` -> tests `JSONProcessor`
* `tests/config_io/xml/ats_xml_processor_test.py` -> tests `XMLProcessor`
* `tests/config_io/yaml/ats_yaml_processor_test.py` -> tests `YAMLProcessor`

#### `tests/ats_checker_test.py`
Splits into:
* `tests/checker/ats_checker_engine_test.py` -> tests `Checker` engine
* `tests/checker/type/ats_type_validator_test.py` -> tests `TypeValidator`
* `tests/checker/context/ats_context_provider_test.py` -> tests `ContextProvider`
* `tests/checker/reporter/ats_checker_reporter_bundle_test.py` -> tests `CheckerReporterBundle`

#### `tests/ats_generator_test.py`
Splits into:
* `tests/generator/ats_generator_engine_test.py` -> tests `Generator` engine
* `tests/generator/scheme/ats_scheme_loader_test.py` -> tests `SchemeLoader`
* `tests/generator/tar/ats_tar_processor_test.py` -> tests `TarProcessor`
* `tests/generator/template/ats_template_processor_test.py` -> tests `TemplateProcessor`

#### `tests/ats_info_test.py`
Splits into:
* `tests/info/ats_info_engine_test.py` -> tests `InfoManager` engine
* `tests/info/build_date/ats_build_date_test.py` -> tests `BuildDate` component
* `tests/info/info_ok/ats_info_ok_test.py` -> tests `InfoOk` component
* `tests/info/licence/ats_licence_test.py` -> tests `Licence` component
* `tests/info/logo/ats_logo_test.py` -> tests `Logo` component
* `tests/info/name/ats_name_test.py` -> tests `Name` component
* `tests/info/organization/ats_organization_test.py` -> tests `Organization` component
* `tests/info/repository/ats_repository_test.py` -> tests `Repository` component
* `tests/info/use_github/ats_use_github_test.py` -> tests `UseGithub` component
* `tests/info/version/ats_version_test.py` -> tests `Version` component

#### `tests/ats_logging_test.py`
Splits into:
* `tests/logging/ats_logging_engine_test.py` -> tests `LoggerManager` engine
* `tests/logging/logger/ats_logger_test.py` -> tests `Logger`

#### `tests/ats_option_parser_test.py`
Splits into:
* `tests/option/ats_option_engine_test.py` -> tests `OptionManager` engine
* `tests/option/strategy/ats_parser_strategy_test.py` -> tests `ParserStrategy`
* `tests/option/command/ats_command_option_test.py` -> tests `CommandOption`

#### `tests/ats_reporter_test.py`
Splits into:
* `tests/reporter/ats_reporter_engine_test.py` -> tests `Reporter` engine
* `tests/reporter/ats_proxy_reporter_test.py` -> tests `ProxyReporter` (decorator vreport)
* `tests/reporter/theme/ats_console_theme_test.py` -> tests `ConsoleTheme`

---

### 3. Relocating & Renaming Single Test Files

Existing single-file test modules will be renamed/moved to their corresponding package folders under `tests/`:

* `tests/ats_base_cfg_test.py` -> `tests/config_io/cfg/ats_cfg_loader_test.py`
* `tests/ats_base_ini_test.py` -> `tests/config_io/ini/ats_ini_loader_test.py`
* `tests/ats_base_json_test.py` -> `tests/config_io/json/ats_json_loader_test.py`
* `tests/ats_base_xml_test.py` -> `tests/config_io/xml/ats_xml_loader_test.py`
* `tests/ats_base_yaml_test.py` -> `tests/config_io/yaml/ats_yaml_loader_test.py`
* `tests/ats_config_file_test.py` -> `tests/config_io/ats_conf_file_test.py` (for `ConfFile`)
* `tests/ats_config_manager_test.py` -> `tests/config_io/ats_config_loader_test.py` (for `ConfigLoader` manager)
* `tests/ats_config_setup_bundle_test.py` -> `tests/config_setup/ats_config_setup_bundle_test.py`
* `tests/ats_template_dir_test.py` -> `tests/config_setup/ats_template_dir_test.py`
* `tests/ats_pro_config_test.py` -> `tests/config_setup/ats_pro_config_test.py`
* `tests/ats_pro_name_test.py` -> `tests/config_setup/ats_pro_name_test.py`
* `tests/ats_exceptions_test.py` -> `tests/exceptions/ats_exceptions_test.py`
* `tests/ats_ext_infrastructure_test.py` -> `tests/splasher/external/ats_ext_infrastructure_test.py`
* `tests/ats_github_infrastructure_test.py` -> `tests/splasher/external/ats_github_infrastructure_test.py`
* `tests/ats_splash_property_test.py` -> `tests/splasher/property/ats_splash_property_test.py`
* `tests/ats_terminal_properties_test.py` -> `tests/splasher/terminal/ats_terminal_properties_test.py`
* `tests/ats_splash_test.py` -> `tests/splasher/ats_splasher_engine_test.py`
* `tests/ats_logging_stdout_test.py` -> `tests/logging/logger/ats_logger_stdout_test.py`
* `tests/ats_cfg2object_test.py` -> `tests/config_io/cfg/ats_cfg2object_test.py`
* `tests/ats_cfg_storer_test.py` -> `tests/config_io/cfg/ats_cfg_storer_test.py`
* `tests/ats_object2cfg_test.py` -> `tests/config_io/cfg/ats_object2cfg_test.py`
* `tests/ats_ini2object_test.py` -> `tests/config_io/ini/ats_ini2object_test.py`
* `tests/ats_ini_storer_test.py` -> `tests/config_io/ini/ats_ini_storer_test.py`
* `tests/ats_object2ini_test.py` -> `tests/config_io/ini/ats_object2ini_test.py`
* `tests/ats_json2object_test.py` -> `tests/config_io/json/ats_json2object_test.py`
* `tests/ats_json_storer_test.py` -> `tests/config_io/json/ats_json_storer_test.py`
* `tests/ats_object2json_test.py` -> `tests/config_io/json/ats_object2json_test.py`
* `tests/ats_xml2object_test.py` -> `tests/config_io/xml/ats_xml2object_test.py`
* `tests/ats_xml_storer_test.py` -> `tests/config_io/xml/ats_xml_storer_test.py`
* `tests/ats_object2xml_test.py` -> `tests/config_io/xml/ats_object2xml_test.py`
* `tests/ats_yaml2object_test.py` -> `tests/config_io/yaml/ats_yaml2object_test.py`
* `tests/ats_yaml_storer_test.py` -> `tests/config_io/yaml/ats_yaml_storer_test.py`
* `tests/ats_object2yaml_test.py` -> `tests/config_io/yaml/ats_object2yaml_test.py`
* `tests/ats_file_check_test.py` -> `tests/config_io/ats_file_check_test.py`
* `tests/ats_factory_class_test.py` -> `tests/ats_factory_class_test.py`
* `tests/ats_factory_component_test.py` -> `tests/ats_factory_component_test.py`
* `tests/ats_factory_dict_utils_test.py` -> `tests/ats_factory_dict_utils_test.py`
* `tests/ats_factory_file_utils_test.py` -> `tests/ats_factory_file_utils_test.py`
* `tests/ats_factory_inspector_test.py` -> `tests/ats_factory_inspector_test.py`
* `tests/ats_factory_type_test.py` -> `tests/ats_factory_type_test.py`

---

## Verification Plan

### Automated Tests
* Run `python3 run_coverage.py` or `./run_coverage.sh` and ensure:
  * Recursive test discovery correctly executes all 452 unit tests.
  * All tests pass successfully.
  * Code coverage remains at 99%+ with 100% statement coverage across all source files.
