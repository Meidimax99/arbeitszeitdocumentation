import pdfrw

template = pdfrw.PdfReader("template.pdf")
def find_field(ident):
    fields = template.Root.AcroForm.Fields
    for field in fields:
        if (field.T == ident):
            return field


def fill_field(string, ident):
    formfield = find_field(ident)
    formfield.V = string


def clear_Fields():
    for i in range(1, 14):
        fill_field("", "(TagRow" + str(i) + ")")
        fill_field("", "(vonRow" + str(i) + ")")
        fill_field("", "(bisRow" + str(i) + ")")
        fill_field("", "(StundenRow" + str(i) + ")")


def pdf_full():
    # fix for not showing value? https://github.com/pmaupin/pdfrw/issues/84
    global filecount
    annotations = template.pages[0]['/Annots']
    for annotation in annotations:
        # ... validate / update fields here
        annotation.update(pdfrw.PdfDict(AP=''))

    # programmlogic
    writer = pdfrw.PdfWriter()
    writer.addpages(template.pages)
    writer.write(outPath + "ZeitDocumentation" + str(filecount) + ".pdf")
    filecount += 1

    clear_Fields()


def setupPDF():
    # fill basic fields
    # Name
    fill_field(name, nameField)


def fill_row(rowNum, entry):
    fill_field(str(entry.date.day) + "." + str(entry.date.month) + "." + str(entry.date.year),
               "(TagRow" + str(rowNum) + ")")
    fill_field(entry.starttime, "(vonRow" + str(rowNum) + ")")
    fill_field(entry.endtime, "(bisRow" + str(rowNum) + ")")
    fill_field(str(entry.hours), "(StundenRow" + str(rowNum) + ")")

    if rowNum == 1:
        fill_field(str(entry.date.day) + "." + str(entry.date.month) + "." + str(entry.date.year), "(von)")

    if rowNum == 13:
        fill_field(str(entry.date.day) + "." + str(entry.date.month) + "." + str(entry.date.year), "(bis)")

    return
