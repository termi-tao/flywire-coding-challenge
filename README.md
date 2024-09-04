# Implementation Documentation
The challenge is fully completed and the acceptance criteria is met. This documentation provides a brief introduction of reviewing this challenge to optimize the experience. Meanwhile, the design mindset will also be briefly covered.

### Configuration
The admin page and list course API is good to go without any configuration. To streamline your review process, it's recommended to follow the below steps to set up the database as well as creating some mock data.
 1. Run `docker compose up -d` to bring up the server.
 2. Then run `docker compose exec django bash` to access the container's cli and run `python manage.py migrate` to create a database.
 3. [Optional] Run `python manage.py seed` to create mock courses and intakes. Alternatively, you can also create them on the admin site interface.
 4. Create a super user for later testing steps by running `python manage.py createsuperuser`. It will ask you to for a username, email, and password.

### Admin Site Interface
The admin site interface supports an admin to view/manage courses and intakes. A ***search menu*** and ***filter bar*** are provided on Courses/Intakes page to reduce the complexity of finding specific entities. Good UX, happy users!

***Courses Page***
The courses page shows the below attributes of courses:
 - Course name
 - Intakes - represented by start dates and they are embedded into a comma separated string. By clicking on each intake will redirect you to the ***intake*** change page.
 - ***View***/***Delete*** buttons

***Intakes Page***
The intakes page shows the below attributes of intakes:
 - Relevant course of an intake which redirect admin to course detail page
 - Start date and end date
 - ***View***/***Delete*** buttons

### REST API
You are welcome to import the Postman collection that I've attached in the responding email as a kickstart of the API testing process. This collection has two requests to the ***authentication*** and ***list_courses*** endpoints.

Note: I have set up a pre-request script that acquires token before sending out the GET ***list_courses*** request. You should replace it with your own credentials (admin username and password that you created earlier) instead in the beginning of the script.

For the time being, the ***list_courses*** endpoint returns all the courses and their intakes. Ideally, there should be pagination and filtering (e.g. exclude courses without intakes) implemented depending on the requirements.

As the authentication endpoint, having ***access control levels*** is needed in later implementation too to improve system security.

### Unit tests
This is system is proudly implemented based on Test Driven Development principle, all the core modules have 100% unit test coverage and overall 96% coverage for the whole project (per [Python Coverage](https://coverage.readthedocs.io/en/7.6.1/)). I have made a minor directory restructuring for keeping a neat project structure, now you may find these tests in `apps/admission/tests` and `apps/api/tests` folders. A test fixture file `apps/fixtures/api_test_data.json` was also created for mocking purpose.
To test, simply run `docker  compose  run  --rm  django  pytest`.
