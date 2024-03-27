import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
        id INT PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
)
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    conn.commit()
    return cursor.lastrowid

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()

def delete_video():
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\n YouTube manager app with DB")
        print(" 1. List Videos")
        print(" 2. Add videos")
        print(" 3. Update videos")
        print(" 4. Delete videos")
        print(" 5. Exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input ("Enter your time: ")
            add_video(name,time)

        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter video name: ")
            time = input ("Enter your time: ")
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)

        elif choice == '5':
            break
        
        else:
            print("Choice is invalid")
    conn.close()

if __name__ == '__main__':
    main()