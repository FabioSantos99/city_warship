from CityWarShip.pythonProject2.code.Enemy import Enemy
from CityWarShip.pythonProject2.code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collison_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collison_window(entity1)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
