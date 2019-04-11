import numpy as np
import random
import math
import h5py
import snapshot as SN
import matplotlib.pyplot as plt
from nbodykit.lab import *
from nbodykit import setup_logging, style


basePath = '/Users/usuario-mac/Desktop/Illustris-3'
fields = ['Coordinates']
dm_pos=SN.loadSubset(basePath,135,'DM',fields=fields)
print(dm_pos.shape)





x=dm_pos[:,0]/1000;
y=dm_pos[:,1]/1000;
z=dm_pos[:,2]/1000;


dm_posArr=np.array([x,y,z],dtype=[('x','f'),('y','f'),('z','f')]).T

print(dm_posArr.shape)



DMdensity_cat = ArrayCatalog(data=dm_posArr)


DMdensity_mesh=DMdensity_cat.to_mesh(Nmesh=256,BoxSize=75,window='cic', interlaced=True,position='x')
print(DMdensity_cat)


density=DMdensity_mesh.preview(Nmesh=256)

mesh = ArrayMesh(density,BoxSize=75)
real=mesh.paint(mode='real', Nmesh=256)
real=np.log10(np.abs(real))
plt.imshow(real.preview(axes=[0,2]))
plt.show() ##con estos comandos se produjeron las figuras que te envie por slack


# print(density)
#plt.imshow(DMdensity_mesh.preview(Nmesh=256,axes=[0,1]))
#plt.show()

#density=DMdensity_mesh.preview(Nmesh=256)

#one_plus_delta = DMdensity_mesh.paint(mode='real')
#print("mean of 1+delta = ", one_plus_delta.value.mean())

#density_real= (one_plus_delta*one_plus_delta.value.mean())


#mesh = density.to_mesh(window='cic')

#f=h5py.File('mesh.hdf5','w')
#dset=f.create_dataset('density',data=DMdensity_mesh.preview(Nmesh=256))
#f.close()

#plt.imshow(density)
#plt.show()

#plt.imshow(DMdensity_mesh.preview(axes=[0,1]))
#plt.show()
####overdensity####


#one_plus= DMdensity_cat.paint(mode='real')
#print(type(one_plus))










