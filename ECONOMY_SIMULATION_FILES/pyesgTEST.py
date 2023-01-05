import pyesg

# instantiate a new model with the required parameters
model = pyesg.GeometricBrownianMotion(mu=0.05, sigma=0.2)

# drift is the instantaneous drift of the process. For example,
# if we start with x0=100, what is the instantaneous drift?
model.drift(x0=100)
# array([5.])

# similarly we can measure the instantaneous diffusion
model.diffusion(x0=100)
# array([20.])

# the expectation is the expected value of the process after
# a given amount of time, dt. Here we calculate the expected
# value of the process after one year.
model.expectation(x0=100, dt=1.0)
# array([105.])

# the standard deviation is measured at a period of time too
model.standard_deviation(x0=100, dt=1.0)
# array([20.])

# prepare the arguments to generate scenarios. Here we'll
# generate 10,000 scenarios with 252 daily (trading day)
# time steps, for a one-year projection in total.
x0 = 100.0           # the start value of our process
dt = 1/252           # the length of each timestep in years
n_scenarios = 10000  # the number of scenarios to generate
n_steps = 252        # the number of time steps per scenario
random_state = 123   # optional random_state for reproducibility

# now we generate the scenarios; this outputs a numpy array. It will
# have shape (10000, 253), which represents (scenarios, timesteps).
# There are 253 timesteps because the initial value is included to start
results = model.scenarios(x0, dt, n_scenarios, n_steps, random_state)

# array([[100.        ,  98.65207527,  97.12924873, ..., 111.3500094 ,
#         112.00479028, 113.12444153],
#        [100.        , 101.27637842, 100.8971646 , ...,  61.8709475 ,
#          63.00222064,  62.22126261],
#        [100.        , 100.37636067,  99.32267874, ..., 141.66969149,
#         140.38291993, 138.91659076],
#        ...,
#        [100.        ,  99.42484152,  97.68732205, ..., 139.9306172 ,
#         139.52301459, 139.05345463],
#        [100.        , 100.75304745, 102.09894601, ..., 115.66615197,
#         116.16385992, 118.06267759],
#        [100.        , 101.24269853, 101.73381851, ...,  84.65843473,
#          84.73018762,  85.09768131]])

