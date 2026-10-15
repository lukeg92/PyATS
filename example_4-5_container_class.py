from pyats import aetest
#Define a container and two subsections
class MycommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def subsection_one(self):
        self.a = 1
        print("hello world!")

    @aetest.subsection
    def subsection_two(self):
        assert self.a == 1

#Instantiate the class
common_setup = MycommonSetup()

#Loop through to sww what we get
for i in common_setup:
    print(i)