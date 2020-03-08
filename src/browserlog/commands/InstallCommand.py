"""A InstallCommand Command for Masonite Socialite."""
import os
import shutil

from cleo import Command
from masonite.packages import create_controller, create_or_append_config


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
        shutil.copyfile(module_path + "/../templates/browserlog.html",
                os.getcwd() + "/resources/templates/browserlog.html")

        # Append route
        with open('routes/web.py', 'a') as f:
            f.write("\nROUTES += [ \n")
            f.write("    Get('/logs', 'BrowserlogController@index'),\n")
            f.write(']\n')
