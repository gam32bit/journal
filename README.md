<h1>Python GUI to add journal entries to Postgres Database</h1>

- Before starting on the Python script, I created a database in Postgres. If anyone wants to use this code they will need to replace "yourpassword" with their password and also the username if it's different than postgres.
- Used Chat GPT to help write initial python script. Decided to use tkinter instead of Django or other web app language since I want to keep local. 
- First serious bug was a peer authentication issue which was solved by changing the pg_hba.conf file for postgres. Using the "SHOW config_file" in
postgres helped me locate it, and then I edited the local host setting from "peer" to "md5" 

  `TYPE  DATABASE        USER            ADDRESS                 METHOD`  
  
  `local   all             all                                     md5`
- Chat GPT recommended splitting the GUI class into two separate classes, one class for GUI and one class for interacting with the database.
- Originally tried a treewindow view for the retrieve entries function to keep everything in one window, but it ended up being too crowded, so I changed the retrieve function to create a new window instead. Also added text wrapping for better readability.
- I want to add a feature where I can move to the next text box by pushing Tab, which I should be able to do with the bind method in tkinter.
