"""A phone book in which users can save their contact number with their names."""
import pandas


class ModifyConBook:
    """Allows modification on the phone book."""

    def __init__(self, phone_book_name, contact_book):
        self.phone_book_name = phone_book_name
        self.contact_book = contact_book

    def contact_number_validate(self):
        """Validates that the entered contact number is a 10-digit integer."""
        input_contact_number = input("Contact number should be a 10-digit integer.\nEnter Contact Number: ")
        if not input_contact_number.isdigit() or len(input_contact_number) != 10:
            print(f"\nContact number '{input_contact_number}' is invalid.")
            return self.contact_number_validate()
        return input_contact_number

    def add_contact(self):
        """Adds a new contact to the phone book."""
        try:
            input_contact_number = self.contact_number_validate()
            input_contact_name = input("Enter the name to save the contact number:  ")

            if input_contact_name not in self.contact_book:
                self.contact_book[input_contact_name] = input_contact_number
            else:
                print("A contact with this name already exists.")
        except (ValueError, KeyboardInterrupt):
            print("Contact number should be an integer.")

    def remove_contact(self, contact_name):
        """Removes a contact from the phone book by name."""
        if contact_name not in self.contact_book:
            print("No contact found with this name.")
        else:
            removed_number = self.contact_book.pop(contact_name)
            print(f"Contact '{contact_name}' with number {removed_number} has been removed.")

    def search_contact(self, name):
        """Searches for a contact by name."""
        if name not in self.contact_book:
            print("No contact found with this name.")
        else:
            print(f"Contact for '{name}' is {self.contact_book[name]}.")

    def view_contact(self):
        """Displays all contacts in the phone book."""
        if not self.contact_book:
            print("Your phone book doesn't have any contacts.")
        else:
            print()
            df = pandas.DataFrame(
                {"Name": list(self.contact_book.keys()), "Number": list(self.contact_book.values())},
                index=range(1, len(self.contact_book) + 1)
            )
            df.to_csv(f"{self.phone_book_name}.csv")
            print(df)


def create_phone_book():
    """Creates a phone book and allows the user to modify it."""
    phone_book_name = input("Enter the name for your phone book:\n")
    contact_book = {}
    user = ModifyConBook(phone_book_name, contact_book)

    while True:
        user_input = input("\nDo you want to modify your phone book? Enter yes/no: ").lower()
        if user_input == 'no':
            df = pandas.DataFrame(
                {"Name": list(contact_book.keys()), "Number": list(contact_book.values())},
                index=range(1, len(contact_book) + 1)
            )
            df.to_csv(f"{phone_book_name}.csv")
            print("Goodbye!")
            break
        elif user_input == 'yes':
            user_action = input("\nChoose an action:\n1. add\n2. remove\n3. search\n4. view\n").strip().lower()
            if user_action == 'add':
                user.add_contact()
            elif user_action == 'remove':
                contact_name = input("Enter the name of the contact you want to remove:\n")
                user.remove_contact(contact_name)
            elif user_action == 'search':
                name = input("Enter the name of the contact you want to search:\n")
                user.search_contact(name)
            elif user_action == 'view':
                user.view_contact()
            else:
                print('Please choose a valid option from the list!')
        else:
            print("Invalid input! Enter 'yes' or 'no'.")


if __name__ == "__main__":
    create_phone_book()
