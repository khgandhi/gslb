from gslb.drivers.plugin_driver import GslbAbstractDriver

__author__ = 'kugandhi'

class NoOpPluginDriver(GslbAbstractDriver):

    """
        This is the no op plugin driver that only logs the invocation and update the database..
    """
    def delete_member(self, context, member):
        super(NoOpPluginDriver, self).delete_member(context, member)

    def create_loadbalancer(self, context, loadbalancer):
        super(NoOpPluginDriver, self).create_loadbalancer(context, loadbalancer)

    def delete_healthmonitor(self, context, healthmonitor):
        super(NoOpPluginDriver, self).delete_healthmonitor(context, healthmonitor)

    def delete_pooL_healthmonitor(self, context, pool_id, healthmonitor):
        super(NoOpPluginDriver, self).delete_pooL_healthmonitor(context, pool_id, healthmonitor)

    def create_healthmonitor(self, context, healthmonitor):
        super(NoOpPluginDriver, self).create_healthmonitor(context, healthmonitor)

    def delete_entity_status(self, context, entity):
        super(NoOpPluginDriver, self).delete_entity_status(context, entity)

    def delete_pool(self, context, pool):
        super(NoOpPluginDriver, self).delete_pool(context, pool)

    def create_pool_healthmonitor(self, context, pool_id, healthmonitor):
        super(NoOpPluginDriver, self).create_pool_healthmonitor(context, pool_id, healthmonitor)

    def delete_loadbalancer(self, context, loadbalancer):
        super(NoOpPluginDriver, self).delete_loadbalancer(context, loadbalancer)

    def create_pool(self, context, pool):
        super(NoOpPluginDriver, self).create_pool(context, pool)

    def update_entity_status(self, context, entity_id, state):
        super(NoOpPluginDriver, self).update_entity_status(context, entity_id, state)

    def create_member(self, context, member):
        super(NoOpPluginDriver, self).create_member(context, member)