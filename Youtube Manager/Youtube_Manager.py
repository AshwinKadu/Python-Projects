import json

def load_data():
    try:
        with open('youtube.txt' , 'r') as file:
            test = json.load(file)
            return(test)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start = 1):        
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter time duration of video : ")
    videos.append({'name' : name , 'time'  : time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos) # User will get list to chose from for updating purpose
    index = int(input("Enter number of video to Update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time' : time}
        save_data_helper (videos)
    else:
        "Invalid video index selected! "
        
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        "Invalid video index selected! "

def main():
    videos = load_data() # we will use a function to load data in videos array
    while True:
        print("/n YouTube Manager \| Choose an Option from following ")
        print("1. List of favourite videos ")
        print("2. Add a favourite videos ")
        print("3. Update a You Tube video detail ")
        print("4. Delete a YouTube video ")
        print("5. Exit The app ")
        choice = input ("Enter your choice: ")
        
        match choice:
            case '1':
                list_all_videos(videos) 
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break # this end the while loop and user will exit the app
            case _:
                print("Indvalid Choice")

if __name__ == "__main__":
    main()
