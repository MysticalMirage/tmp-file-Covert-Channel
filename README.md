This project was a quick little covert channel example I created. It uses a shared directory in a linux directory, where the encoder creates files and uses the permissions settings (edited by chmod) to hide characters. The decoder then sees all the files, and decodes the message, stopping once a file has other execute permission, and deletes all of the temporary files.

To use, just edit in your message and shared folder path, then run using python3. For decode, edit in your shared folder path, and run using python3.
