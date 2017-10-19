import numpy as np

def c3_img_to_c1(I):
    I = I.astype('uint8')
    if len(I.shape) == 3:
        h,w,c = I.shape
        assert c == 3, 'must be 3 channel image'
        a = I[:,:,0]
        b = I[:,:,1]
        c = I[:,:,2]

        Res = np.zeros((h, w), 'uint32')
        Res[:,:] = a
        Res = np.left_shift(Res, 8)

        Res[:,:] += b
        Res = np.left_shift(Res, 8)

        Res[:,:] += c
    elif len(I.shape) == 2:
        h,c = I.shape
        assert c == 3, 'must be 3 channel image'
        a = I[:,0]
        b = I[:,1]
        c = I[:,2]
        Res = np.zeros((h), 'uint32')
        Res[:] = a
        Res = np.left_shift(Res, 8)
        Res[:] += b
        Res = np.left_shift(Res, 8)
        Res[:] += c
    else:
        raise Exception("Invalid shape:" + str(I.shape))
    
    return Res

def c1_img_to_c3(I):
    mask = np.ones_like(I, 'uint32')
    mask *= 255
    I3 = np.bitwise_and(I, mask).astype('uint8')
    I = np.right_shift(I, 8)
    I2 = np.bitwise_and(I, mask).astype('uint8')
    I = np.right_shift(I, 8)
    I1 = I.astype('uint8')
    Res = np.array([I1, I2, I3], 'uint8')
    if len(I.shape) == 2:
        return np.moveaxis(Res, 0, 2)
    elif len(I.shape) == 1:
        return np.transpose(Res)
    else:
        raise Exception("Invalid shape:" + str(I.shape))
