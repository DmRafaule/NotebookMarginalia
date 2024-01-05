import config as Conf
import argparse
from ttypes import int1str
from command_manager.manager import CommandManager
import command_manager.callbacks as CB


parser = argparse.ArgumentParser(
        usage="python main.py [-h]",
        description="Fast and easy create notes to remember things.",
        add_help=True,
)
command_manager = CommandManager()
# Viewer
parser.add_argument("-v", action="append_const", const=True, help="Display only ids", required=False)
command_manager.set("v", CB.displayOnlyIDs)

parser.add_argument("-vM", action="append_const", const=True, help="Display titles with text", required=False)
command_manager.set("vM", CB.displayTitleWithText)

parser.add_argument("-vT", action="append_const", const=True, help="Display only titles", required=False)
command_manager.set("vT", CB.displayOnlyTitles)

parser.add_argument("-vE", action="append_const", const=True, help="Display titles, text, category, subcategory", required=False)
command_manager.set("vE", CB.displayTitleTextCategorySubcategory)

parser.add_argument("-vF", action="append_const", const=True, help="Display all available data about note", required=False)
command_manager.set("vF", CB.displayEverything)


functional_args = parser.add_mutually_exclusive_group()
# Getters
functional_args.add_argument("-g", type=str, help="Get note by ID", required=False, metavar="ID")
command_manager.set("g", CB.GetNote)

functional_args.add_argument("-gT", type=str, help="Get note by title", required=False, metavar="TITLE")
command_manager.set("gT", CB.GetNoteByTitle)

functional_args.add_argument("-gC", action="append_const", const=True, help="Get all categories", required=False)
command_manager.set("gC", CB.GetAllCategories)

functional_args.add_argument("-gCS", type=str, help="Get all subcategories in category", required=False, metavar="CATEGORY")
command_manager.set("gCS", CB.GetAllSubcategoriesByCategory)


# Remover
functional_args.add_argument("-r", type=str, help="Remove a note. By id of note.", required=False, metavar="ID")
command_manager.set("r", CB.RemoveNoteByID)

functional_args.add_argument("-rT", type=str, help="Remove a note. By title of note.", required=False, metavar="TITLE")
command_manager.set("rT", CB.RemoveNoteByTitle)

functional_args.add_argument("-rC", type=str, help="Remove a category with all notes in it.", required=False)
command_manager.set("rC", CB.RemoveCategory)

functional_args.add_argument("-rS", type=str, help="Remove a subcategory with all notes in it.", required=False)
command_manager.set("rS", CB.RemoveSubcategory)

# Changer
## Changer by id
functional_args.add_argument("-cIt", type=int1str, help="Change text of note by id", required=False, metavar=("ID", "NEW_TEXT"), nargs=2)
command_manager.set("cIt", CB.ChangeTextByID)

functional_args.add_argument("-cIT", type=int1str, help="Change title of note by id", required=False, metavar=("ID", "NEW_TITLE"), nargs=2)
command_manager.set("cIT", CB.ChangeTitleByID)

functional_args.add_argument("-cIC", type=int1str, help="Change category by id", required=False, metavar=("ID", "NEW_CATEGORY"), nargs=2)
command_manager.set("cIC", CB.ChangeCategoryByID)

functional_args.add_argument("-cIS", type=int1str, help="Change subcategory by id", required=False, metavar=("ID", "NEW_SUBCATEGORY"), nargs=2)
command_manager.set("cIS", CB.ChangeSubcategoryByID)

## Changer by title
functional_args.add_argument("-cTt", type=str, help="Change text of note by title", required=False, metavar=("TITLE", "NEW_TEXT"), nargs=2)
command_manager.set("cTt", CB.ChangeTextByTitle)

functional_args.add_argument("-cTT", type=str, help="Change title of note by title", required=False, metavar=("OLD_TITLE", "NEW_TITLE"), nargs=2)
command_manager.set("cTT", CB.ChangeTitleByTitle)

functional_args.add_argument("-cTC", type=str, help="Change category by title", required=False, metavar=("TITLE", "NEW_CATEGORY"), nargs=2)
command_manager.set("cTC", CB.ChangeCategoryByTitle)

functional_args.add_argument("-cTS", type=str, help="Change subcategory by title", required=False, metavar=("TITLE", "NEW_SUBCATEGORY"), nargs=2)
command_manager.set("cTS", CB.ChangeSubcategoryByTitle)


# Adder
functional_args.add_argument("-aM", type=str, help="Add new note. Minimal required text", required=False, metavar=("TEXT"))
command_manager.set("aM", CB.AddNewBaseNote)

functional_args.add_argument("-aMT", type=str, help="Add new note. With title", nargs=2, required=False, metavar=("TEXT", "TITLE"))
command_manager.set("aMT", CB.AddNewNoteWithTitle)

functional_args.add_argument("-aMTC", type=str, help="Add new note. With title and category", nargs=3, required=False, metavar=("TEXT", "TITLE", "CATEGORY"))
command_manager.set("aMTC", CB.AddNewNoteWithTitleCategory)

functional_args.add_argument("-aMTCS", type=str, help="Add new note. With title, category, subcategory", nargs=4, required=False, metavar=("TEXT", "TITLE", "CATEGORY", "SUBCATEGORY"))
command_manager.set("aMTCS", CB.AddNewNoteWithTitleCategorySubcategory)


# Sorter
functional_args.add_argument("-s", type=str, help="Sort notes.", required=False, nargs="*" )
command_manager.set("s", CB.Sort)

subparsers = parser.add_subparsers(required=False, title="Sorting values", help="Possible sorting commands.", metavar="")

parser_by_number = subparsers.add_parser('by_number', help=f"Select a number of output notes per page. Max value is {Conf.NUM_LIM}, Min value is {Conf.NUM_STR}")
parser_by_number.add_argument('x', type=int)
command_manager.set("by_number", CB.by_number)
parser_by_number.set_defaults(func=command_manager.get('by_number'))

parser_by_category = subparsers.add_parser('by_category', help="Sort notes by categories.")
parser_by_category.add_argument('category', type=str)
command_manager.set("by_category", CB.by_category)
parser_by_category.set_defaults(func=command_manager.get('by_category'))

parser_by_subcategory = subparsers.add_parser('by_subcategory', help="Sort notes by sub categories.")
parser_by_subcategory.add_argument('subcategory', type=str)
command_manager.set("by_subcategory", CB.by_subcategory)
parser_by_subcategory.set_defaults(func=command_manager.get('by_subcategory'))

parser_by_increasing_order = subparsers.add_parser('by_earliest', help="Sort notes by order(increasing or not) in which they are displaying.")
parser_by_increasing_order.add_argument('is_increasing', type=str)
command_manager.set("by_increasing", CB.by_increasing)
parser_by_increasing_order.set_defaults(func=command_manager.get('by_increasing'))

args = parser.parse_args()
dict_args = vars(args)

isEmpty = True
# Handle all commands by callbacks on each command
for a in reversed(dir(args)):
    if not a.startswith('__') and not callable(getattr(args, a)):
        if dict_args[a] is not None:
            isEmpty = False
            func = command_manager.get(a)
            func(parser, dict_args[a])

if isEmpty:
    print(Conf.GREETING_MESSAGE)
