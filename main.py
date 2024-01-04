import config as Conf
import argparse
from ttypes import int1str
from mmap import COMMAND_MAP
import sort_commands as Sort_C


parser = argparse.ArgumentParser(
        usage="python main.py [-h]",
        description="Fast and easy create notes to remember things.",
        add_help=True,
)
# Viewer
parser.add_argument("-v", action="append_const", const=True, help="Display only ids", required=False)
parser.add_argument("-vM", action="append_const", const=True, help="Display titles with text", required=False)
parser.add_argument("-vT", action="append_const", const=True, help="Display only titles", required=False)
parser.add_argument("-vE", action="append_const", const=True, help="Display titles, text, category, subcategory", required=False)
parser.add_argument("-vF", action="append_const", const=True, help="Display all available data about note", required=False)

functional_args = parser.add_mutually_exclusive_group()
# Getters
functional_args.add_argument("-g", type=str, help="Get note by ID", required=False, metavar="ID")
functional_args.add_argument("-gT", type=str, help="Get note by title", required=False, metavar="TITLE")
functional_args.add_argument("-gC", action="append_const", const=True, help="Get all categories", required=False)
functional_args.add_argument("-gCS", type=str, help="Get all subcategories in category", required=False, metavar="CATEGORY")

# Remover
functional_args.add_argument("-r", type=str, help="Remove a note. By id of note.", required=False, metavar="ID")
functional_args.add_argument("-rT", type=str, help="Remove a note. By title of note.", required=False, metavar="TITLE")
functional_args.add_argument("-rC", type=str, help="Remove a category with all notes in it.", required=False)
functional_args.add_argument("-rS", type=str, help="Remove a subcategory with all notes in it.", required=False)

# Changer
## Changer by id
functional_args.add_argument("-cIt", type=int1str, help="Change text of note by id", required=False, metavar=("ID", "NEW_TEXT"), nargs=2)
functional_args.add_argument("-cIT", type=int1str, help="Change title of note by id", required=False, metavar=("ID", "NEW_TITLE"), nargs=2)
functional_args.add_argument("-cIC", type=int1str, help="Change category by id", required=False, metavar=("ID", "NEW_CATEGORY"), nargs=2)
functional_args.add_argument("-cIS", type=int1str, help="Change subcategory by id", required=False, metavar=("ID", "NEW_SUBCATEGORY"), nargs=2)
## Changer by title
functional_args.add_argument("-cTt", type=str, help="Change text of note by title", required=False, metavar=("TITLE", "NEW_TEXT"), nargs=2)
functional_args.add_argument("-cTT", type=str, help="Change title of note by title", required=False, metavar=("OLD_TITLE", "NEW_TITLE"), nargs=2)
functional_args.add_argument("-cTC", type=str, help="Change category by title", required=False, metavar=("TITLE", "NEW_CATEGORY"), nargs=2)
functional_args.add_argument("-cTS", type=str, help="Change subcategory by title", required=False, metavar=("TITLE", "NEW_SUBCATEGORY"), nargs=2)
# Adder
functional_args.add_argument("-aM", type=str, help="Add new note. Minimal required text", required=False, metavar=("TEXT"))
functional_args.add_argument("-aMT", type=str, help="Add new note. With title", nargs=2, required=False, metavar=("TEXT", "TITLE"))
functional_args.add_argument("-aMTC", type=str, help="Add new note. With title and category", nargs=3, required=False, metavar=("TEXT", "TITLE", "CATEGORY"))
functional_args.add_argument("-aMTCS", type=str, help="Add new note. With title, category, subcategory", nargs=4, required=False, metavar=("TEXT", "TITLE", "CATEGORY", "SUBCATEGORY"))


# Sorter
functional_args.add_argument("-s", type=str, help="Sort notes.", required=False, nargs="*" )
subparsers = parser.add_subparsers(required=False, title="Sorting values", help="Possible sorting commands.", metavar="")

parser_by_number = subparsers.add_parser('by_number', help=f"Select a number of output notes per page. Max value is {Conf.NUM_LIM}, Min value is {Conf.NUM_STR}")
parser_by_number.add_argument('x', type=int)
parser_by_number.set_defaults(func=Sort_C.by_number)

parser_by_category = subparsers.add_parser('by_category', help="Sort notes by categories.")
parser_by_category.add_argument('category', type=str)
parser_by_category.set_defaults(func=Sort_C.by_category)

parser_by_subcategory = subparsers.add_parser('by_subcategory', help="Sort notes by sub categories.")
parser_by_subcategory.add_argument('subcategory', type=str)
parser_by_subcategory.set_defaults(func=Sort_C.by_subcategory)

parser_by_increasing_order = subparsers.add_parser('by_earliest', help="Sort notes by order(increasing or not) in which they are displaying.")
parser_by_increasing_order.add_argument('is_increasing', type=str)
parser_by_increasing_order.set_defaults(func=Sort_C.by_increasing)

args = parser.parse_args()
dict_args = vars(args)

isEmpty = True
# Handle all commands by callbacks on each command
for a in reversed(dir(args)):
    if not a.startswith('__') and not callable(getattr(args, a)):
        if dict_args[a] is not None:
            isEmpty = False
            func = COMMAND_MAP[a]
            func(parser, dict_args[a])

if isEmpty:
    print(Conf.GREETING_MESSAGE)
