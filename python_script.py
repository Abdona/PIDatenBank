from cmath import acos, cos, sin
from math import radians
from tkinter import Y
from bcrypt import re
import psycopg2

def db_interact(request):
    string_to_return = ""
    conn = None
    try:
        conn = psycopg2.connect("host=172.16.5.10 dbname=postgres user=postgres password=test")
        cur = conn.cursor()
        if "cheapest" or "cheap" and "for my" in request:
            cur.execute(
                """ 
                SELECT * FROM public.appointments_devices
                 
                """
            )
            mobile_records = cur.fetchall()
            print(mobile_records)
            if any(x for request in mobile_records for x in request if isinstance(x, str)):
                deviceID= next(x[0] for item in request.split(" ") for x in mobile_records if x[1] == item)##FIND THE CHEAPEST SERVICE
                print(deviceID)
                command = f"""
                            SELECT * FROM public.appointments_devices WHERE "device_id" = '{deviceID}';  
                            """
                string_to_return += f"executing following command: {command} \n"
                cur.execute(command)
                mobile_records2 = cur.fetchall()
                for row in mobile_records2:
                    string_to_return +=(f"Id = {row[0]} \n")
                    string_to_return +=(f"Name = {row[1]}")
        elif "nearest" or "near" in request:
            findAress = """
                SELECT address FROM addresses WHERE acos(
                               sin(radians(53.499809325094326)) 
                                 * sin(radians(latitude)) 
                               + cos(radians(53.499809325094326)) 
                                 * cos(radians(latitude)) 
                                 * cos( radians(10.002976557845734)
                                   - radians(longitude))
                               ) * 6371 <= 20;
            """
            cur.execute(findAress)
            mobile_records3 = cur.fetchall()
            string_to_return+=f"executing following command:\n '{findAress}' \n resultes:{mobile_records3}"
        else:
            string_to_return += "nothing is found"
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print(string_to_return)
    return string_to_return
  
  





if __name__ == '__main__':
    db_interact("I'm at least the cheapest for my iphone")