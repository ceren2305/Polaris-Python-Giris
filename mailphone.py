import re

input_file = 'lvl1_bozuk_veri.txt'
output_file = 'lvl1_temiz_rehber.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(\d{3,4}[-\s]?\d{3}[-\s]?\d{4})'

emails = re.findall(email_pattern, content)
phones = re.findall(phone_pattern, content)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("EMAILS:\n")
    f.write("\n".join(emails) + "\n\n")
    f.write("PHONE NUMBERS:\n")
    f.write("\n".join(phones))