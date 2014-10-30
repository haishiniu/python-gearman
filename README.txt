==============
python-gearman
==============

Description
===========
Python Gearman API - Client, worker, and admin client interfaces

For information on Gearman and a C-based Gearman server, see http://www.gearman.org/

Installation
============
* easy_install gearman
* pip install gearman

Links
=====
* 2.x source <http://github.com/Yelp/python-gearman/>
* 2.x documentation <http://packages.python.org/gearman/>

* 1.x source <http://github.com/samuel/python-gearman/>
* 1.x documentation <http://github.com/samuel/python-gearman/tree/master/docs/>

My fork
=======

Setting up a basic worker to grab task from gearman server.
Python code:
=================================================

gearman_server_list = [
  {
    'host' : 'locahost',
    'port' : 4730,
    'keepalive' : True,
    'keepidle' : 300,
    'keepintvl' : 60,
    'keepcnt' : 20
  },
  {
    'host' : 'locahost',
    'port' : 4731,
    'keepalive' : True,
    'keepidle' : 300,
    'keepintvl' : 60,
    'keepcnt' : 20,
  },
]

gm_worker = gearman.GearmanWorker(gearman_server_list)

# See gearman/job.py to see attributes on the GearmanJob
# Send back a reversed version of the 'data' string
def task_listener_reverse(gearman_worker, gearman_job):
    return reversed(gearman_job.data)

# gm_worker.set_client_id is optional
gm_worker.set_client_id('your_worker_client_id_name')
gm_worker.register_task('reverse', task_listener_reverse)

#You must set the argument 'do_grab=True' to launch the worker to grab tasks
#from servers

gm_worker.work(do_grab=True)
