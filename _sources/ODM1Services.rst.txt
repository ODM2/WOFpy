***************
ODM1 SQL Server
***************
A single service can be run from the command line.

    ``python examples/flask/odm_1_1/runserver_odm_1_1.py
    --config=lbr_config.cfg
    --connection=connection.file``

connection.file contains:

``postgresql+psycopg2://username:password/db_name``

``mysql+mysqldb://username:password/db_name``

Detailed Instructions
---------------------
This example is located in the **examples/flask/odm_1_1** folder.

This example shows how to access CUAHSI Observations Data Model (ODM) databases
in Microsoft SQL Server.  The example uses the Little Bear River ODM 1.1
example database from the HIS website at
http://his.cuahsi.org/odmdatabases.html.

Follow the steps below to run this example.

#. Install Microsoft SQL Server.  You can download the free version, SQL
   Express.
#. Download the Little Bear River ODM 1.1 database from the HIS website.
#. Attach the database to SQL Server.
#. Grant a SQL Server account **select** privileges on the database.  WOFpy
   will use this account to connect to the database.
#. Determine the database connection string. **lbr_connection_string** set to a SQLAlchemy-compatible
   database connection string for the Little Bear River database, e.g.,
   'mssql+pyodbc://webservice:webservice@localhost/LittleBear11?driver=SQL+Server+Native+Client+10.0'``
#. In the **examples/flask/odm_1_1** folder, edit the value of the **openPort**
   variable in **runserver_odm_1_1.py** to match an open port on your computer,
   if necessary.  Then save and close the file.
#. Open a command window in the **examples/odm_1_1** folder and enter:

..code:: bash

    python runserver_odm11.py
    --config=lbr_config.cfg
    --connection=connection.file

#. In your command window you should see a message indicating that the service
   is running along with instructions for accessing the service.