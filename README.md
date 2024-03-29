&#x202E;

**Script Description: Converting JSON IDs to MongoDB ObjectId Format**

This Python script automates the process of converting IDs found in JSON files to the format of MongoDB ObjectId. It is designed to work with a directory containing multiple JSON files, processing each file individually.

**Features:**

**Automatic Conversion:** The script automatically detects and converts IDs in JSON files to the format expected by MongoDB ObjectId.

**Batch Processing:** It processes all JSON files in a specified directory, making it suitable for handling large numbers of files at once.

**UTF-8 Encoding:** The script ensures proper handling of non-ASCII characters, such as those found in languages like Arabic, by using UTF-8 encoding when reading and writing files.

**Usage:**

Specify the directory containing the JSON files to be processed by setting the directory variable.

Run the script, and it will iterate over all JSON files in the specified directory.

The script will convert IDs in each JSON file to the format of MongoDB ObjectId and overwrite the original files with the updated content.

Upon completion, a message indicating the successful processing of each file will be displayed, along with a final message indicating that all files have been processed.

**Note:**

Ensure that the JSON files in the directory are intended to be modified, as the script will overwrite the original files with the updated content.
