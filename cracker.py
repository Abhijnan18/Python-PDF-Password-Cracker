import PyPDF2


class PDFPasswordCracker:
    def __init__(self, pdf_path, password_list_path):
        self.pdf_path = pdf_path
        self.pdf_reader = PyPDF2.PdfReader(open(pdf_path, "rb"))
        if not self.pdf_reader.is_encrypted:
            print("PDF is not encrypted.")
            return

        # Load passwords from file
        with open(password_list_path, 'r', encoding='utf-8') as f:
            self.dictionary = [line.strip() for line in f.readlines()]

    def crack_password(self):
        for password in self.dictionary:
            try:
                if self.pdf_reader.decrypt(password) == 1:
                    print(f"Password found: {password}")
                    return True
            except Exception as e:
                print(f"Error while trying password '{password}': {str(e)}")

        print("Password not found in the dictionary.")
        return False


# Example usage:
if __name__ == "__main__":
    pdf_file = "encrypted.pdf"  # Replace with your encrypted PDF file path
    # Replace with the path to your password list file
    # password_list_file = "10k-most-common.txt"
    password_list_file = "psswd.txt"
    cracker = PDFPasswordCracker(pdf_file, password_list_file)
    cracker.crack_password()
