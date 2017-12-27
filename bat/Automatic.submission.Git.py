import os
import json
import datetime
#执行bat文件的路径
autoBat = "D:\\workroom\\doc\\bat\\每日一键GIT提交.bat"
#需要git提交的项目
Projects = {\
	"ajaxxy":{\
		"path":"D:\\workroom\\ajaxxy\\",\
		"data_base_type":"mysql",\
		"data_base_name":"",\
		"data_base_user":"root",\
		"data_base_pwd":"root",\
		"remote":""\
	},
	"doc":{\
		"path":"D:\\workroom\\doc\\",\
		"data_base_name":"",\
		"data_base_user":"root",\
		"data_base_pwd":"root",\
		"remote":""\
	},
	"da_skin":{\
		"path":"D:\\workroom\\da_skin\\",\
		"data_base_name":"",\
		"data_base_user":"root",\
		"data_base_pwd":"root",\
		"remote":""\
	},
	"study":{\
		"path":"D:\\workroom\\study\\",\
		"data_base_name":"",\
		"data_base_user":"root",\
		"data_base_pwd":"root",\
		"remote":""\
	},
	"workroom_paltform":{\
		"path":"D:\\workroom\\workroom_paltform\\",\
		"data_base_name":"",\
		"data_base_user":"root",\
		"data_base_pwd":"root",\
		"remote":""\
	},
	"ddweb":{\
		"path":"D:\\www_root\\api.ddweb.com.cn\\",\
		"data_base_name":"cloud_ddweb",\
		"data_base_user":"root",\
		"data_base_pwd":"root",\
		"remote":""\
	}
}
cmd = ""
for j in Projects:
	_j = Projects[j]
	path = _j["path"]
	remote = _j["remote"]
	disk = path[0:2]
	data_dump_cmd = ""
	if(_j["data_base_name"]):
		data_dump_cmd = "mysqldump -u"+_j["data_base_user"]+" -p"+_j["data_base_pwd"]+" "+_j["data_base_name"]+" > MysqlSql.sql\n"
	cmd += disk+"\n"+"cd "+os.path.normcase(path)+"\n"+data_dump_cmd+"git add -A\ngit commit -m \"%date:~0,10%%time:~0,8%\"\ngit push\n"
	print(j+' create successer!')
fs = open(autoBat,'w')
fs.write(cmd)
fs.close()
os.system(autoBat)