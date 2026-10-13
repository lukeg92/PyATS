from pyats import aetest

class MyCommonSetup(aetest.CommonSetup)
    """Common Setup"""

    @aetest.subsection
    def connect_to_devices(self):
        """Code to connect to devices"""
        pass

    @aetest.subsection
    def apply_base_config(self):
        """Code to configure devices with base/initial config"""
        pass
    