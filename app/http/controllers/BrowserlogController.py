from os import listdir, remove

from masonite.view import View
from masonite.helpers import config
from masonite.request import Request
from masonite.response import Download
from browserlog.utils import parse_log
from masonite.controllers import Controller


class BrowserlogController(Controller):
    def index(self, view: View, request: Request):
        path = config('browserlog.BROWSERLOG_STORAGE_PATH')
        log_files = listdir(path)

        logs = []
        q = int(request.input('q', '0'))

        action = request.input('action')

        if action == 'clean':
            open('{0}/{1}'.format(path, log_files[q]), 'w').close()

        if action == 'download':
            return Download('{0}/{1}'.format(path, log_files[q]), name=log_files[q].split('.')[0], force=True)

        try:
            log_files[q]
        except IndexError:
            q = 0

        for line in open('{0}/{1}'.format(path, log_files[q]), 'r'):
            if parse_log(line):
                logs.append(parse_log(line))

        return view.render('browserlog/index.html', {'log_files': log_files, 'logs': logs, 'q': q})
