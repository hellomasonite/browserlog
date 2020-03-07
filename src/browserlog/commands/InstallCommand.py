"""A InstallCommand Command for Masonite Socialite."""
import os

from cleo import Command
from masonite.packages import create_controller

package_directory = os.path.dirname(os.path.realpath(__file__))


class InstallCommand(Command):
    """
    Craft the socialite config file

    browserlog:install
    """

    def handle(self):
        create_controller(
            os.path.join(
                package_directory,
                '../controller/BrowserlogController.py'
            )
        )