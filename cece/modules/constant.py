"""
See LICENSE file for copyright and license details.
"""

class AppProfile():
    """
        Profile to use for the app.
    """
    PERSONAL = 0
    ZIVLE = 1

class TaskFile():
    """
        Location of task files.
    """
    PERSONAL = '/home/rockwolf/Dropbox/vimwiki/todo.md'
    ZIVLE = '/home/rockwolf/Dropbox/vimwiki/todo.md'

class ReminderFile():
    """
        Location of reminder files.
    """
    PERSONAL = '/var/tmp/reminders.txt'
    ZIVLE = '/var/tmp/zivle_reminders.txt'
