import psycopg2

def db_interact():
    string_to_return = ""
    commands = (
        """
        SELECT * FROM public.appointments_servicecenter 
        """,)
    conn = None
    try:
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=7741domkRAT.")
        cur = conn.cursor()
        for command in commands:
            string_to_return += f"executing following command: {command}"
            cur.execute(command)
            mobile_records = cur.fetchall()

            for row in mobile_records:
                string_to_return +=("Id = ", row[0])
                string_to_return +=("Name = ", row[1])
                print(string_to_return)
                # print("Model = ", row[1])
                # print("Price  = ", row[2], "\n")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print(string_to_return)
    print(string_to_return)
    return string_to_return
  
  





if __name__ == '__main__':
    db_interact()