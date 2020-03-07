from datetime import datetime

def parse_log(line):
    # line = "2020-03-07 10:40:40 - ERROR - SyntaxError in /Users/macbookpro/workspace/hellomasonite/packages/browserlog/bootstrap/start.py on line 38"
    line = line.split(' - ')

    date = line[0]
    level = line[1]
    level = level.lower()
    message = line[2]

    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    levels_classes = {
        'debug': 'info',
        'info': 'info',
        'notice': 'info',
        'warning': 'warning',
        'error': 'danger',
        'critical': 'danger',
        'alert': 'danger',
        'emergency': 'danger',
        'processed': 'info',
        'failed': 'warning',
    }

    level_class = levels_classes[level]

    return {
        'logged_at': date.strftime("%B %d %Y %H:%M:%S %p"),
        'level': level,
        'message': message,
        'level_class': level_class
    }