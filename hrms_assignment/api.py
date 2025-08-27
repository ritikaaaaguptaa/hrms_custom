import frappe

def on_update_employee(doc, method):
    if doc.custom_lifecycle_stage == "Confirmation" and doc.status != "Active":
        doc.status = "Active"

    if doc.custom_lifecycle_stage == "Exit":
        pdf = frappe.get_print("Employee", doc.name, "Experience Letter", as_pdf=True)

        # Save file and attach to Employee
        file = frappe.get_doc({
            "doctype": "File",
            "file_name": f"Experience_Letter_{doc.name}.pdf",
            "attached_to_doctype": "Employee",
            "attached_to_name": doc.name,
            "content": pdf,
            "is_private": 1
        })
        file.insert()



