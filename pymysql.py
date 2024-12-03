import pymysql
db = pymysql.connect(host='localhost',database = 'student',user='root',password='Devendra@26',port=3306)
cur = db.cursor()
i=1
n=int(input("enter no.of records"))
while i<=n:
    emid = int(input("enter emp id"))
    empname = input("enter name")
    sal = int(input("enter salary"))
    sql = ("insert into emp(emid,empname,sal) values('%d','%s','%d')" %(emid,empname,sal,))
    cur.execute(sql)
    i = i + 1
# output =
# enter no.of records 1
# enter emp id 525
# enter name Dev
# enter salary 10000
# its sucessfully stored in database
