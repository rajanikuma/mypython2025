print (" rajani 60")

class Counter:
    instance_count = 0  

    def __init__(self):
        Counter.instance_count +=1

    @classmethod
    def get_instance_count(cls):
        """Returns the number of instances created."""
        return cls.instance_count
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

print(Counter.get_instance_count())  #
