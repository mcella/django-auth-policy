#!/usr/bin/env python
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "testsite.settings"

    from django.core import management
    import django
    django.setup()

    management.call_command('test', 'testsite.tests', verbosity=1,
                            interactive=False)
