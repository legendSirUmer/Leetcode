class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        arr,arr2 = startTime.split(":"),endTime.split(":")
        hour = int(arr2[0]) - int(arr[0])
        minutes = int(arr2[1]) - int(arr[1])
        seconds = int(arr2[2]) - int(arr[2])
        
        hour = hour * 3600
        minutes = minutes * 60

        return(hour+minutes+seconds)


sol = Solution()

print(sol.secondsBetweenTimes("12:34:56","13:00:00"))