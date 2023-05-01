import mysql.connector

class DB:
    def __init__(self):
        #connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='rahul',
                database='phones'
            )
            self.mycursor = self.conn.cursor()
            print('connection established')
        except:
            print('connection Error')
        # function for the smartphone name

    def phone_brand(self):
        brand_name=[]

        self.mycursor.execute("""
        select  distinct(brand_name) from smartphones  
        """)
        data = self.mycursor.fetchall()

        print(data)

        for item in data:
            brand_name.append(item[0])
        return brand_name

    def model_selection(self,option):
        models = []
        self.mycursor.execute("""
                SELECT model
                FROM smartphones
                WHERE brand_name = '{}'
               """.format(option))
        data1 = self.mycursor.fetchall()

        print(data1)
        for item in data1:
            models.append(item[0])
        return models

    def fetch_features(self,option,option1):
        features = {}
        self.mycursor.execute("""
                        SELECT *
                        FROM smartphones
                        WHERE brand_name = '{}'AND Model = '{}'
                       """.format(option, option1))
        data2 = self.mycursor.fetchall()
        print(data2)
        for item in data2:
            brand_name = item[0]
            model_name = item[1]
            model_data = {
                'price(in Rs)': item[2],
                'rating': item[3],
                'has_5g': item[4],
                'has_nfc': item[5],
                'has_ir_blaster': item[6],
                'processor_brand':item[7],
                'num_cores':item[8],
                'processor_speed':item[9],
                'battery_capacity(mAH)':item[10],
                'fast_charging_available':item[11],
                'fast_charging':item[12],
                'ram_capacity(GB)':item[13],
                'internal_memory(GB)':item[14],
                'screen_size(Inches)':item[15],
                'refresh_rate':item[16],
                'num_rear_cameras':item[17],
                'num_front_cameras':item[18],
                'os':item[19],
                'primary_camera_rear(MPx)':item[20],
                'primary_camera_front(MPx)':item[21],
                'extended_memory_available':item[22],
                'extended_upto':item[23],
                'resolution_width':item[24],
                'resolution_height':item[25]
                }
            features[model_name] = model_data

        return features





