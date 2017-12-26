import os
base_path = 'D:/workroom/'
gits = ['doc','study','ajaxxy','da_skin','workroom_paltform']
for file in gits:# 循环需要GIT的文件
	tmp_base_path = base_path+file
	GitAutoPush = tmp_base_path+"/GitAutoPush.bat"
	fp=open(GitAutoPush,'w')
	git_text = "D:\ncd "+os.path.normcase(tmp_base_path)+"\ngit add -A\ngit commit -m \"%date:~0,10%\"\ngit push"
	fp.write(git_text)
	fp.close()
	if os.access(GitAutoPush,os.F_OK):
		print(file+' Can be submitted automatically')
	else:
		print(file+' Can not be submitted automatically')
		fp = open(tmp_base_path+"/.gitignore",'a')
		fp.write('\r\n/GitAutoPush.bat')
		fp.close()
		#给最终执行文件增加
		fp = open("D:/workroom/每日一键GIT提交.bat",'a')
		text = os.path.normcase(GitAutoPush)
		fp.write(text+"\r\n")
		fp.close()
for file in gits:# git提交
	GitAutoPush = tmp_base_path+"/GitAutoPush.bat"
	print(GitAutoPush)
	os.system(GitAutoPush) 
print("Run successfully")
