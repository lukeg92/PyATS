from pyats import aetest

class Testcase(aetest.Testcase):
    """Testcase with steps"""

    @aetest.test
    def test(self, steps):
        """Code for test section and steps"""
        #steps.start() begins the step
        with steps.start("The first step") as step:
            print("This is step one")

        with steps.start("The second step") as step:
            print("This is step two")