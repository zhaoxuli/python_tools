import cv2
import numpy  as np
def get_heat_map(shape_lst=[500,30,3],Gray_init=[1,90,255],k=100):
    h,w,c =shape_lst
    if h%k != 0:
        print 'k must be height`s divisor '
        quit()
    B_init,G_init,R_init =Gray_init

    init_mat = np.ones((h,w,c))
    init_mat[:,:,0] = init_mat[:,:,0] *B_init#B
    init_mat[:,:,1] = init_mat[:,:,1] *G_init #G
    init_mat[:,:,2] = init_mat[:,:,2] *R_init #R

    out_mat = init_mat.astype(np.uint8)

    print  out_mat.dtype
    print out_mat.shape
    for i in range(k):
        step = h/k
        start = step*i
        out_mat[start:start+step,:,0] = B_init+((255-B_init)/k)*i
        if  i < k/2:
            out_mat[start:start+step,:,1] = G_init+((255-G_init)/(k/2))*i
        else:
            out_mat[start:start+step,:,1] = G_init+((255-G_init)/(k/2))*(k/2)-((255-G_init)/(k/2))*(i-k/2)
        out_mat[start:start+step,:,2] = R_init - (R_init/k)*i
        #print 'start:end',start,start+step
        #print 'B:',out_mat[start,:,0][0],
        #print 'G:',out_mat[start,:,1][0],
        #print 'R:',out_mat[start,:,2][0]
    cv2.imshow('test',out_mat)
    cv2.waitKey()
    return out_mat
get_heat_map()
