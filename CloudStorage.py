import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        print("Successfully connected to dropbox account!!!")

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode = WriteMode('overwrite'))

def main():
    access_token = 'nT0QDyThNTcAAAAAAAAAAQhpXvwjnPaAhvUZS2VGBxBcUr8636p6AuenxKfO_amY'
    transferData = TransferData(access_token)

    file_from = input("Enter the file you want to upload")
    file_to = input("Enter the file location in the dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)


main()
