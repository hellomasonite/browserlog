from datetime import datetime

def get_level_class(level):
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

  return levels_classes[level]

def parse_log(line):
  try:
    line = line.split(' - ')
    date = line[0]
    level = line[1].lower()
    message = line[2]

    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    return {
        'logged_at': date.strftime("%B %d %Y %H:%M:%S %p"),
        'level': level,
        'message': message,
        'level_class': get_level_class(level)
    }

  except:
    return
