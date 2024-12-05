# database_query.py
import mysql.connector
from config import DB_CONFIG

def query_phone_addresses(phone_number: str) -> list:
    """执行 MySQL 查询以获取该手机号码的姓名信息"""
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )
        cursor = connection.cursor()
        query = """
        SELECT Id, Name
        FROM `User`.`MemberDetail`
        WHERE MemberId IN (SELECT Id FROM Member WHERE Phone = %s)
        AND deleteAt = 0
        """
        cursor.execute(query, (phone_number,))
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    except mysql.connector.Error as e:
        print(f"数据库查询失败: {e}")
        return []
