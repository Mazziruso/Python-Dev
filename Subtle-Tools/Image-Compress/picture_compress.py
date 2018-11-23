from PIL import Image as Img
import os


def compress(info, pathc):
	for f_path in info['path']:
		# output file
		output = pathc + '\\Compress\\'
		if not os.path.isdir(output):
			os.mkdir(output, 744)
		# record the name of image
		name = f_path.split('\\')[-1]
		# open image
		image = Img.open(f_path)
		# save the image into the disks, whose quality is 40%
		image.save(output+'C_'+name, quality=40)


def get_files(file_dir):
	L = []
	for root, dirs, files in os.walk(file_dir):
		for file in files:
			if os.path.splitext(file)[1] == '.jpg':
				L.append(os.path.join(root, file))
	return L


# current path
path_current = os.getcwd()
# obtain the filename of all pictures
strs = get_files(path_current)
# construct the dict
infos = {'path': strs}
compress(infos, path_current)
