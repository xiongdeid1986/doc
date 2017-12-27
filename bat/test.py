import os
import json
import datetime
#执行bat文件的路径
autoBat = "D:\\workroom\\doc\\bat\\每日一键GIT提交.bat"
#需要git提交的项目
Projects = {\
	"ajaxxy":{\
		"path":"D:\\workroom\\ajaxxy\\",\
		"remote":""\
	},
	"doc":{\
		"path":"D:\\workroom\\doc\\",\
		"remote":""\
	},
	"da_skin":{\
		"path":"D:\\workroom\\da_skin\\",\
		"remote":""\
	},
	"study":{\
		"path":"D:\\workroom\\study\\",\
		"remote":""\
	},
	"workroom_paltform":{\
		"path":"D:\\workroom\\workroom_paltform\\",\
		"remote":""\
	},
	"ddweb":{\
		"path":"D:\\www_root\\api.ddweb.com.cn\\",\
		"remote":""\
	}
}
cmd = ""
for j in Projects:
	_j = Projects[j]
	path = _j["path"]
	remote = _j["remote"]
	disk = path[0:2]
	cmd += disk+"\n"+"cd "+os.path.normcase(path)+"\ngit add -A\ngit commit -m \"%date:~0,10%\"\ngit push\n"
	print(disk)
	print(path)
	print(remote)
fs = open(autoBat,'w')
fs.write(cmd)
fs.close()
print(cmd)