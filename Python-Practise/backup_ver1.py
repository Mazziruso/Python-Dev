import os
import time

#source是指需要备份的文件夹内的所有文件或单个文件
source = ['"F:\\Python\\source"']

#target_dir是指备份压缩完成的压缩文件存放地址
target_dir = 'F:\\Python\\backup'

#备份文件压缩文件名
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#如果不存在备份文件存放文件夹或地址
if not os.path.exists(target_dir) :
	os.mkdir(target_dir)

#使用zip命令将需要备份的文件压缩打包
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))


print('Zip command is:')
print(zip_command)
print('Running:')

#如果zip命令执行了就返回成功，否则就返回失败
if os.system(zip_command) == 0 :
	print('Successful backup to',target)
else:
	print('Backup FAILED')