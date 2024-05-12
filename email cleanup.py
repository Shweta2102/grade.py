def clean_email_list(input_file, output_file):

    with open(input_file, 'r') as file:
        emails = set(file.read().splitlines())


    sorted_emails = sorted(emails)


    with open(output_file, 'w') as file:
        for email in sorted_emails:
            file.write(email + '\n')

    print(f"Cleaned email list has been written to {output_file}.")


clean_email_list('C:\Users\shwet\OneDrive\Desktop\email_list.txt', 'C:\Users\shwet\OneDrive\Desktop\cleaned_email_list.txt')
