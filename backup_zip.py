import os
import time

source = ['"D:\\world"']
target_dir = 'D:\\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comments = input("Enter a comment --->")
if len(comments) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comments.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup Failed')
