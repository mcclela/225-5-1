import sqlite3

# Database file path, ensure this matches the path used in your Flask application
DATABASE = '/nfs/demo.db'

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(DATABASE)

def clear_test_contacts():
    """Clear only the test contacts from the database."""
    db = connect_db()
    # Assuming all test contacts follow a specific naming pattern
    db.execute("DELETE FROM contacts WHERE name LIKE 'Test Name %'")
    db.commit()
    print('Test contacts have been deleted from the database.')
    db.close()

def delete_names_without_space():
    """Delete contacts where the name has no spaces."""
    db = connect_db()
    db.execute("DELETE FROM contacts WHERE name NOT LIKE '% %'")
    deleted = db.total_changes
    db.commit()
    print(f'Deleted {deleted} contacts with single-word names.')
    db.close()
    
if __name__ == '__main__':
    clear_test_contacts()
