"""Process melons from file and print them"""

from harvest import make_melon_type_lookup, make_melon_types, Melon


def create_melons_from_file():
    """Process melons from file and print them"""
    with open("harvest_log.txt", encoding="utf8") as file:
        melons_from_file = []
        for line in file:
            attributes = line.rstrip().split()
            shape_rating = attributes[1]
            color_rating = attributes[3]
            melon_type = attributes[5]
            harvested_by = attributes[8]
            field_number = attributes[11]

            all_melons_type_list = make_melon_types()
            all_melons_dict = make_melon_type_lookup(all_melons_type_list)
            melon_type = all_melons_dict[melon_type]

            melons_from_file.append(
                Melon(melon_type,
                      shape_rating,
                      color_rating,
                      field_number,
                      harvested_by)
            )
        print(melons_from_file)


create_melons_from_file()
