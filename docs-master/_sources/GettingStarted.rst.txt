.. _Getting Started:

***************
Getting Started
***************

Here is a quick guide to getting WOFpy up and running.

Installation
============

Follow the steps below to install WOFpy and its prerequisites on a Windows
computer.

#. Install **Python 2.7**.  The 32-bit installer is recommended.
#. Add the **Python** folder to your **Path** environment variable.
#. Install **setuptools**. This allows the setup script to be run.
#. Add the **Python/scripts** folder to your **Path** environment variable.
#. Open a command window (run cmd), navigate to the WOFpy folder (with setup.py
   in it), and enter this command: ``python setup.py install``


The wof package (in the subfolder named **wof**) is now accessible from any
directory.

    If you edit code in the **wof** folder, you may need to run setup.py again
    to apply the changes to your system.

Database Support
================
You may need to install additional components to connect to your database.
* sqlalhchemy
* pydobc (for ODM1_1 using sqlserver and ODM2)
* msqldb (for ODM1_1 using mysql)
* ODM2API (for ODM2 example)
* other database drivers: postgres, sqllite, mysql.


PIP Installs
============
TBD: ONCE a Package is created and packaged.
``pip install WofPy``

If you are using ODM, or ODM2, then you need to run the extras (ODM1, or ODM2)
``pip install WofPy -e .[ODM2]``


.. _examples:

Running the Examples
====================

Example services are included with WOFpy.  Each example consists of data, Data
Access Objects (DAOs), models, and the service definition.  The examples are
located in the **examples** folder.

The general procedure for each example is to set up any required data
connections, use Python to run the runserver.py script, and test the service
using a Web browser or other client application.  The script should print
service endpoint URIs in the window used to execute the script.

When testing is complete, you should stop the service.  For example, if you
started the service using a command window in Windows, you can stop the service
by pressing ``CTRL+C`` in the command window.

.. note::
    These examples are run in debug mode for demonstration purposes.  In a
    production environment, you would use something like IIS or Apache to
    manage the service.

The examples are described in more detail below.

.. _barebones-example:

Barebones SQLite Example
------------------------

This example is located in the **examples/flask/barebones** folder.

This example shows how to access a very simple SQLite database located in the
**LCM_Data** subfolder.  The database only has three tables in it: one for
sites, one for variables, and one for data values.  The remaining information
required for WaterML is read from a config file.

Follow the steps below to run this example.

#. In the **examples/flask/barebones** folder, edit the value of the **openPort**
   variable in **runserver_LCM.py** to match an open port on your computer,
   if necessary.  Then save and close the file. 
#. Open a command window in the **examples/flask/barebones** folder and enter:
   ``python runserver_LCM.py``
#. In your command window you should see a message indicating that the service
   is running along with instructions for accessing the service.  

Comma Delimited File Example
----------------------------

This example is located in the **examples/flask/csv_server** folder.

This example shows how to access data from comma delimited (CSV) files in the 
**csv** subfolder.  One CSV file contains the time series values, while
another contains descriptions of observations sites.  

Follow the steps below to run this example.

#. In the **examples/flask/csv_server** folder,  **runserver_csv.py**   Then save and close the file.
#. Open a command window in the **examples/flask/csv_server** folder and enter:
   ``python runserver_csv.py``
#. In your command window you should see a message indicating that the service
   is running along with instructions for accessing the service.  

.. _swis-example:

SWIS SQLite Example
-------------------

This example is located in the **examples/flask/swis** folder.

This example shows how to access a more complicated SQLite database based on
early designs of the Texas Water Development Board's Surface Water Information
System (SWIS) database.

Follow the steps below to run this example.

#. In the **examples/flask/swis** folder **runserver_swis.py** t
#. Open a command window in the **examples/flask/swis** folder and enter:
   ``python runserver_swis.py``
#. In your command window you should see a message indicating that the service
   is running along with instructions for accessing the service.  

ODM 1.1 SQL Server Example
--------------------------

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
   database connection string for the Little Bear River database, e.g. in a file ending in .connection (eg private.connection or lbr.connection),
   'mssql+pyodbc://webservice:webservice@localhost/LittleBear11?driver=SQL+Server+Native+Client+10.0'``
#. In the **examples/flask/odm_1_1** folder, edit the value of the **openPort**
   variable in **runserver_odm_1_1.py** to match an open port on your computer,
   if necessary.  Then save and close the file.
#. Open a command window in the **examples/flask/odm_1_1** folder and enter:

.. code:: bash

    python runserver_odm_1_1.py
    --config=lbr_config.cfg
    --connection=lbr.connection

#. In your command window you should see a message indicating that the service
   is running along with instructions for accessing the service.

   ODM1Services

ODM 2 SQL Server Example
------------------------

This example is located in the **examples/flask/odm2** folder.

These examples show how to access Observations Data Model (ODM2) databases in PostgreSQL/Mysql Server.
The example for ODM2 measurement data uses the Marchantaria Time Series ODM2 PostgreSQL database from the ODM2 github at https://github.com/ODM2/ODM2/tree/master/usecases/marchantariats.
And the example for ODM2 timeseries uses Little Bear River Test ODM2 Mysql Database from ODM2 github at https://github.com/ODM2/ODM2/tree/master/usecases/littlebearriver/sampledatabases.

Follow the steps below to run this example.

#. Install PostgreSQL or Mysql Server based on the data use cases.
#. Download ODM2 database from the ODM2 github at above URLs.
#. Download the ODM2API (https://github.com/ODM2/ODM2PythonAPI/tree/setup). At **src** folder, enter this command: ``python setup.py install``.
#. Determine the database connection string. **odm2_connection_string** set to a SQLAlchemy-compatible
   database connection string for the ODM2 database, e.g.,
   'postgresql+psycopg2://username:passowkr@hostname:port/db_name' or, 'mysql+mysqldb://username:password/db_name'
#. In the **examples/flask/odm2/{measurement|timeseries}** folder, edit the value of the **openPort**
   variable in **runserver_multiple.py|runserver_odm2_measurement.py|runserver_odm2_timeseries.py** to match an open port on your computer,

   ODM2Services

CBI External Service Example
----------------------------

This example is located in the **examples/flask/cbi** folder.

This example shows how to access a Web service provided by the Conrad Blucher
Institute (CBI) for the Texas Coastal Ocean Observation Network (TCOON).
TCOON is a live network with new values continuously pouring in from sensors
along the Texas coast.  Data access is provided by a variant of the OGC's
Sensor Observation Service (SOS).  We will provide access to the data with
a WaterOneFlow service by wrapping the TCOON SOS service with our data access
object (DAO) and supporting modules.  Because site and variable descriptions
do not change frequently in TCOON, we store that information in a local SQLite
database.  The result is a Web service that uses both a SQLite database and
another Web service to provide data to the client.  Of course, the client has
no idea that this is happening.  All the client cares about is that we provide
access using a standard WaterOneFlow service and send responses back in WaterML
format!

This example requires an internet connection to access the TCOON Web service.
To prepare your service, you will make a cache of sites and variables available
from TCOON.  Then you will run the service.

Follow the steps below to run this example.

#. Open a command window in the **examples/flask/cbi** folder and enter:
   ``python build_cbi_cache.py``
#. In the command window, enter:
   ``python runserver_cbi.py``
#. In your command window you should see a message indicating that the service
   is running along with instructions for accessing the service.  

Multiple Services Example
-------------------------

This example is located in the **examples/flask/** folder.

This folder contains a **runserver_multiple.py** script demonstrating how to
run multiple services at once.  It uses the
:ref:`barebones <barebones-example>` and :ref:`SWIS <swis-example>` examples.
Follow the steps below to run this example.

#. In the **examples/flask/** folder, edit the value of the **openPort**
   variable in **runserver_multiple.py** to match an open port on your computer,
   if necessary.  Then save and close the file. 
#. Open a command window in the **examples** folder and enter:
   ``python runserver_multiple.py``
#. In your command window you should see a message indicating that the service
   is running along with instructions for accessing the service.

.. include:: AccessingService.rst

