############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller,
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("Muskmelon", "musk", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType("Casaba", "cas", 2003, "orange", False, None)
    casaba.add_pairing("strawberry")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("Crenshaw", "cren", 1996, "green", False, None)
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType(
        "Yellow Watermelon", "yw", 2013, "yellow", False, True)
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon
    return melon_dict


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Returns True or False if melon is sellable"""
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melons_dict = make_melon_type_lookup(melon_types)
    melon1 = Melon(melons_dict["yw"], 8, 7, 2, "Sheila")
    melon2 = Melon(melons_dict["yw"], 3, 4, 2, "Sheila")
    melon3 = Melon(melons_dict["yw"], 9, 8, 3, "Sheila")
    melon4 = Melon(melons_dict["cas"], 10, 6, 35, "Sheila")
    melon5 = Melon(melons_dict["cren"], 8, 9, 35, "Michael")
    melon6 = Melon(melons_dict["cren"], 8, 2, 35, "Michael")
    melon7 = Melon(melons_dict["cren"], 2, 3, 4, "Michael")
    melon8 = Melon(melons_dict["musk"], 6, 7, 4, "Michael")
    melon9 = Melon(melons_dict["yw"], 7, 10, 3, "Sheila")
    return [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
