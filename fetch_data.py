import sqlite3
import json

# connect to db
def connect_to_database(db_path):
    conn = sqlite3.connect(db_path)
    return conn

# get all corses
def fetch_all_courses(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses')
    return cursor.fetchall()

# get spe corse 
def fetch_course_details(conn, course_code):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM courses WHERE course_code = ?', (course_code,))
    return cursor.fetchone()

# get some spe corse 's all meeting time 
def fetch_meeting_sections(conn, course_code):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM meeting_sections WHERE course_code = ?', (course_code,))
    return cursor.fetchall()

def main():
    db_path = 'courses.db'
    conn = connect_to_database(db_path)
    
    """courses = fetch_all_courses(conn)
    for course in courses:
        print(course)
    """
    
    course_code = 'ISP100H5'
    course_details = fetch_course_details(conn, course_code)
    print("\nCourse Details:", course_details)

    meeting_sections = fetch_meeting_sections(conn, course_code)
    print("\nMeeting Sections:")
    print(meeting_sections)


if __name__ == '__main__':
    main()