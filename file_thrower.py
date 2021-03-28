import requests
import os


if __name__ == "__main__":
    print("File  thrower initialised!")
    url = "http://192.168.1.110:8080/save_file"
    file_source_path = "test_files"
    print("Sending files")
    counter = 0
    for file in os.listdir(file_source_path):
        print(f'Attempting to send {file} file')
        files = {"file": open(f"{file_source_path}/{file}", "rb")}
        res = requests.post(url, files=files)
        print("Sent!")
        os.remove(f"{file_source_path}/{file}")
        counter += 1
    print(f"Files send completed. Total {counter} files sent!")
    print("File thrower finished!")    
