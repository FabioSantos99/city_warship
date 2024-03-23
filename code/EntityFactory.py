#!/usr/bin/python
# -*- coding: utf-8 -*-
from CityWarShip.pythonProject2.code.Background import Background
from CityWarShip.pythonProject2.code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'city':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'city{i}', (0, 0)))
                    list_bg.append(Background(f'city{i}', (WIN_WIDTH, 0)))
                return list_bg
