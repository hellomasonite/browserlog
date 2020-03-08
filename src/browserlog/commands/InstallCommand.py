"""A InstallCommand Command for Masonite Socialite."""
import os
import shutil

from cleo import Command
from masonite.packages import create_controller, create_or_append_config, append_file


package_directory = os.path.dirname(os.path.realpath(__file__))


class InstallCommand(Command):
    """
    Install Browserlog

    browserlog:install
    """

    def handle(self):
        module_path = os.path.dirname(os.path.realpath(__file__))

        # Publish BrowserlogController
        create_controller(
            os.path.join(
                package_directory,
                '../controllers/BrowserlogController.py'
            )
        )

        # Publish Browserlog config file
        create_or_append_config(
            os.path.join(
                package_directory,
                '../config/browserlog.py'
            )
        )

        # Publish view
        config_directory = os.path.join(os.getcwd(), 'resources/templates/browserlog')

        if not os.path.exists(config_directory):
            os.makedirs(config_directory)

        shutil.copyfile(
            os.path.join(
                package_directory,
                '../templates/browserlog/index.html'
            ),
            config_directory + '/' + 'index.html')

        # Append route
        with open('routes/web.py', 'a') as f:
            f.write("\nROUTES += [ \n")
            f.write("    Get('/logs', 'BrowserlogController@index'),\n")
            f.write(']\n')
