File Integrity Checker
Overview

The File Integrity Checker is a Python script designed to monitor and verify the integrity of files in a specific directory by calculating and comparing their SHA512 hashes. The script helps detect unauthorized changes, deletions, or additions to files, providing a way to ensure that critical files remain unchanged over time.
Features

    Create a Baseline: Generate a snapshot of file hashes and store them in a baseline.txt file.
    Monitor File Integrity: Compare current files' hashes with the baseline to detect changes, deletions, or additions.
    Audit Logging: Keep track of any discrepancies detected during the monitoring phase (detailed monitoring is a work-in-progress).

Functions
1. calculate_file_hash(filepath)

    Calculates the SHA512 hash of a given file, providing a unique fingerprint for each file.
    Useful for verifying the integrity of files by comparing their hashes over time.

2. erase_baseline_if_already_exists()

    Deletes the existing baseline.txt file (if any) to avoid mixing old data with new when generating a fresh baseline.

3. collect_new_baseline()

    Collects a new baseline of file hashes in the Files directory.
    Ignores hidden files and writes the file paths and their corresponding hashes to baseline.txt.

4. begin_monitoring()

    Monitors files for changes, deletions, or additions based on the saved baseline.
    (Detailed implementation for monitoring is not fully included yet.)

5. main()

    The script's entry point, which prompts the user to either:
        A) Collect a new baseline of file hashes.
        B) Begin monitoring files based on an existing baseline.

Usage

    Create a New Baseline:
        Run the script and choose option A to collect the current file hashes from the Files directory.
    Monitor File Integrity:
        After the baseline has been created, run the script and choose option B to begin monitoring files for changes.

Requirements

    Python 3.x
    No additional libraries required.
