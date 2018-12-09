import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = -1

def init():
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    print(next_id)
    if next_id == -1:
        next_id += 1
    else:
        next_id = int(entries[0]['id']) + 1
    
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(index):
    global entries, GUESTBOOK_ENTRIES_FILE
    try:
        for i in entries:
            if i['id'] == str(index):
                entries.pop(entries.index(i))
                break
    except:
        print("ERROR! Could not delete entries")

    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def edit_entry(index, edit):
    global entries, GUESTBOOK_ENTRIES_FILE
    try:
        for i in entries:
            if i['id'] == str(index):
                i['text'] = edit
                break
    except:
        print("ERROR! Could not edit entries")

    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")






