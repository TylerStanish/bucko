create table profile (
    id serial primary key
    , email text unique not null
    , password text not null
);

create table auth_session (
    id serial primary key
    , profile_id int references profile(id) not null
    , token text unique not null
    -- for the sake of this little app, I'll leave expiration out.
    -- TODO but don't forget to double check if you change your mind.
    -- , expires timestamptz not null
);
