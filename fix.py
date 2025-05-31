import os
import subprocess

def sanitize_name(filename):
    # Replace spaces with underscores
    new_name = filename.replace(' ', '_')

    # Add .py extension if missing
    if not new_name.endswith('.py'):
        new_name += '.py'

    return new_name

# Get list of all files tracked by git
result = subprocess.run(['git', 'ls-files'], capture_output=True, text=True)
files = result.stdout.strip().split('\n')

for old_name in files:
    new_name = sanitize_name(old_name)
    if new_name != old_name:
        print(f'Renaming:\n  {old_name}\n-> {new_name}')
        subprocess.run(['git', 'mv', old_name, new_name])
