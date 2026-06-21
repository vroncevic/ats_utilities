# Implementation Plan - Fix Dependency Injection in Factory Context Bundle

In a recent update, `ATSReporter` was modified to accept `component_bundle` (of type `ReporterComponentBundle`) instead of receiving direct keyword arguments (like `checker` or `theme`). Because the fallback mechanism in `inject(...)` attempts to construct the dependency using keywords derived from its dependency declaration (`['checker']`), calling `inject(...)` when `context.reporter` is `None` raises a `TypeError` due to the mismatch.

This plan details how to resolve this by pre-instantiating `context.checker` and `context.reporter` using `ReporterComponentBundle` in `factory_context_bundle(...)` prior to calling the `inject(...)` helper. This ensures that the dependencies are correctly built and then directly injected into the class instance, bypassing fallback class-instantiation via `inject` and avoiding the `TypeError`.

## Proposed Changes

### Core Library

#### [MODIFY] [factory_context_bundle.py](file:///data/dev/python/ats_utilities/github/ats_utilities/ats_utilities/factory_context_bundle.py)

Update `factory_context_bundle` in `ats_utilities/factory_context_bundle.py` as follows:
- Import `ReporterComponentBundle` from `ats_utilities.reporter.component_bundle`.
- If `context.checker` is `None`, instantiate it using `ATSChecker()`.
- If `context.reporter` is `None`, instantiate it using `ATSReporter(component_bundle=ReporterComponentBundle(checker=context.checker))`.
- Pass these fully resolved dependencies to `inject(...)`.

```python
def factory_context_bundle(instance: Any, context: Optional[ContextBundle] = None):
    # No dependency injection then use default ones.
    if not bool(context):
        context = ContextBundle()

    if context.checker is None:
        context.checker = ATSChecker()

    if context.reporter is None:
        from ats_utilities.reporter.component_bundle import ReporterComponentBundle
        comp_bundle = ReporterComponentBundle(checker=context.checker)
        context.reporter = ATSReporter(component_bundle=comp_bundle)

    inject(
        instance,
        ('checker', context.checker, ATSChecker, None),
        ('reporter', context.reporter, ATSReporter, ['checker']),
        ('verbose', context.verbose, False, None)
    )
```

## Verification Plan

### Manual Verification
- Run the story file to ensure the injection resolves correctly:
  ```bash
  PYTHONPATH=. python3 use_cases/factory_context_bundle/story_factory_context_bundle.py
  ```
