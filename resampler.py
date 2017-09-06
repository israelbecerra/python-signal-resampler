

class resampler:
    'This class resamples a signal with a desired sampling rate'

    def __init__(self, signal, time, samRate):
        self.signal = signal    #original signal
        self.time = time        #time stamp for each signal sample
        self.samRate = samRate  #desired sampling rate
        self.deltaT = 1/samRate
    
    def resample(self):
        """Resamples a signal with 'samRate' sampling rate"""
        
        #we check if time and signal vectors have the same size
        if len(self.time)!=len(self.signal):
            print('****Time and signal vectors have diffent size')
            return
        
        #initialization
        n = len(self.time)
        final_t = self.time[n-1]
        
        #we always include in the new signal and new time vector the first pair (time[0],singal[0])
        new_signal = [self.signal[0]]
        new_time = [self.time[0]]
        t = self.time[0] + self.deltaT
        t_index = 1
        
        #we check that the signal has more than one element
        if n<2:
            return
        
        #we iterate through the original signal
        while True:

            #we look for the interval that contains 't'
            i0 = t_index
            for i in range(i0,n):
                if  t<=self.time[i]:#we found the needed time index
                    t_index = i
                    break
                
            #we interpolate in the right interval
            s = self.interpolate(self.time[t_index-1], self.signal[t_index-1], self.time[t_index], self.signal[t_index], t)

            #we apppend the new interpolated sample to the new signal and update the new time vector
            new_signal.append(s)
            new_time.append(t)

            #we take step further on time
            t = t + self.deltaT
            
            #we check the stop condition
            if t>self.time[n-1]:
                break

        return (new_time,new_signal)



    def interpolate(self, t1, s1, t2, s2, t):
        """Interpolates at parameter 't' between points (t1,s1) and (t2,s2)"""

        if( t1<=t and t<=t2 ): #we check 't' is not out of bounds
            m = (s2 - s1)/(t2 - t1)
            b = s1 - m*t1
            return m*t + b
        else:
            return 'OutOfBounds'


     
