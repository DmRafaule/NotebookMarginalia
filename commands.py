from config import NUM_LIM, NUM_STR, DATA_FILE_PATH
from data_manager.manager import Note, DataManager
from view_manager.manager import ViewManager
import os
from getkey import getkey, keys


def displayOnlyIDs(parser, args):
    view_manager = ViewManager()
    view_manager.set(view_manager._viewOnlyIDs)


def displayTitleWithText(parser, args):
    view_manager = ViewManager()
    view_manager.set(view_manager._viewTitleWithText)


def displayOnlyTitles(parser, args):
    view_manager = ViewManager()
    view_manager.set(view_manager._viewOnlyTitles)


def displayTitleTextCategorySubcategory(parser, args):
    view_manager = ViewManager()
    view_manager.set(view_manager._viewTitleTextCategorySubcategory)


def displayEverything(parser, args):
    view_manager = ViewManager()
    view_manager.set(view_manager._viewFull)


# REMOVE
def show_notes(note_dicts):
    view_manager = ViewManager()
    for note_dict in note_dicts:
        note = Note(note_dict)
        print(view_manager.view(note))


def Sort(parser, args):
    step = NUM_LIM
    offset = 0
    data_to_paginate = None
    for i, arg in enumerate(args):
        if arg == "by_category":
            if not args[i+1].startswith("by_"):
                sub_args = parser.parse_args([f'{arg}', f'{args[i+1]}'])
                sub_args.func(sub_args)
                manager = DataManager(DATA_FILE_PATH)
                offset = len(manager.data)
                data_to_paginate = manager.data
        elif arg == "by_subcategory":
            if not args[i+1].startswith("by_"):
                sub_args = parser.parse_args([f'{arg}', f'{args[i+1]}'])
                sub_args.func(sub_args)
                manager = DataManager(DATA_FILE_PATH)
                offset = len(manager.data)
                data_to_paginate = manager.data
        elif arg == "by_earliest":
            if not args[i+1].startswith("by_"):
                sub_args = parser.parse_args([f'{arg}', f'{args[i+1]}'])
                sub_args.func(sub_args)
                manager = DataManager(DATA_FILE_PATH)
                offset = len(manager.data)
                data_to_paginate = manager.data
        elif arg == "by_number":
            if not args[i+1].startswith("by_") and (int(args[i+1]) <= NUM_LIM and int(args[i+1]) >= NUM_STR):
                manager = DataManager(DATA_FILE_PATH)
                offset = len(manager.data)
                data_to_paginate = manager.data
                sub_args = parser.parse_args(f'{arg} {int(args[i+1])}'.split())
                sub_args.func(sub_args)
                step = int(args[i+1])
    counter = 0
    offset_counter = step
    while counter < offset:
        os.system('cls||clear')
        print (f"{counter}-{offset_counter}/{offset}")
        show_notes(data_to_paginate[counter:offset_counter])
        print("To new page, press [SPACE]")
        counter += step
        offset_counter += step
        while getkey() is not keys.SPACE:
            pass
    else:
        print("End of list")


def GetNote(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    res_data = []
    for data_record in manager.data:
        if args == data_record['id']:
            note = data_record
            res_data.append(note)
    show_notes(res_data)


def GetNoteByTitle(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    res_data = []
    for data_record in manager.data:
        if data_record['title'] is not None and data_record['title'].find(args) != -1:
            note = data_record
            res_data.append(note)
    show_notes(res_data)


def GetAllCategories(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    categories = []
    for record in manager.data:
        if record['category'] is not None:
            categories.append(record['category'])
    categories = set(categories)

    for category in categories:
        print(category)


def GetAllSubcategoriesByCategory(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    category = args
    subcategories = []
    for record in manager.data:
        if record['subcategory'] is not None and record['category'] is not None:
            if record['category'] == category:
                subcategories.append(record['subcategory'])
    subcategories = set(subcategories)

    for subcategory in subcategories:
        print(subcategory)


def RemoveNoteByID(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['id'] == args:
            manager.data.remove(record)
    manager.updateDataBase()


def RemoveNoteByTitle(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['title'] == args:
            manager.data.remove(record)
    manager.updateDataBase()


def RemoveCategory(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    records_to_remove = []
    for record in manager.data:
        if record['category'] == args:
            records_to_remove.append(record)

    for toRemove in records_to_remove:
        manager.data.remove(toRemove)

    manager.updateDataBase()


def RemoveSubcategory(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    records_to_remove = []
    for record in manager.data:
        if record['subcategory'] == args:
            records_to_remove.append(record)

    for toRemove in records_to_remove:
        manager.data.remove(toRemove)

    manager.updateDataBase()


def ChangeTextByID(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['id'] == args[0]:
            record['text'] = args[1]
    manager.updateDataBase()


def ChangeTitleByID(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['id'] == args[0]:
            record['title'] = args[1]
    manager.updateDataBase()


def ChangeCategoryByID(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['id'] == args[0]:
            record['category'] = args[1]
            record['subcategory'] = None
    manager.updateDataBase()


def ChangeSubcategoryByID(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['id'] == args[0]:
            record['subcategory'] = args[1]
    manager.updateDataBase()


def ChangeTextByTitle(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['title'] == args[0]:
            record['text'] = args[1]
    manager.updateDataBase()


def ChangeTitleByTitle(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['title'] == args[0]:
            record['title'] = args[1]
    manager.updateDataBase()


def ChangeCategoryByTitle(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['title'] == args[0]:
            record['category'] = args[1]
            record['subcategory'] = None
    manager.updateDataBase()


def ChangeSubcategoryByTitle(parser, args):
    manager = DataManager(DATA_FILE_PATH)
    for record in manager.data:
        if record['title'] == args[0]:
            record['subcategory'] = args[1]
    manager.updateDataBase()


def AddNewBaseNote(parser, args):
    note = Note({'text': args[0]})
    manager = DataManager(DATA_FILE_PATH)
    manager.save(note)


def AddNewNoteWithTitle(parser, args):
    note = Note({'text': args[0], 'title': args[1]})
    manager = DataManager(DATA_FILE_PATH)
    manager.save(note)


def AddNewNoteWithTitleCategory(parser, args):
    note = Note({'text': args[0], 'title': args[1], 'category': args[2]})
    manager = DataManager(DATA_FILE_PATH)
    manager.save(note)


def AddNewNoteWithTitleCategorySubcategory(parser, args):
    note = Note({'text': args[0], 'title': args[1], 'category': args[2], 'subcategory': args[3]})
    manager = DataManager(DATA_FILE_PATH)
    manager.save(note)
