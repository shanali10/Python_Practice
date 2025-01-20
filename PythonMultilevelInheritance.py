class BigBang:
    noOfStars = 1
    def stars(self):
        return f"At the time of BigBang no. of Stars was {self.noOfStars}"

class Universe(BigBang):
    # noOfStars = 1000000000010
    noOfPlanets = 10000038

    def starsPlanets(self):
        return f"At the time of Universe Creation" \
               f" no. of Stars was {self.noOfStars}" \
               f" and no. of Planets was {self.noOfPlanets}"


class Earth(Universe):
    noOfStars = 1000000000000000000005
    noOfPlanets = 10000000000000000000000000003

    # def starsPlanets(self):
    #     return f"At the time of Earth Creation" \
    #            f" no. of Stars was {self.noOfStars}" \
    #            f" and no. of Planets was {self.noOfPlanets}"

    pass

bg = BigBang()
uni = Universe()
earth = Earth()

print(bg.stars())
print(uni.starsPlanets())
print(earth.starsPlanets())

print(uni.noOfStars)