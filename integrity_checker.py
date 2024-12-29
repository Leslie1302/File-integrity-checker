import hashlib
import os
from time import sleep, strftime
from getpass import getuser

def calculate_file_hash(filepath):
    """Calculate the SHA512 hash of a file"""
    hash_sha512 = hashlib.sha512()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha512.update(chunk)
        return hash_sha512.hexdigest()
##This function calculates the SHA512 hash of a file, providing a unique digital fingerprint. If the file changes, so does this hash, allowing us to detect alterations.

def erase_baseline_if_already_exists():
    """Delete baseline.txt if it exists"""
    if os.path.exists('baseline.txt'):
        os.remove('baseline.txt')
##Before collecting a new baseline, we ensure any existing baseline file is deleted to avoid mixing old data with new. This erases any existing baseline text file

def collect_new_baseline():
    """Collect a new baseline of file hashes, ignoring certain file types."""
    erase_baseline_if_already_exists()
    files_directory = './Files'
    if not os.path.exists(files_directory):
        os.makedirs(files_directory)
    files = [f for f in os.listdir(files_directory) if os.path.isfile(os.path.join(files_directory, f)) and not f.startswith('.')]
    with open('baseline.txt', 'a') as baseline_file:
        for f in files:
            file_path = os.path.join(files_directory, f)
            file_hash = calculate_file_hash(file_path)
            baseline_file.write(f"{file_path}|{file_hash}\n")

##Here, we gather a baseline of our files’ hashes. We ignore hidden files (those starting with .) and write each file's path and hash to baseline.txt.

def begin_monitoring():
    """Monitor files for changes, deletions, and new copies based on saved baseline, including detailed audit logs."""
    ##(Implementation details are skipped for brevity. Please refer to the full code for specifics.)

def main():
    print("\nWhat would you like to do?\n")
    print("     A) collect new Baseline? ")
    print("     B) Begin monitoring files with saved Baseline?\n")
    response = input("Please enter 'A' or 'B': ").upper()

    if response == 'A':
        collect_new_baseline()
    elif response == 'B':
        begin_monitoring()

main()