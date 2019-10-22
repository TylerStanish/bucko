Use `FLASK_ENV` environment variable to set which environment you want to be in. We will use the development database if `FLASK_ENV` is `development`, and the testing database if `FLASK_ENV` is `production`

Don't forget:
- Run migrations
  - Don't forget metacommands with `\i` must be relative to the db/ directory
- Set `PYTHONPATH` to the absolute path to where main.py lives
- Grep for `TODO`s and make sure they're done

TODO
- Auth
- Error handling (especially with schemas)

Notes:
- If you ever try to debug your tests, make sure to set your `PYTHONPATH` so imports work
