# -*- coding: utf-8 -*-

qualifiedItems = [
    "Aged Brie",
    "Backstage passes to a TAFKAL80ETC concert",
    "Sulfuras, Hand of Ragnaros"
]

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != qualifiedItems[0] and item.name != qualifiedItems[1]:
                if item.quality > 0:
                    if item.name != qualifiedItems[2]:
                        item.decrease_one_quality()
            else:
                if item.quality < 50:
                    item.increase_one_quality()
                    if item.name == qualifiedItems[1]:
                        if item.sell_in < 11:
                            item.increase_one_quality()
                        elif item.sell_in < 6:
                            item.increase_one_quality()

            if item.name != qualifiedItems[2]:
                item.decrease_one_sell_in()

            if item.sell_in < 0:
                if item.name != qualifiedItems[0]:
                    if item.name != qualifiedItems[1]:
                        if item.quality > 0:
                            if item.name != qualifiedItems[2]:
                                item.decrease_one_quality()
                    else:
                        item.clear_quality()
                else:
                    if item.quality < 50:
                        item.increase_one_quality()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def increase_one_quality(self):
        self.quality = self.quality + 1
    
    def decrease_one_quality(self):
        self.quality = self.quality - 1

    def clear_quality(self):
        self.quality = 0

    def decrease_one_sell_in(self):
        self.sell_in = self.sell_in - 1
