import os
import shutil

def create_view(location, to='resources/templates/browserlog'):
    file_name = os.path.basename(location)

    view_directory = os.path.join(os.getcwd(), to)
    view_file = os.path.join(view_directory, file_name)
    if not os.path.exists(view_directory):
        # Create the path to the model if it does not exist
        os.makedirs(view_directory)

    if os.path.isfile(view_file):
        # if file does exist
        print('\033[91m{0} File Already Exists!\033[0m'.format(file_name))
    else:
        # copy file over
        shutil.copyfile(
            location,
            view_file
        )

        print('\033[92m{0} File Created\033[0m'.format(file_name))