<h1>Python GUI to add journal entries to Postgres Database</h1>

- Used Chat GPT to help write initial python script. Decided to use tkinter instead of Django or other web app language since I want to keep local. 
- First serious bug was a peer authentication issue which was solved by changing the pg_hba.conf file for postgres. Using the "SHOW config_file" in
postgres helped me locate it, and then I edited the local host setting from "peer" to "md5" 

  `TYPE  DATABASE        USER            ADDRESS                 METHOD`  
  
  `local   all             all                                     md5`
