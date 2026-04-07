# tests/test_smoke.py


def test_import_main_module():
    """Smoke test to verify the main module can be imported."""
    try:
        import scripts  # Replace with actual package name if different

        assert scripts is not None
    except ImportError as e:
        assert False, f'Failed to import shopgoodwill-scripts package: {e}'


def test_dependency_availability():
    """Ensure key dependencies are available."""
    dependencies = [
        'gotify_handler',
        'parsedatetime',
        'Cryptodome',  # Note: pycryptodomex imports as Cryptodome
        'daemon',
        'requests',
        'tzdata',
    ]
    for package in dependencies:
        try:
            __import__(package)
        except ImportError as e:
            assert False, f'Dependency {package} not available: {e}'
