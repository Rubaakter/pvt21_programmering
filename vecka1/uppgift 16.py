from PyPDF2 import PdfFileReader

# def extract_information(pdf_path):
#     with open("text_file.pdf", 'rb') as f:
#         pdf = PdfFileReader(f)
#         information = pdf.getDocumentInfo()
#         number_of_pages = pdf.getNumPages()
#
#
#     txt = f"""
#     Information about {"text_file.pdf"}:
#
#     Author: {information.author}
#     Creator: {information.creator}
#     Producer: {information.producer}
#     Subject: {information.subject}
#     Title: {information.title}
#     Number of pages: {number_of_pages}
#     """
#
#     print(txt)
#     return information
#
# if __name__ == '__main__':
#     path = 'text_file.pdf'
#     extract_information(path)

x_ray = ["Sep  6 07:42:27 ripley /usr/lib/y-daemon-X-RAY[666]: 37",
         "Sep  6 07:31:41 ripley /usr/lib/y-daemon-X-RAY[666]: Exchange",
         "Sep  6 07:31:41 ripley /usr/lib/y-daemon-X-RAY[666]: 4 pm",
         "Sep  6 07:42:22 ripley /usr/lib/y-daemon-X-RAY[666]: at",
         "Sep  6 07:42:27 ripley /usr/lib/y-daemon-X-RAY[666]: 37"]
bear = ["Sep  6 07:31:41 ripley /usr/lib/y-daemon-BEAR[666]: happens",
        "Sep  6 07:42:22 ripley /usr/lib/y-daemon-BEAR[666]: location",
        "Sep  6 07:42:22 ripley /usr/lib/y-daemon-BEAR[666]: location"]
for i in range(3):
    print(bear[i])

for i in range(5):
    print(x_ray[i])