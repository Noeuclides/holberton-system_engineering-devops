## Application server

0. Setting up a development environment, which is used for testing and debugging the code before deploying it to production.
1. Get the production application server set up with Gunicorn on web-01, port 5000. Installing Gunicorn. Flask application object will serve as a WSGI entry point into the application. This will be the production environment.
2. Configure Nginx to serve the page from the route /airbnb-onepage/
3. Adding another service for Gunicorn to handle. Configure Nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001