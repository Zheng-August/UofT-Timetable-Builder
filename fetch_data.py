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

def fetch_key_sections(conn, course_key):
    cursor = conn.cursor()

    query = "SELECT * FROM courses WHERE course_code LIKE ? OR name LIKE ?"
    param = ('%' + course_key + '%','%' + course_key + '%')
    cursor.execute(query, param)
    courses = cursor.fetchall()

    course_list = []
    for course in courses:
        course_list.append(' '.join(course[2:5]))
    return course_list


def fetch_special_sections(conn, course_code, section_code):
    cursor = conn.cursor()

    query = "SELECT * FROM courses WHERE course_code = ? AND section_code = ?"
    param = (course_code,section_code)
    cursor.execute(query, param)
    course = cursor.fetchall()

    course_id = course[0][1] # get id
    cursor.execute('SELECT * FROM meeting_sections WHERE course_id = ?', (course_id,))
    meeting_times = cursor.fetchall()

    return meeting_times

    


def main():
    db_path = 'courses.db'
    conn = connect_to_database(db_path)
    
    """courses = fetch_all_courses(conn)
    for course in courses:
        print(course)
    """
    
    # course_code = 'ISP100H5'
    # course_details = fetch_course_details(conn, course_code)
    # print("\nCourse Details:", course_details)

    # meeting_sections = fetch_meeting_sections(conn, course_code)
    # print("\nMeeting Sections:")
    # print(meeting_sections)
    
    # course_key = 'csc108H1'
    # course_details = fetch_key_sections(conn, course_key)
    # print("\nCourse Details:", course_details)

    course_code = 'CSC108H1'
    section_code = 'F'
    course_details = fetch_special_sections(conn, course_code, section_code)
    print(course_details)


if __name__ == '__main__':
    main()