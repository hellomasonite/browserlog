"""A InstallCommand Command for Masonite Socialite."""
import os

from cleo import Command
from masonite.packages import create_controller, create_or_append_config


package_directory = os.path.dirname(os.path.realpath(__file__))


class InstallCommand(Command):
    """
    Publish Browserlog controller

    browserlog:install
    """

    def handle(self):
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
        shutil.copytree(module_path + "/../templates",
                os.getcwd() + "/resources/templates/browserlog")

        # Append route
        with open('routes/web.py', 'a') as f:
            f.write("\nGet('/logs', 'BrowserlogController@index') \n")
