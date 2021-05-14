from plover_build_utils.testing import blackbox_test
from plover.registry import registry
from plover.config import DEFAULT_SYSTEM_NAME
from plover import system

registry.update()
system.setup(DEFAULT_SYSTEM_NAME)

@blackbox_test
class TestsBlackbox:

	def test_start_words(self):
		r'''
		"KAUPB": "{:initial:con:foo}",

		KAUPB	" con"
		KAUPB	" confoo"

		'''
