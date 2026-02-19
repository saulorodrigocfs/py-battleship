class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(
            self,
            start: tuple,
            end: tuple,
            is_drowned: bool = False
    ) -> None:
        if start[0] == end[0] and start[1] <= end[1]:
            self.decks = [
                Deck(start[0], i) for i in range(start[1], end[1] + 1)
            ]
        elif start[0] == end[0] and start[1] > end[1]:
            self.decks = [
                Deck(start[0], i) for i in range(end[1], start[1] + 1)
            ]
        elif start[1] == end[1] and start[0] <= end[0]:
            self.decks = [
                Deck(i, start[1]) for i in range(start[0], end[0] + 1)
            ]
        elif start[1] == end[1] and start[0] > end[0]:
            self.decks = [
                Deck(i, start[1]) for i in range(end[0], start[0] + 1)
            ]
        self.is_drowned = is_drowned

    def get_deck(self, row: int, column: int) -> Deck | None:
        for deck in self.decks:
            if deck.column == column and deck.row == row:
                return deck
        return None

    def fire(self, row: int, column: int) -> None:
        deck_shot = self.get_deck(row, column)
        if deck_shot is None:
            return
        deck_shot.is_alive = False
        count = 0
        for deck in self.decks:
            if deck.is_alive is False:
                count += 1
        if len(self.decks) == count:
            self.is_drowned = True


class Battleship:
    def __init__(self, ships: list) -> None:
        self.field = {}
        for ship_tuple in ships:
            ship_obj = Ship(ship_tuple[0], ship_tuple[1])
            for deck in ship_obj.decks:
                self.field[(deck.row, deck.column)] = ship_obj

    def fire(self, location: tuple) -> str:
        if location not in self.field:
            return "Miss!"
        ship = self.field[location]
        ship.fire(location[0], location[1])
        if ship.is_drowned:
            return "Sunk!"
        else:
            return "Hit!"
