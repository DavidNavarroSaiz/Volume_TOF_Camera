from ctypes.wintypes import PCHAR
from lib2to3.pytree import Base
from pickle import TRUE
from tkinter import ROUND, W
from unittest import TextTestResult
import h5py
import numpy as np
from vedo import *
import vedo
import vista
from pymesh import *
import pymesh as pm
from vtk import *


def norm_pc1(pc):

    min_x = np.min(pc[:, 0])
    min_y = np.min(pc[:, 1])
    min_z = np.min(pc[:, 2])

    pc[:, 0] = pc[:, 0] - min_x
    pc[:, 1] = pc[:, 1] - min_y
   

    return pc
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def norm_pc(pc):

    min_x = np.min(pc[:, 0])
    min_y = np.min(pc[:, 1])
    min_z = np.min(pc[:, 2])

    pc[:, 0] = pc[:, 0] - min_x
    pc[:, 1] = pc[:, 1] - min_y
    pc[:, 2] = pc[:, 2] - min_z

    return pc
dim_x = 606
dim_y = 888
dim_z = 444
#------------------------------obtencion de la superficie de volumen en el recipiente----------------
def resta_pc(pcres):
   
    res=np.max(pcres[:,2]) 
    a=res*0.97
    
   
    seleccion=pcres[abs(pcres[:,2])>a]
    #xyz=seleccion[:,:3]
    #seleccion=resta_valores_atipicos(seleccion,3)
   # vista_volumen=vista.vista([1,1])
    #mesh_volumen=Points(seleccion)
        
    #vista_volumen.graficar(mesh_volumen)
   
    return seleccion
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def Creacion_de_puntos_aleatorios(pc):
    ind_puntos = np.arange(0, pc.shape[0])
    puntos_aleatorios = np.random.choice(ind_puntos, size=2048, replace=False)
    pc_dwn = pc[puntos_aleatorios, :]
    return (pc_dwn)
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def suma_pc(rest1):
     k1=np.mean(rest1[:,2]) 
     res=0
     for i in rest1[0]:
        for j in rest1[1]:
            
            res=np.max(np.max(rest1[:,2]))+res
     k=res/len(rest1[2])
     return(k)

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def nube_de_puntos(pc):
      PointCloud = Points(pc, r=3.0)
      scalars = PointCloud.points()[:, 2]
      PointCloud.pointColors(scalars, cmap='magma')
      return (PointCloud)
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def resta_valores_atipicos(pcres,t):
   std=np.std(pcres)#sacar puntuacion
   ##t=0.4
   rest=np.mean(pcres)
   #--------------deteccion de valores atipicos-------------
   for h in pcres:
       salida=[]
       z=(h-rest)/std
       if (np.abs(z.any())>t):
          salida.append(h)
       salida=np.array(salida)
  
       #print("zsalida",z.shape)
       #print("zstd",std)
       #print("salida valores atipicos z",salida)
       #print("media z",rest)
      
#-----------eliminacion de los valores ----------------
   for i in salida:
        pcres=np.delete(pcres,np.where(salida==i))


   return pcres
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
def completar_vector (v,pcr):
    vi=v[5]
    g=[]
    if len(v)!=len(pcr[:,2]):
        p=[ vi for s in range((len(pcres[:,2])-len(v)))]
        p=np.array(p)
        g=np.append(v,p)
        print("p", len(g))
        pcres[:,2]=g
    return pcr
#---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
def puntos_volumen(pcres,vol):
    aux=[]
    pcr=pcres
    #res=suma_pc(vol)
    res=np.max(vol[:,2]) 
    a=res*0.98
    columna = [fila[2] for fila in pcres]
    
    seleccion=pcres[abs(pcres[:,2])>a]
    
    return seleccion


#---------------------------------------------------------------------------------------
#---------------------------------************principal*************------------------------------------------------------
with h5py.File('Capturas/Prueba_1.h5', 'r') as hdf,h5py.File('Capturas/Prueba_1_Complemento.h5', 'r') as hdf1:
    
    
    ls = list(hdf.keys())
    print("Labels:", ls)
    print("Tamaño:", len(ls))

    ls1 = list(hdf1.keys())
    print("Labels:", ls1)
    print("Tamaño:", len(ls1))

    plt = Plotter(shape=(2, 2))

#-------------- toma de datos de la imagen de referencia----------------------------------------
    Tapa=np.array(hdf.get(ls[0]))*0.025
#----------------------------------------------------------------------------    
    pcres= []
    for item in ls:
     

        pc = np.array(hdf.get(item))*0.025# Nuevos datos de la imagen con el volumen 
        
                   
       
      
       # pc= Creacion_de_puntos_aleatorios(pc)
       
       

       # print("Tamaño:", pc.shape)
       # print("Dif X:", np.max(pc[:, 0]) - np.min(pc[:, 0]))
        #print("Dif Y:", np.max(pc[:, 1]) - np.min(pc[:, 1]))
        #print("Dif Z:", np.max(pc[:, 2]) - np.min(pc[:, 2]))

        PointCloud=nube_de_puntos(pc) #creacion de nube de puntos para graficar 
       

        

        bx_pc = PointCloud.box()
        cm = PointCloud.centerOfMass()
     

        print(item)

    
        ##----------muestra imagen de referencia---------------        
    
        PointCloudres=nube_de_puntos((Tapa))
        plt.show(PointCloudres,
                bg='white',
                title="Stream", interactive=2, axes=True, at=0)
#------------------------------------------------------------
 #-----------mustra de imagen capturada---------
        plt.show(PointCloud,
                bg='white',
                title="Stream", interactive=2, axes=True, at=1)

#-----------creando una matrix con el volumen---------------------
              
        
        prueba= np.array(hdf.get(item))*0.025
        prueba=resta_pc(prueba) #superfice del volumen a medir 
        altura=suma_pc(prueba) #valor de altura de la superfice para hacer prueba 
        
        pc2=np.append(Tapa,prueba)
        aux=int( len(pc2)/3)
        pc2=np.array(pc2).reshape(aux,Tapa.shape[1])

        #pc2>>>>> matrix union superficie volumen con tarro vacio

        PointCloudrest1 =nube_de_puntos((pc2)) 
 
       
        
#---------------------------------------------------       
#-----------muestra de imagen union superfice con imagen reerencia-----------------
        plt.show(PointCloudrest1,
                bg='white',
                title="Stream", interactive=2, axes=True, at=2)

#---------- muestra de datos varios en consola----------------------------------------------------
        #print("punto tarro con volumen",pc3) 
        #print("puntos tarro vacio",Tapa)
        #print ("matrix",pc2)
        #print("altura",altura)
  
#-----------------grafica superfice del volumen---------------------------------------------------------------------- --------------------------------------------------------------------------------------------------

        PointCloudres=nube_de_puntos((prueba))
        plt.show(PointCloudres,
                    bg='white',
                    title="Stream", interactive=2, axes=True, at=3)

#-----------------------------------calculo de volumen-------------------------------------------

        if item=="Prueba_1-1":
            volref=prueba
            #volref=norm_pc(volref)
            #print("superfice volumen",volref)
            altura_ref=suma_pc(volref)
       
        varia_altura=(altura_ref-altura)/100
        #print("\n***********altura variacion*****\n",varia_altura,"\n")
    #prueba------------------------------matrix final -------------------------------------
        matrix_vol=puntos_volumen(pc2,prueba) #matrix con segmentacion de la zona donde se encuentra el volumen 
        punto=nube_de_puntos((matrix_vol))  
        plt.show(punto,
                    bg='white',
                    title="Stream", interactive=2, axes=True, at=0)    
       
        #matrix_vol>>> son la nube de puntos de la zona donde esta el volumen del recipiente 
        vista_volumen=vista.vista([1,1])
        mesh_v=Points(punto)
        matrix_vol=norm_pc(matrix_vol)
        mesh_volmen=vedo.Mesh(matrix_vol,c=None,alpha=1)
        
        vol= vedo.delaunay3D(mesh_volmen, alphaPar=0, tol=None, boundary=False)
        a=vedo.TetMesh.tomesh(vol)
    
        c= Mesh.volume(a)
        vista_volumen.graficar(a)

        print("volumen ocupado",c)



#-------------tratamiento para el siguiente archivo con las demas imagenes de volumen------------------       
    for item1 in ls1:


           # print("Tamaño:", pc.shape)
           # print("Dif X:", np.max(pc[:, 0]) - np.min(pc[:, 0]))
           # print("Dif Y:", np.max(pc[:, 1]) - np.min(pc[:, 1]))
           # print("Dif Z:", np.max(pc[:, 2]) - np.min(pc[:, 2]))
            
            print(item1)
            bx_pc = PointCloud.box()
            cm = PointCloud.centerOfMass()

            
        ##----------muestra imagen de referencia---------------        
   
            PointCloudres=nube_de_puntos((Tapa))
            plt.show(PointCloudres,
                    bg='white',
                    title="Stream", interactive=2, axes=True, at=0)
    #------------------------------------------------------------
    #-----------creando una matrix con el volumen---------------------
              
           
            prueba= np.array(hdf1.get(item1))*0.025
            pc=np.array(hdf1.get(item1))*0.025
           # pc=norm_pc(pc)
            print(prueba.shape)
            prueba=resta_pc(prueba)
            altura=suma_pc(prueba) #valor de altura de la superfice para hacer prueba 
        
            pc2=np.append(Tapa,prueba)
            aux=int( len(pc2)/3)
            pc2=np.array(pc2).reshape(aux,Tapa.shape[1])
           
            #pc2=norm_pc(pc2)
       
        
            PointCloud=nube_de_puntos((pc))
            PointCloudrest1 =nube_de_puntos(pc2) 
 
            #-----------mustra de imagen capturada---------
            plt.show(PointCloud,
                    bg='white',
                    title="Stream", interactive=2, axes=True, at=1)
        
    #---------------------------------------------------       
    #-----------muestra de imagen union superfice con imagen reerencia-----------------
            plt.show(PointCloudrest1,
                    bg='white',
                    title="Stream", interactive=2, axes=True, at=2)

    #---------- muestra de superfice del volumen----------------------------------------------------
          
            PointCloudres=nube_de_puntos((prueba))
            plt.show(PointCloudres,
                    bg='white',
                    title="Stream", interactive=2, axes=True, at=3)
#----------------------------------------------------------------------------------------------------------         
    #-----------------------------------calculo de volumen-------------------------------------------

            if ls1==ls1[1]:
                volref=prueba
                print("superfice volumen",volref.shape)
                altura_ref=suma_pc(volref)
       
          #  varia_altura=(altura_ref-altura)/100
           # print("\n***********altura variacion*****\n",varia_altura)
#prueba-------------------------------------------------------------------
            matrix_vol=puntos_volumen(pc2,prueba)
            punto=nube_de_puntos((matrix_vol))  
            plt.show(punto,
                        bg='white',
                        title="Stream", interactive=2, axes=True, at=0)    
           # print("valor maximo x",np.max(pc3[:,0]),"\nvalor minimo x",np.min(pc3[:,0]))
            #print("valor maximo y",np.max(pc3[:,1]),"\nvalor minimo y",np.min(pc3[:,1]))
            vista_volumen=vista.vista([1,1])
            mesh_v=Points(punto)
            matrix_vol=norm_pc(matrix_vol)

            mesh_volmen=vedo.Mesh(matrix_vol,c=None,alpha=1)
        
            vol= vedo.delaunay3D(mesh_volmen, alphaPar=0, tol=None, boundary=False)
            a=vedo.TetMesh.tomesh(vol)
    
            c= Mesh.volume(a)
            vista_volumen.graficar(a)

            print("volumen ocupado",c)
    #varia_altura=altura_ref-altura
    #print("\n***********altura variacion*****\n",varia_altura)
    