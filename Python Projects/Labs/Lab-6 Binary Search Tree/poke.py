# poke.py
class Poke:
    def __init__(self, _list):
        self.name = _list[0]
        self.id = int(_list[1])
        self.japan_name = _list[2]

    def __lt__(self, other):
        if isinstance(other, int):
            return self.id < other

        elif isinstance(other, Poke):
            return self.id < other.id

        else:
            raise IndexError("Error, invalid Type")

    def __gt__(self, other):
        if isinstance(other, int):
            return self.id > other

        elif isinstance(other, Poke):
            return self.id > other.id

        else:
            raise IndexError("Error, invalid Type")

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other

        elif isinstance(other, Poke):
            return self.id == other.id

        else:
            raise IndexError("Error, invalid Type")

    def __str__(self):
        return (
            "Pokemon name: "
            + self.name
            + " Id: "
            + str(self.id)
            + " Japanese name: "
            + self.japan_name
        )

    def __ne__(self, other):
        if isinstance(other, int):
            return self.id != other

        elif isinstance(other, Poke):
            return self.id != other.id

        else:
            raise IndexError("Error, invalid Type")
