import abc

class Assignment(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def lesson(self, student):
        pass

    @abc.abstractmethod
    def check(self, code):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        """
        Detects if a derived class is a subclass of this
        abstract one without extending it (duck typing)

        :param C:
        :return:
        """
        if cls is Assignment:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented


class IntroToPython:
# example with duck typing

    def lesson(self):
        return f"""
             Hello {self.student}. define two variables,
             an integer named a with value 1
             and a string named b with value 'hello'
         """

    def check(self, code):
        return code == "a = 1\nb = 'hello"


class Statistics(Assignment):
    # Example with explicit inheritance
    def lesson(self,student):
        return f"""
        Good work so far, 
        {self.student}.
        Now calculate the average numbers 
        """
    def check(self, code):
        import statistics

        code = "import statistics\n"+code
        local_vars = {}
        global_vars = {}
        exec(code, global_vars, local_vars)
        return local_vars.get("avg") == statistics.mean([1,5,18, -3])


class AssignmentGrader:
    def __init__(self, student, AssignmentClass):
        self.assignment = AssignmentClass()
        self.assignment.student = student
        self.attempts = 0
        self.correct_attempts = 0

    def check(self, code):
        self.attempts += 1
        result = self.assignment.check(code)
        if result:
            self.correct_attempts += 1
            return result

    def lesson(self):
        return self.assignment.lesson()

if __name__ == "__main__":
    print("testing Statistic subclassing")
    if issubclass(Statistics, Assignment):
        print("yes")
    else:
        print("no")
    print("testing IntroToPython subclassing")
    if issubclass(IntroToPython, Assignment):
        print("yes")
    else:
        print("no")


