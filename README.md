# kollektivet
Website to organize houshold activities.

Originaly hosted localy on a Raspberry Pi

# run
- Install the python django module.
- Go to the kollektivet dir
- Run `python manage.py runserver 0.0.0.0:8000`
- Access the website using http://localhost:8000

# Washlist
Gives the ability to register the duration of a
wash to signal if the machine is occupied.

Also possible to enter a queue to be the next in line to wash.

The server can be set up with a mail (currently gmail) to mail
the user when the wash is done, and the next in queue.

![New wash](/readmeImages/newWash.PNG)
![Ongoing wash](/readmeImages/ongoingWash.PNG)
