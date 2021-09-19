from plover_build_utils.testing import blackbox_test
from plover.registry import registry
from plover import system
from plover.config import DEFAULT_SYSTEM_NAME

registry.update()
system.setup(DEFAULT_SYSTEM_NAME)


@blackbox_test
class TestsBlackbox:

	def test_initial(self):
		r'''
		"A": "{a^}",
		"R": "{re^}",  # Prefix
		"K": "{:initial:key | k}",

		A	" a"
		K	" ak"
		K	" ak key"
		R	" ak key re"
		K	" ak key rekey"
		'''
