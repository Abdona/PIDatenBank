import psycopg2


  
  






def create_tables():
    commands = (
        """
        CREATE TABLE companies (
            company_id SERIAL PRIMARY KEY,
            company_name VARCHAR(255) NOT NULL,
            company_description VARCHAR(255) NOT NULL,
            company_email VARCHAR(320) NOT NULL
        )
        """,
        """ CREATE TABLE addresses (
                address_id SERIAL PRIMARY KEY,
                latitude DECIMAL (2,2),
                longitude DECIMAL (2,2),
                city VARCHAR(50) NOT NULL,
                address VARCHAR(255) NOT NULL
                )
        """,
        """ CREATE TABLE service_centers (
                service_center_id SERIAL PRIMARY KEY,
                grade_name VARCHAR(255) NOT NULL,
                companyID integer REFERENCES companies(company_id),
                addressID integer REFERENCES addresses(address_id)
                )
        """,
        """ CREATE TABLE categories (
                category_id SERIAL PRIMARY KEY,
                category_name VARCHAR(20) NOT NULL,
                service_centerID integer REFERENCES service_centers(service_center_id)
                )
        """,
        """ CREATE TABLE services (
                service_id SERIAL PRIMARY KEY,
                service_description VARCHAR(120) NOT NULL,
                categoryID integer REFERENCES categories(category_id),
                device VARCHAR(50),
                price decimal(2,1) NOT NULL
                )
        """,
        """
        CREATE TABLE users (
                user_id INTEGER PRIMARY KEY,
                first_name VARCHAR(25) NOT NULL,
                last_name VARCHAR(25) NOT NULL,
                email VARCHAR(25) NOT NULL
        )
        """,
        """
        CREATE TABLE review (
            review_id INTEGER PRIMARY KEY,
            review_text VARCHAR(50) NOT NULL,
            rating decimal(2,1) CONSTRAINT chk_rating CHECK (rating >= 0 AND rating <= 5),
            userID integer REFERENCES users(user_id),
            service_centerID integer REFERENCES service_centers(service_center_id)
        )
        """,
        """
        CREATE TABLE orders (
            userID integer REFERENCES users(user_id),
            service_centerID integer REFERENCES service_centers(service_center_id),
            serviceID integer REFERENCES services(service_id),
            price decimal(2,1) NOT NULL
        )
        """
        )
    conn = None
    try:
        conn = psycopg2.connect("host=127.16.5.15 dbname=postgres user=postgres password=test")
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
            conn.commit()
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
  
  





if __name__ == '__main__':
    create_tables()
