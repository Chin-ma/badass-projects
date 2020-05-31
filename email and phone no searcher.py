import re, pyperclip
email_patt = re.compile(r'''
[A-Za-z0-9][A-Za-z0-9!#$%&'\*\+-/=\?\^_`{\|]*#username
@
[A-Za-z0-9-\.]+#domain
\.
com|org|net#super domain
''', re.VERBOSE)
string = pyperclip.paste()
matched_emails = email_patt.findall(string)
matched_emails = ", ".join(matched_emails)
phone_patt = re.compile(r'([+-]\d{1,3})(\s|.|-)(\d{3})(\2)(\d{3})(\2)(\d{3})')
matched_no = phone_patt.findall(string)
matched_nos = []
for item in matched_no:
    each = "".join(item)
    matched_nos.append(each)
matched_nos = ', '.join(matched_nos)
if len(matched_emails)==0 and len(matched_nos)==0:
    print('no emails and phone nos found on clipboard')
else:
    all_matched = f'email adresses are: {matched_emails}\nphone nos are: {matched_nos}'
    print(all_matched)

    pyperclip.copy(f'''{matched_emails}{matched_nos}''')
