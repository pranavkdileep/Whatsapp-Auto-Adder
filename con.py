import vobject
import csv

def extract_phone_numbers(vcf_file, csv_file):
    with open(vcf_file, 'r') as file:
        vcard_data = file.read()
        
    contacts = vobject.readComponents(vcard_data)
    
    phone_numbers = []
    for contact in contacts:
        for tel in contact.tel_list:
            phone_numbers.append(tel.value)
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Phone Numbers'])
        writer.writerows([[number] for number in phone_numbers])

# Example usage
vcf_file_path = 'contacts.vcf'
csv_file_path = 'phone_numbers.csv'

extract_phone_numbers(vcf_file_path, csv_file_path)
