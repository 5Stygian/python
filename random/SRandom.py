import datetime

currentTime = datetime.datetime.now()

class StygianRandom:
    def normalize(number, min_value, max_value):
        if max_value == min_value:
            return 0
        return (number - min_value) / (max_value - min_value)

    def random():
        time = int(currentTime.strftime("%f"))
        normalizedOut = StygianRandom.normalize(time, 0, 1)
        return normalizedOut
    
print(StygianRandom.random())
