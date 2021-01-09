Let's add another requirement:

room_name should start with ROOM_ and be longer than 8 chars

To begin let's add the associated tests.

Step 1 : 
I've created the function def verify_room_name(room_name)

Step 2 :
I've added a test for the new function verify_room_name

Step 3 :
I've removed the first test and added a fancier

Step 5 : 
I've coded the function verify_room_name





Let's add another requirement :

room_type should be public or private

Step 1 : 
I've created the fonction verify_room_type(room_type)

Step 2 :
I've created and added some tests to the function test_verify_room_type(self)

Step 3 :
I've coded the function verify_room_type





Let's add another requirement :

password should be longer than 8 chars, have at least 1 number and one special character ( ascii punctuation) 

Step 1 : 
I've created the function verify_password_length(password) that verify the password's length

Step 2 :
I've created and added some tests to the function test_verify_password_length(self)

Step 3 : 
I've created the function verify_password_number(password) that check if the password includes a number 

Step 4 :
I've created and added some tests to the function test_verify_password_number(self)

Step 5 : 
I've created the function verify_password_special(password) that check if the password includes a special character

Step 6 :
I've created and added some tests to the function test_verify_password_special(self)

Step 7 : 
I've created the function verify_password_total(password) that check if the password meet the 3 requirements by using the 3 function define earlier

Step 8 :
I've created and added some tests to the function test_verify_password_total(self)
At this stage there is 6 test and 4 fail because the function verify_password_* always return false.

Step 9 :
I've coded the function verify_password_length

Step 10 :
I've coded the function verify_password_number

Step 11:
I've coded the function verify_password_special

Step 12:
I've coded the function verify_password_total
Everytime we implemented a function we checked that the status from the test turned from False to True. At this stage its a 6/6 ok 






Let's add another requirement :
Creating a room that not meet the previous requirement should be impossible

Step 1 : 
I've created the fonction verify_add_room(db_path, room_name, room_type) that checks for a NameError Exception to be thrown

Step 2 :
I've created and added some tests to the function test_verify_add_room(self) :

Step 3 :
I've coded the function verify_add_room






Let's add another requirement :
Creating a user that not meet the previous requirement should be impossible

Step 1 : 
I've created the fonction verify_add_user that checks for a NameError Exception to be thrown

Step 2 :
I've created and added some tests to the function test_verify_add_user(self) :

Step 3 :
I've coded the function verify_add_user


Test are now 8/8 ok
All the requirement are now implemented if you use verify_add_user and verify_add_room to fill the database

extra-requirements-gruaux-raphanel
