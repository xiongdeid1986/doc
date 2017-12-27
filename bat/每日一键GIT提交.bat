D:
cd d:\workroom\ajaxxy\
git add -A
git commit -m "%date:~0,10%%time:~0,8%"
git push
D:
cd d:\workroom\doc\
git add -A
git commit -m "%date:~0,10%%time:~0,8%"
git push
D:
cd d:\workroom\da_skin\
git add -A
git commit -m "%date:~0,10%%time:~0,8%"
git push
D:
cd d:\workroom\study\
git add -A
git commit -m "%date:~0,10%%time:~0,8%"
git push
D:
cd d:\workroom\workroom_paltform\
git add -A
git commit -m "%date:~0,10%%time:~0,8%"
git push
D:
cd d:\www_root\api.ddweb.com.cn\
mysqldump -uroot -proot cloud_ddweb > MysqlSql.sql
git add -A
git commit -m "%date:~0,10%%time:~0,8%"
git push
