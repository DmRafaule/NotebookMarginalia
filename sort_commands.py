from config import DATA_FILE_PATH, NUM_LIM
from data_manager.manager import DataManager
from datetime import datetime
from operator import itemgetter


def by_number(args):
    manager = DataManager(DATA_FILE_PATH)
    manager.update(manager.data[:args.x])


def by_category(args):
    manager = DataManager(DATA_FILE_PATH)
    new_data = []
    for i in manager.data:
        if i['category'] is not None and i['category'] == args.category:
            new_data.append(i)
    manager.update(new_data[:NUM_LIM])


def by_subcategory(args):
    manager = DataManager(DATA_FILE_PATH)
    new_data = []
    for i in manager.data:
        if i['subcategory'] is not None and i['subcategory'] == args.subcategory:
            new_data.append(i)
    manager.update(new_data[:NUM_LIM])


def by_increasing(args):
    # Get singleton of data manager
    manager = DataManager(DATA_FILE_PATH)
    new_data = []
    # Update time of creation data (cast it to datetime class)
    # For a reason to compare and sort it
    for data in manager.data:
        date = datetime.strptime(data['time_created'], "%Y-%m-%d %H:%M:%S.%f")
        data['time_created'] = date
        new_data.append(data)
    # Figure out do we actually needed to sort it
    if args.is_increasing != "true":
        new_data = sorted(new_data, key=itemgetter("time_created"), reverse=True)
    # Convert data back to string for json serialization
    res_data = []
    for data in new_data:
        data['time_created'] = str(data['time_created'])
        res_data.append(data)
    manager.update(res_data[:NUM_LIM])
