# Restructure tests/ by Modules (Phased Plan)

To manage this complex restructuring safely, we will execute the refactoring in five incremental stages. At the end of each stage, we will run the verification pipeline to ensure all tests pass and coverage remains at 100% statement coverage.

---

## Stage 1: Core Utility Tests

Restructures the tests for global factory/utility modules directly under `ats_utilities/`:

### Relocated Test Files
* `tests/ats_factory_class_test.py` -> `tests/ats_factory_class_test.py` (kept at root for root file)
* `tests/ats_factory_component_test.py` -> `tests/ats_factory_component_test.py` (kept at root)
* `tests/ats_factory_dict_utils_test.py` -> `tests/ats_factory_dict_utils_test.py` (kept at root)
* `tests/ats_factory_file_utils_test.py` -> `tests/ats_factory_file_utils_test.py` (kept at root)
* `tests/ats_factory_inspector_test.py` -> `tests/ats_factory_inspector_test.py` (kept at root)
* `tests/ats_factory_type_test.py` -> `tests/ats_factory_type_test.py` (kept at root)
* `tests/ats_bundles_test.py:test_context_bundle` -> `tests/ats_context_bundle_test.py` (tests `context_bundle.py`)

---

## Stage 2: Exceptions, Config Setup, Option

Restructures exceptions, configuration setup utilities, and CLI option parsing:

### New Directories
* `tests/exceptions/`
* `tests/config_setup/`
* `tests/option/`
* `tests/option/command/`
* `tests/option/parser/`
* `tests/option/strategy/`

### Relocated & Split Test Files
* `tests/ats_exceptions_test.py` -> `tests/exceptions/ats_exceptions_test.py`
* `tests/ats_config_setup_bundle_test.py` -> `tests/config_setup/ats_config_setup_bundle_test.py`
* `tests/ats_template_dir_test.py` -> `tests/config_setup/ats_template_dir_test.py`
* `tests/ats_pro_config_test.py` -> `tests/config_setup/ats_pro_config_test.py`
* `tests/ats_pro_name_test.py` -> `tests/config_setup/ats_pro_name_test.py`
* `tests/ats_bundles_test.py:test_option_component_bundle` -> `tests/option/ats_component_bundle_test.py`
* `tests/ats_option_parser_test.py` split into:
  * `tests/option/ats_option_engine_test.py` (tests `OptionManager` engine)
  * `tests/option/strategy/ats_parser_strategy_test.py` (tests `ParserStrategy` strategy)
  * `tests/option/command/ats_command_option_test.py` (tests `CommandOption`)

---

## Stage 3: Info, Logging, Reporter

Restructures metadata management, logger managers, and output/reporting modules:

### New Directories
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
* `tests/reporter/`
* `tests/reporter/theme/`

### Relocated & Split Test Files
* `tests/ats_bundles_test.py:test_logging_component_bundle` -> `tests/logging/ats_component_bundle_test.py`
* `tests/ats_bundles_test.py:test_logger_bundle` -> `tests/logging/logger/ats_logger_bundle_test.py`
* `tests/ats_bundles_test.py:test_reporter_component_bundle` -> `tests/reporter/ats_component_bundle_test.py`
* `tests/ats_logging_stdout_test.py` -> `tests/logging/logger/ats_logger_stdout_test.py`
* `tests/ats_logging_test.py` split into:
  * `tests/logging/ats_logging_engine_test.py` (tests `LoggerManager` engine)
  * `tests/logging/logger/ats_logger_test.py` (tests `Logger`)
* `tests/ats_reporter_test.py` split into:
  * `tests/reporter/ats_reporter_engine_test.py` (tests `Reporter` engine)
  * `tests/reporter/ats_proxy_reporter_test.py` (tests `ProxyReporter`)
  * `tests/reporter/theme/ats_console_theme_test.py` (tests `ConsoleTheme`)
* `tests/ats_info_test.py` split into:
  * `tests/info/ats_info_engine_test.py` (tests `InfoManager` engine)
  * `tests/info/build_date/ats_build_date_test.py` (tests `BuildDate`)
  * `tests/info/info_ok/ats_info_ok_test.py` (tests `InfoOk`)
  * `tests/info/licence/ats_licence_test.py` (tests `Licence`)
  * `tests/info/logo/ats_logo_test.py` (tests `Logo`)
  * `tests/info/name/ats_name_test.py` (tests `Name`)
  * `tests/info/organization/ats_organization_test.py` (tests `Organization`)
  * `tests/info/repository/ats_repository_test.py` (tests `Repository`)
  * `tests/info/use_github/ats_use_github_test.py` (tests `UseGithub`)
  * `tests/info/version/ats_version_test.py` (tests `Version`)
  * `tests/ats_bundles_test.py:test_info_component_bundle` -> `tests/info/ats_component_bundle_test.py`

---

## Stage 4: Splasher, Generator

Restructures console UI/progress-bars and template generator engines:

### New Directories
* `tests/splasher/`
* `tests/splasher/external/`
* `tests/splasher/progressbar/`
* `tests/splasher/property/`
* `tests/splasher/terminal/`
* `tests/generator/`
* `tests/generator/scheme/`
* `tests/generator/tar/`
* `tests/generator/template/`

### Relocated & Split Test Files
* `tests/ats_bundles_test.py:test_splash_component_bundle` -> `tests/splasher/ats_component_bundle_test.py`
* `tests/ats_bundles_test.py:test_splash_center_bundle` -> `tests/splasher/ats_splash_center_bundle_test.py`
* `tests/ats_bundles_test.py:test_generator_component_bundle` -> `tests/generator/ats_component_bundle_test.py`
* `tests/ats_bundles_test.py:test_generator_bundle` -> `tests/generator/ats_generator_bundle_test.py`
* `tests/ats_ext_infrastructure_test.py` -> `tests/splasher/external/ats_ext_infrastructure_test.py`
* `tests/ats_github_infrastructure_test.py` -> `tests/splasher/external/ats_github_infrastructure_test.py`
* `tests/ats_splash_property_test.py` -> `tests/splasher/property/ats_splash_property_test.py`
* `tests/ats_terminal_properties_test.py` -> `tests/splasher/terminal/ats_terminal_properties_test.py`
* `tests/ats_splash_test.py` -> `tests/splasher/ats_splasher_engine_test.py`
* `tests/ats_generator_test.py` split into:
  * `tests/generator/ats_generator_engine_test.py` (tests `Generator` engine)
  * `tests/generator/scheme/ats_scheme_loader_test.py` (tests `SchemeLoader`)
  * `tests/generator/tar/ats_tar_processor_test.py` (tests `TarProcessor`)
  * `tests/generator/template/ats_template_processor_test.py` (tests `TemplateProcessor`)

---

## Stage 5: Config IO Loader, Storer, Processors

Restructures all parsing, loading, storing, and format processing utilities:

### New Directories
* `tests/config_io/`
* `tests/config_io/cfg/`
* `tests/config_io/ini/`
* `tests/config_io/json/`
* `tests/config_io/xml/`
* `tests/config_io/yaml/`

### Relocated & Split Test Files
* `tests/ats_bundles_test.py:test_config_file_bundle` -> `tests/config_io/ats_config_file_bundle_test.py`
* `tests/ats_bundles_test.py:test_config_loader_bundle` -> `tests/config_io/ats_config_loader_bundle_test.py`
* `tests/ats_bundles_test.py:test_file_bundle` -> `tests/config_io/ats_file_bundle_test.py`
* `tests/ats_config_file_test.py` -> `tests/config_io/ats_conf_file_test.py`
* `tests/ats_config_manager_test.py` -> `tests/config_io/ats_config_loader_test.py`
* `tests/ats_file_check_test.py` -> `tests/config_io/ats_file_check_test.py`
* `tests/ats_base_cfg_test.py` -> `tests/config_io/cfg/ats_cfg_loader_test.py`
* `tests/ats_base_ini_test.py` -> `tests/config_io/ini/ats_ini_loader_test.py`
* `tests/ats_base_json_test.py` -> `tests/config_io/json/ats_json_loader_test.py`
* `tests/ats_base_xml_test.py` -> `tests/config_io/xml/ats_xml_loader_test.py`
* `tests/ats_base_yaml_test.py` -> `tests/config_io/yaml/ats_yaml_loader_test.py`
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
* `tests/ats_processors_test.py` split into:
  * `tests/config_io/cfg/ats_cfg_processor_test.py` (tests `CFGProcessor`)
  * `tests/config_io/ini/ats_ini_processor_test.py` (tests `INIProcessor`)
  * `tests/config_io/json/ats_json_processor_test.py` (tests `JSONProcessor`)
  * `tests/config_io/xml/ats_xml_processor_test.py` (tests `XMLProcessor`)
  * `tests/config_io/yaml/ats_yaml_processor_test.py` (tests `YAMLProcessor`)

---

## Verification Plan

### Automated Tests
* Run `./run_coverage.sh` at the end of each stage to verify that:
  * Restructured test files are discovered correctly.
  * All active tests pass.
  * Coverage metrics are kept intact.
