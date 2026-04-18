from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.sale import Sale


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllRetailers():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM go_retailers")
        result = [Retailer(**row)
                  for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllRetails():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM go_retails 
                
            """
        cursor.execute(query, )
        result = [Retailer(**row)
                  for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllAnni():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        # Query con COALESCE: se il parametro è None, SQL usa il valore della colonna stessa
        query = """
                        SELECT DISTINCT YEAR(Date)
                        FROM go_daily_sales
                    """
        cursor.execute(query)
        result=[]
        for row in cursor.fetchall():
            result.append(row['YEAR(Date)'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllBrands():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        # Query con COALESCE: se il parametro è None, SQL usa il valore della colonna stessa
        query = """
                            SELECT DISTINCT Product_brand
                            FROM go_products
                        """
        cursor.execute(query, )
        result = []
        for row in cursor.fetchall():
            result.append(row['Product_brand'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTopVendite(anno, brand, retail):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
         SELECT s.*, (s.Unit_sale_price * s.Quantity) AS Ricavo
            FROM go_daily_sales s
            JOIN go_products p ON p.Product_number = s.Product_number
            WHERE YEAR(s.Date) = COALESCE(%s, YEAR(s.Date))
              AND p.Product_brand = COALESCE(%s, p.Product_brand)
              AND s.Retailer_code = COALESCE(%s, s.Retailer_code)
            ORDER BY Ricavo DESC
            LIMIT 5 
                                """
        cursor.execute(query, (anno,brand,retail) )
        result = []
        for row in cursor.fetchall():
            result.append(Sale(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAnalizza(anno,brand, retail):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        query = """
                SELECT 
                SUM(s.Unit_sale_price * s.Quantity) AS GiroAffari,
                    COUNT(*) AS NumVendite,
                    COUNT(DISTINCT s.Retailer_code) AS NumRetailers,
                    COUNT(DISTINCT s.Product_number) AS NumProdotti
                FROM go_daily_sales s
                JOIN go_products p ON p.Product_number = s.Product_number
                WHERE YEAR(s.Date) = COALESCE(%s, YEAR(s.Date))
                  AND p.Product_brand = COALESCE(%s, p.Product_brand)
                  AND s.Retailer_code = COALESCE(%s, s.Retailer_code)
                    
                                        """
        cursor.execute(query, (anno, brand, retail))
        result= cursor.fetchone()
        print(result)
        cursor.close()
        conn.close()
        return result
