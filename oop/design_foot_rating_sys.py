from typing import List 
import heapq

class HeapItem:
    def __init__(self, rating, name):
        self.rating = rating
        self.name = name

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.name < other.name
        return self.rating > other.rating

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_dict = {}
        self.food_cuisine = {}
        self.food_rating_map = {}
        for idx in range(len(foods)):
            food = foods[idx]
            cuisine = cuisines[idx]
            rating = ratings[idx]
            item = HeapItem(rating, food)

            if cuisine not in self.food_dict:
                self.food_dict[cuisine] = []
            heapq.heappush(self.food_dict[cuisine], item)

            self.food_cuisine[food] = cuisine
            self.food_rating_map[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        self.food_rating_map[food] = newRating
        heapq.heappush(self.food_dict[cuisine], HeapItem(newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest_rated_item = self.food_dict[cuisine][0]
        # this trick helps avoid heapify every single time. check if my current rating matches with the most up to date rating
        while highest_rated_item.rating != self.food_rating_map[highest_rated_item.name]:
            heapq.heappop(self.food_dict[cuisine])
            highest_rated_item = self.food_dict[cuisine][0]
        return highest_rated_item.name


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)