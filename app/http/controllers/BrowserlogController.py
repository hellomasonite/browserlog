from os import listdir

from masonite.view import View
from masonite.helpers import config
from masonite.request import Request
from browserlog.utils import parse_log
from masonite.controllers import Controller


class BrowserlogController(Controller):
    def index(self, view: View, request: Request):
        path = config('browserlog.BROWSERLOG_STORAGE_PATH')
        log_files = listdir(path)

        logs = []
        q = int(request.input('q', '0'))

        try:
            log_files[q]
        except IndexError:
            q = 0

        for line in open('{0}/{1}'.format(path, log_files[q]), 'r'):
            if parse_log(line):
                logs.append(parse_log(line))

        return view.render('browserlog/index.html', {'log_files': log_files, 'logs': logs, 'q': q})
