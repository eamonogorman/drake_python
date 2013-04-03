import asciitable

# Model A
# Read table. (Note had to convert d's to e's in raw data to allow them to be read in)
dat = asciitable.read('model_a', data_start=21)
indx = dat['col1']    # array of values from 'redshift' column
radius = dat['col2']
te = dat['col3']
nhi= dat['col4']
ne= dat['col5']
nhii= dat['col6']

#
rsol  = 6.9598e+10
rstar = 25.4*rsol
z=radius/rstar

# plot data
figure(1)
semilogx(z, te,label='All',color = 'r')  # First plot!
grid()
xlabel('Radius ($R\star$)')   # latex works!!
ylabel('Temperature (K)')
text(40, 7000, 'Model A', fontdict=None,color = 'r')

# Calculate Velocity
sig = 1.330
rho = 1.673e-24*sig*(nhi+nhii)
mloss = (2.0e-10*1.989e+33)/3.1557600e+7
vel=mloss/(4.0*3.1415926*rho*radius*radius)/1.0e+5
#Plot Velocity
figure(2)
semilogx(z, vel,label='All',color = 'r')  # First plot!
# Add text to plot
text(10, 31, 'Model A', fontdict=None,color='r')
xlabel('Radius ($R\star$)')   # latex works!!
ylabel('Velocity (km s$^{-1}$)')


# Model B
# Read table. (Note had to convert d's to e's in raw data to allow them to be read in)
dat = asciitable.read('model_b', data_start=22)
indx = dat['col1']    # array of values from 'redshift' column
radius = dat['col2']
te = dat['col3']
nhi= dat['col4']
ne= dat['col5']
nhii= dat['col6']

#
rsol  = 6.9598e+10
rstar = 25.4*rsol
z=radius/rstar

# plot data
figure(1)
semilogx(z, te, label='All',color='g')  # First plot!
grid()
xlabel('Radius ($R\star$)')   # latex works!!
ylabel('Temperature (K)')

# Add text to plot
text(10, 8200, 'Model B', fontdict=None,color='g')

# Calculate Velocity
sig = 1.330
rho = 1.673e-24*sig*(nhi+nhii)
mloss = (2.0e-10*1.989e+33)/3.1557600e+7
vel=mloss/(4.0*3.1415926*rho*radius*radius)/1.0e+5
#Plot velocity
figure(2)
semilogx(z, vel,label='All',color = 'g')  # First plot!
text(10, 41, 'Model B', fontdict=None,color='g')