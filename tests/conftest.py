"""Local pytest configuration"""

import pytest

from tests.utils import flush_all


@pytest.fixture(autouse=True)
def flush_local_registries() -> None:
    flush_all()
