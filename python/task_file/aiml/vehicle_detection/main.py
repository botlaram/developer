import cv2
import numpy as np

##start web camera or video
cap=cv2.VideoCapture("video.mp4")

count_line_position=550

offset=6 #allowable error between pixel
counter=0


##minimum width and height of rectangle
min_width=80
min_height=80

##initialize subtructor
algo=cv2.bgsegm.createBackgroundSubtractorMOG()   #remove background from video

#count vehicles
def center_handler(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx=x+x1
    cy=y+y1
    return cx,cy

detect_vehicle=[] #appending count vehicle

##loop to cont. the video
while True:
    ret,frame1=cap.read() #read video frame
    grey=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY) #convert color to gray
    blur=cv2.GaussianBlur(grey,(3,3),5) #fix blur point
    
    ## apply on each frame
    img_sub=algo.apply(blur)

    #dilat > detect and structure the neighbour pixel
    #np here use to create a grid of pixels
    dilat=cv2.dilate(img_sub,np.ones((5,5)))
    kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) #reshape the algorithm
    
    #morphological operations to increase the size of objects in images as well as decrease them
    dilatada=cv2.morphologyEx(dilat,cv2.MORPH_CLOSE,kernel)
    dilatada=cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE,kernel)
    
    #count binary image using algorithm  #h-height
    counterShape,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    ##draw line to start count vehicle from the line
    #frame1(startline,endline,color,thickness)
    cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(255,127,0),3)
    
    ##for loop to draw rectangle
    for (i,c) in enumerate(counterShape):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_counter= (w>=min_width) and (h>=min_height)
        if not validate_counter:
            continue
        ##(x,y) generate random when detect vehicles
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        
        ##here y-2 means about the y axix
        cv2.putText(frame1,"Vehicle Counter :"+str(counter),(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        center=center_handler(x,y,w,h)
        detect_vehicle.append(center)
        cv2.circle(frame1,center,4,(0,0,255),-1)

        for (x,y) in detect_vehicle:
            if y<(count_line_position+offset) and y>(count_line_position-offset): #count vehicle if pass the line position
                counter+=1
                cv2.line(frame1,(25,count_line_position),(1200,count_line_position),(0,127,255),3) #change the color after crossing the line
                detect_vehicle.remove((x,y))
                print("count vehicle : "+str(counter))
            
    ##text on figure
    cv2.putText(frame1,"Vehicle Counter :"+str(counter),(450,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),5)
    
    # cv2.imshow("Detector",dilatada)  ##to check it works

    cv2.imshow("Display Video",frame1) #show video
    
    ##close window
    if cv2.waitKey(1) == 13: ##press Enter to close the  video
        break

cv2.destroyAllWindows() #destroy all
cap.release()