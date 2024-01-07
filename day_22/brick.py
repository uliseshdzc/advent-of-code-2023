from __future__ import annotations
from point import Point


class Brick:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.children: set[Brick] = set()
        self.parents: set[Brick] = set() 

    def __repr__(self) -> str:
        return  "[" + str(self.start.x) + "," + \
                str(self.start.y) + "," + \
                str(self.start.z) + "]-[" + \
                str(self.end.x) + "," + \
                str(self.end.y) + "," + \
                str(self.end.z) + "]"       

    def set_height(self, height): 
        self.end.z = self.end.z - self.start.z + height
        self.start.z = height

    def overlaps(self, brick: Brick):
        return  max(self.start.x, brick.start.x) <= min(self.end.x, brick.end.x) and \
                max(self.start.y, brick.start.y) <= min(self.end.y, brick.end.y)
    
    def removable(self):
        for child in self.children:
            if len(child.parents) == 1:
                return False
        return True

    def drop(self, settled_bricks: list[Brick]):
        height = 1
        overlap_bricks: list[Brick] = []

        for brick in settled_bricks:
            if self.overlaps(brick):
                overlap_bricks.append(brick)
                height = max(height, brick.end.z + 1)
        self.set_height(height)

        for brick in overlap_bricks:
            if height == brick.end.z + 1:
                self.parents.add(brick)
                brick.children.add(self)

    def count_falling(self, falling: set[Brick]):
        count = 0
        to_fall: list[Brick] = []

        for child in self.children:
            if child in falling:
                continue

            if sum([parent not in falling for parent in child.parents]) == 0:   
                count += 1
                falling.add(child)
                to_fall.append(child)   

        for brick in to_fall:
            count += brick.count_falling(falling)                                         

        return count