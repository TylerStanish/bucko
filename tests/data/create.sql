insert into profile (id, email, password) values (1000000, 'blablabla@example.com', 'thehashedpassword');
insert into auth_session (profile_id, token) values (1000000, 'the_auth_session_token');
