#member table
MemTab= ( """
       create table if not exists Members(
       username varchar(255) PRIMARY KEY,
       firstName varchar(255) NOT NULL,
       lastName varchar(255) UNIQUE,
       password varchar(255) NOT NULL)
       """
)

#resort table
ResTab = ( """
       create table if not exists Resorts(
       name varchar(255) PRIMARY KEY,
       location varchar(255) NOT NULL,
       price int NOT NULL,
       description varchar(690),
       facilities varchar(420))
       """
)
#booking table
BookTab = ( """
       create table if not exists Booking(
       resort_name varchar(255) PRIMARY KEY,
       username varchar(255) UNIQUE NOT NULL,
       start_date date NOT NULL,
       end_date date,
       occupants int DEFAULT 1,
       cost int NOT NULL,)
       """
)

#passwords table

PassTab = ("""
        create table if not exists Passwords(
        username varchar(255),
        Password varchar(255)
        
        """
)