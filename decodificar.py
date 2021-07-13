import cv2
import skimage.io 
import binascii
import sys

def open_img(name):
    img = skimage.io.imread(name,0)
    return img


def cut_msg(msg):
    new_msg = ''
    for i in range (len(msg)-8):
        if(msg[i*8:(i*8)+16]== '0101110000110000'):
            return new_msg
        else:
            new_msg += msg[i*8:i*8+8]
    return new_msg


def decodificador(img_output, p):
    l, c, d = img_output.shape
    msg=''
    for i in range(l):
        for j in range(c):
            a = '{0:08b}'.format(img_output[i][j][0])
            msg += a[7-p]
            a = '{0:08b}'.format(img_output[i][j][1])
            msg += a[7-p]
            a = '{0:08b}'.format(img_output[i][j][2])
            msg += a[7-p]
            
    msg = cut_msg(msg)
    n = int(msg, 2)
    qlenf=len(msg)
    qlenf=(qlenf/8)*2
    qlenf=str(qlenf)
    qlenf="%0"+qlenf+"x"
    ascii_msg = binascii.unhexlify(qlenf % n)
    ascii_msg = ascii_msg.decode("utf-8", "ignore")
    
    return ascii_msg


def main():
    img = open_img(str(sys.argv[1]))
    p = int(sys.argv[2])
    if (p<0 or p>3):
        p=0
    msg_out = str(sys.argv[3])
    msg = decodificador(img,p)
    f = open(msg_out, "w")
    f.write(msg)
    f.close()
    

if __name__ == "__main__":
    main()
