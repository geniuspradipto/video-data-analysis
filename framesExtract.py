import cv2
import os

def extract_frames(video_path):
    # collecting the video file's name without extension mp4
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_dir = f"frames-{video_name}"  # e.g., frames-vid1 for vid1.mp4
    
    # Check if the folder already exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created folder: {output_dir}")
    else:
        print(f"Folder {output_dir} already exists. Skipping folder creation.")
        return
    
    # Loading the video using VideoCapture function in opencv
    capture = cv2.VideoCapture(video_path) # capture object is the captured frame
    
    frame_count = 0
    
    while capture.isOpened(): #isOpened fncn is checking whether the video is properly opened
        isread, frame = capture.read() # isread is boolean , specifying whether the frame is read or not and frame is the actual captured frame
        
        if not isread:  # if no frames are left to read
            break
        
        # Saving the current frame as a jpg image and then incrementing the frame_count for the next file name
        frame_filename = os.path.join(output_dir, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame) # imwrite function saves the frame as an image file
        
        frame_count += 1
    
    capture.release() #release function closes the video file
    print(f"Extracted {frame_count} frames to {output_dir}")

# let's specify the path of the video and call the function
video_path = 'vid2.mp4' # since it is in the same path
# output_dir = 'frames'  # we are creating a subfolder called 'frames' in the current directory and we will put all the images there

extract_frames(video_path)
