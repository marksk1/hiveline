from hiveline import get_database

droppable_collections = [
    'jobs',
    'route-results',
    'simulations',
    'stats',
    'trace-arcs',
    'trace-graphs',
    'virtual-commuters'
]


def purge_sim_data(sim_id, db=None):
    """
    Purge all data associated with a simulation from the database.
    :param sim_id: The id of the simulation to purge.
    :param db: The database to purge the data from.
    :return:
    """
    if db is None:
        db = get_database()

    for collection in droppable_collections:
        result = db[collection].delete_many({'sim-id': sim_id})
        print(f"Deleted {result.deleted_count} documents from {collection}")


if __name__ == '__main__':
    purge_sim_data("35e58b29-ea03-4b34-b533-05c848b9fb31")
    purge_sim_data("9a0194be-b1be-425c-a408-98163e03ab56")
