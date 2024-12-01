from domain.component.Die import Die

class Cup:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, '_init'):
            cls._init = True
            self.first_die = Die()
            self.second_die = Die()

    def roll(self) -> int:
        self.first_die.roll()
        self.second_die.roll()
        return self.first_die.face_value + self.second_die.face_value

    def is_double(self) -> bool:
        return self.first_die.face_value == self.second_die.face_value