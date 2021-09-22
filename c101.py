import dropbox 
class TransferData: 
    def __init__(self, access_token): 
      self.access_token = access_token 
    def upload_file(self, file_from, file_to):
         """upload a file to Dropbox using API v2 """ 
         dbx = dropbox.Dropbox(self.access_token) 
         with open(file_from, 'rb') as f: 
             dbx.files_upload(f.read(), file_to) 
def main(): 
    access_token = 'sl.A4iJBbPASxlKb9jBkkhF52GxOKoy3N7tVIqoHS7c20f29WptXyfgcPlDFP8bu848i1j6EbLTdhrMUvMVz3edXNXo2ASRndrpLBvXwFGk7NKe7JGZjftWzmj1GY7jxuaAz9sDHiU' 
    transferData = TransferData(access_token) 
    file_from = input('enter the file path to transafer') 
    file_to = input('enter the full path to upload') 
    # API v2 
    transferData.upload_file(file_from, file_to) 
if __name__ == '__main__': 
    main()
