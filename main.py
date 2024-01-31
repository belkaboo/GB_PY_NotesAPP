import json
import datetime
import sys


def save_notes(notes, filename):
    with open(filename, 'w') as file:
        json.dump(notes, file)


def load_notes(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def add_note(notes):
    note_id = input("Enter the note ID: ")
    title = input("Enter the note title: ")
    body = input("Enter the note text: ")
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes[note_id] = {'title': title, 'text': body, 'date_time': date_time}
    print("Note added successfully!")


def edit_note(notes):
    note_id = input("Enter the note ID to edit: ")
    if note_id in notes:
        title = input("Enter the new title: ")
        body = input("Enter the new text: ")
        notes[note_id]['title'] = title
        notes[note_id]['text'] = body
        notes[note_id]['date_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Note edited successfully!")
    else:
        print("Note not found!")


def delete_note(notes):
    note_id = input("Enter the note ID to delete: ")
    if note_id in notes:
        del notes[note_id]
        print("Note deleted successfully!")
    else:
        print("Note not found!")


def print_notes(notes):
    for note_id, note_info in notes.items():
        print(f"Note ID: {note_id}")
        print(f"Title: {note_info['title']}")
        print(f"Text: {note_info['text']}")
        print(f"Date/Time: {note_info['date_time']}")
        print("-" * 30)


def print_note_by_id(notes):
    note_id = input("Enter note ID to view: ")
    if note_id in notes:
        note_info = notes[note_id]
        print(f"Note ID: {note_id}")
        print(f"Title: {note_info['title']}")
        print(f"Text: {note_info['text']}")
        print(f"Date/Time: {note_info['date_time']}")
    else:
        print("Note not found!")


def filter_notes_by_date(notes):
    date_str = input("Enter date in format (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        filtered_notes = {note_id: note_info for note_id, note_info in notes.items() if
                          note_info['date_time'].startswith(date_str)}
        return filtered_notes
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return {}


def main():
    filename = 'notes.json'
    notes = load_notes(filename)

    while True:
        print("\nMenu:")
        print("1. Add Note")
        print("2. Edit Note")
        print("3. Delete Note")
        print("4. View Note by ID")
        print("5. Filter Notes by Date")
        print("6. Print All Notes")
        print("7. Save and Quit")
        print("8. Quit without saving")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            add_note(notes)
        elif choice == '2':
            edit_note(notes)
        elif choice == '3':
            delete_note(notes)
        elif choice == '4':
            print_note_by_id(notes)
        elif choice == '5':
            filtered_notes = filter_notes_by_date(notes)
            print_notes(filtered_notes)
        elif choice == '6':
            print_notes(notes)
        elif choice == '7':
            save_notes(notes, filename)
            print("Notes saved. Good bye!")
            break
        elif choice == '8':
            print("Good bye!")
            sys.exit()              
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()