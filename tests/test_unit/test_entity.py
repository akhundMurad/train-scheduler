from scheduler.domain.common.entity import Entity


def test_entity() -> None:
    entity_1 = Entity()
    entity_2 = Entity()

    assert entity_1 != entity_2
