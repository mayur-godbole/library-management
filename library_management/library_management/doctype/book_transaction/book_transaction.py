from frappe.model.document import Document
import frappe
from frappe.utils import getdate

class BookTransaction(Document):
    pass

def validate_book_transaction(doc, method):
    if doc.transaction_type == "Issue":
        if not doc.due_date:
            frappe.throw("Due Date is mandatory for Issue transactions")

    if doc.transaction_type == "Return":
        if not doc.return_date:
            frappe.throw("Return Date is mandatory for Return transactions")

    if doc.return_date:
        if getdate(doc.return_date) < getdate(doc.transaction_date):
            frappe.throw("Return Date cannot be before Transaction Date")
