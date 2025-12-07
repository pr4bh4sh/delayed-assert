# Changelog

All notable changes to this project will be documented in this file.

## [0.4.3] - 2025-12-07

### Added
- **Linting & Style Enforcement**: Added `pycodestyle` (PEP 8) and `pydocstyle` (PEP 257) checks to the CI pipeline.
- Enforced strict code style and docstring standards on the codebase.

## [0.4.2] - 2025-12-07

### Added
- **@test_case Decorator**: Validate expectations in functions with custom names (not starting with `test_`) by annotating them with `@test_case`.
- **Parallel Testing**: CI now uses `pytest-xdist` to run tests in parallel, ensuring thread safety.
- **Improved Test Discovery**: Added `pytest.ini` to ensure `test.py` is correctly discovered by pytest.

## [0.4.1] - 2025-12-07

### Added
- **Optional Caller Verification**: added ability to disable the automatic stack check that enforces `expect()` to be called from a `test*` method.
  - Disable via env var: `DELAYED_ASSERT_CHECK_CALLER=0`
  - Disable via API: `set_check_caller(False)`

## [0.4.0] - 2025-12-07

### Added
- **Color Output Control**: Added ability to toggle ANSI color output (useful for CI logs).
  - Disable via env var: `DELAYED_ASSERT_ENABLE_COLOR=0`
  - Disable via API: `set_color_enabled(False)`

### Changed
- Refactored internal color logic to use `Color`/`NoColor` strategy pattern.
- Updated CI to support Python 3.8, 3.9, 3.10, 3.11 (dropped 2.7 support).
- Automated PyPI publishing via GitHub Actions.

## [0.3.6] - 2021-09-17
- Minor version bump.
- Code style improvements (PEP8).

## [0.3.5] - 2021-01-17
- Fixed frame object compatibility between Python versions.

## [0.3.4] - 2020-12-16
- Ensure `assert_expectations` is called.

## [0.3.3] - 2020-05-01
- Added top level test method detection for caller.
