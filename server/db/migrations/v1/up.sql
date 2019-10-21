create table profile (
    id serial primary key,
    email text not null,
    hashed_password not null
);
