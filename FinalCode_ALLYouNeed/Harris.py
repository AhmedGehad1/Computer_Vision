import cv2
import numpy as np
from matplotlib import pyplot as plt

def my_harris(img_dir, threshold, window_size,ksize=3,k=0.04):

    img = cv2.imread(img_dir)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img_gaussian = cv2.GaussianBlur(img_gray,(3,3),1)

    height = img.shape[0]   
    width = img.shape[1]    

    Response_matrix = np.zeros((height,width))
    
    #  Calculate the image derivatives (Ix, Iy) and the square of the derivatives (Ix2, Iy2, IxIy)
    Ix = cv2.Sobel(img_gaussian, cv2.CV_64F, 1, 0, ksize)
    Iy = cv2.Sobel(img_gaussian, cv2.CV_64F, 0, 1, ksize)
    
    Ix2=np.square(Ix)
    Iy2=np.square(Iy)
    IxIy=Ix*Iy

    offset = int( window_size / 2 )

    # Calculate  (Sx2, Sy2 , Sxy)
    for y in range(offset, height-offset-1):
        for x in range(offset, width-offset-1):
            Sx2 = np.sum(Ix2[y-offset:y+1+offset, x-offset:x+1+offset])
            Sy2 = np.sum(Iy2[y-offset:y+1+offset, x-offset:x+1+offset])
            Sxy = np.sum(IxIy[y-offset:y+1+offset, x-offset:x+1+offset])

    # Define the matrix M(x,y)=[[Sx2,Sxy],[Sxy,Sy2]]
            M = np.array([[Sx2,Sxy],[Sxy,Sy2]])

    # Calculate the response function ( R=det(M)-k(Trace(M))^2 )
            det=np.linalg.det(M)
            #det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
            tr=np.matrix.trace(M)
            #tr = M[0, 0] + M[1, 1]
            R=det-k*(tr**2)
            Response_matrix[y,x]=R
            
    # Apply a threshold
    cv2.normalize(Response_matrix, Response_matrix, 0, 1, cv2.NORM_MINMAX)
    threshold = threshold * Response_matrix.max()

    for y in range(offset, height-offset):
        for x in range(offset, width-offset):
            value=Response_matrix[y, x]
            if value>threshold:
                cv2.circle(img,(x,y),3,(0,255,0))
                # img[y, x] = [0, 255, 0]
                # x=x+window_size
    
    # plt.figure("Manually implemented Harris detector")
    # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # plt.xticks([]), plt.yticks([])
    # plt.show()

    save_path = 'C:/Users/ahmad/Desktop/Computer_Vision/images/result.jpg'  # Define the save path
    save_result_image(img, save_path)

    return save_path

# my_harris("D:/oneDrive/Desktop/wo-Noise.jpg", 7,  0.03) 
def save_result_image(img, path):
    cv2.imwrite(path, img)
    print("Result image saved successfully at:", path)
