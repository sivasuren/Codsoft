import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.create_ui()

    def create_ui(self):
        self.window = tk.Tk()
        self.window.title("Contact Book")

        # Labels and Entry widgets for contact details
        tk.Label(self.window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.window)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.window)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.window, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.window)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons for actions
        tk.Button(self.window, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.window, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.window, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.window, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.window, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if
                       search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]
            if results:
                contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in results])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Info", "No matching contacts found.")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_term:
            for contact in self.contacts:
                if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
                    updated_name = simpledialog.askstring("Update Contact",
                                                          f"Update Name (Current: {contact['Name']}):",
                                                          initialvalue=contact['Name'])
                    updated_phone = simpledialog.askstring("Update Contact",
                                                           f"Update Phone (Current: {contact['Phone']}):",
                                                           initialvalue=contact['Phone'])
                    updated_email = simpledialog.askstring("Update Contact",
                                                           f"Update Email (Current: {contact['Email']}):",
                                                           initialvalue=contact.get('Email', ''))
                    updated_address = simpledialog.askstring("Update Contact",
                                                             f"Update Address (Current: {contact['Address']}):",
                                                             initialvalue=contact.get('Address', ''))

                    contact['Name'] = updated_name if updated_name else contact['Name']
                    contact['Phone'] = updated_phone if updated_phone else contact['Phone']
                    contact['Email'] = updated_email if updated_email else contact.get('Email', '')
                    contact['Address'] = updated_address if updated_address else contact.get('Address', '')

                    messagebox.showinfo("Success", "Contact updated successfully.")
                    break
            else:
                messagebox.showinfo("Info", "No matching contacts found.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_term:
            for contact in self.contacts:
                if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
                    confirm_delete = messagebox.askyesno("Delete Contact", f"Do you want to delete {contact['Name']}?")
                    if confirm_delete:
                        self.contacts.remove(contact)
                        messagebox.showinfo("Success", "Contact deleted successfully.")
                    break
            else:
                messagebox.showinfo("Info", "No matching contacts found.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
