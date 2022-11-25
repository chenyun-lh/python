import pymysql
import json
conn = pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="abc123",
                       database="stock_db",
                       charset="utf8")

# 获取游标
cursor = conn.cursor()
# 查询sql语句
sql = '''select i.code, i.short, i.chg, 
            i.turnover, i.price, i.highs, f.note_info 
            from info as i inner join focus as f on i.id = f.info_id;'''
# 执行sql
cursor.execute(sql)
# 获取结果集
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 关闭数据库连接
conn.close()
# 个人中心数据列表
center_data_list = list()
# 遍历每一行数据转成字典
for row in result:
    # 创建空的字典
    center_dict = dict()
    center_dict["code"] = row[0]
    center_dict["short"] = row[1]
    center_dict["chg"] = row[2]
    center_dict["turnover"] = row[3]
    center_dict["price"] = str(row[4])
    center_dict["highs"] = str(row[5])
    center_dict["note_info"] = row[6]
    # 添加每个字典信息
    center_data_list.append(center_dict)

    print(center_data_list)

center_data_list = json.dumps(center_data_list,ensure_ascii=False)
print(type(center_data_list))
print(center_data_list)

