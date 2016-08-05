#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_proj.base_settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
