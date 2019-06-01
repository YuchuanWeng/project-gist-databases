from .models import Gist
import datetime

def search_gists(db_connection, **kwargs):
    
    query = 'SELECT * FROM gists'
    if not kwargs:
        cursor = db_connection.execute(query)
        return cursor.fetchall()
    else:
        if "created_at" in kwargs and "github_id" in kwargs:
            cursor = db_connection.execute("SELECT * FROM gists WHERE github_id = :github_id AND datetime(created_at) == datetime(:created_at)", kwargs)
        if "created_at" in kwargs:
            cursor = db_connection.execute("SELECT * FROM gists WHERE datetime(created_at) == datetime(:created_at)", kwargs)
        if "github_id" in kwargs:
            cursor = db_connection.execute("SELECT * FROM gists WHERE github_id = :github_id", kwargs)

        results = []
        for gist in cursor:
            results.append(Gist(gist))
        return results

