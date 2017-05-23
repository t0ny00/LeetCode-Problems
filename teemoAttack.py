In LLP world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

# You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

# # Example 1:
# Input: [1,4], 2
# Output: 4
# Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
# This poisoned status will last 2 seconds until the end of time point 2. 
# And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
# So you finally need to output 4.


def teemoAttack(frames, duration):
  endtime = -1
  time_poisoned = 0
  if (len(frames) == 1): return duration
  for frame in frames:
    if (frame <= endtime): time_poisoned += endtime - frame - 1
    else: time_poisoned += duration 
    endtime = frame + duration - 1
  time_poisoned += duration
  return time_poisoned
  
print (teemoAttack([1,2,5],2))
