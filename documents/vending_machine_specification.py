import pypandoc

# DOCX 파일을 PDF로 변환
pypandoc.convert_file('c:/copilot/documents/VendingMachine_Specification.docx', 'pdf', outputfile='VendingMachine_Specification.pdf', extra_args=['--pdf-engine=xelatex'])

# DOCX 파일을 HTML로 변환
pypandoc.convert_file('c:/copilot/documents/VendingMachine_Specification.docx', 'html', outputfile='VendingMachine_Specification.html')

# DOCX 파일을 Markdown으로 변환
pypandoc.convert_file('c:/copilot/documents/VendingMachine_Specification.docx', 'md', outputfile='VendingMachine_Specification.md')