import cv2
import skimage.io 
import sys

def open_img(name):
    img = skimage.io.imread(name,0)
    return img

def codificador(img_input, name_output, p,msg):
    l, c, d = img_input.shape
    img_output = img_input.copy()
    aux = 0
    for i in range(l):
        for j in range(c):
                if aux >= (len(msg)):
                    break
                a = '{0:08b}'.format(img_input[i][j][0])
                a = a[0:(7-p)]+msg[aux]+a[(8-p):8]
                aux += 1
                img_output[i][j][0] = int(a,2)
                if aux >= (len(msg)):
                    break
                a = '{0:08b}'.format(img_input[i][j][1])
                a = a[0:(7-p)]+msg[aux]+a[(8-p):8]
                aux += 1
                img_output[i][j][1] = int(a,2)
                if aux >= (len(msg)):
                    break
                a = '{0:08b}'.format(img_input[i][j][2])
                a = a[0:(7-p)]+msg[aux]+a[(8-p):8]
                aux += 1
                img_output[i][j][2] = int(a,2)      
    cv2.imwrite(name_output, cv2.cvtColor(img_output, cv2.COLOR_RGB2BGR))
    return img_output
    
def convert_msg(msg):
    new_msg =[ord(c) for c in msg]
    msg = ''.join(('{0:08b}'.format(c)) for c in new_msg)
    msg += '0101110000110000' 
    return msg

def plano_bits( img, p):
    l, c, d = img.shape
    for i in range(l):
        for j in range(c):
            a = '{0:08b}'.format(img[i][j][0])
            img[i][j][0] = int(a[7-p],2)
            a = '{0:08b}'.format(img[i][j][1])
            img[i][j][1] = int(a[7-p],2)
            a = '{0:08b}'.format(img[i][j][2])
            img[i][j][2] = int(a[7-p],2)
    img[img > 0] = 255
    cv2.imwrite("Plano de bit "+str(p)+"_imagem resultante.png", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    

def main():
    img = open_img(str(sys.argv[1]))
    f = open(str(sys.argv[2]), "r")
    msg = f.read()
    f.close()
    p = int(sys.argv[3])
    if (p<0 or p>3):
        p=0
    img_out = str(sys.argv[4])
    msg = convert_msg(msg)
    img_res = codificador(img, img_out,p,msg)
    plano_bits(img_res.copy(), 7)
    plano_bits(img_res.copy(), 0)
    plano_bits(img_res.copy(), 1)
    plano_bits(img_res.copy(), 2)
    
if __name__ == "__main__":
    main()
