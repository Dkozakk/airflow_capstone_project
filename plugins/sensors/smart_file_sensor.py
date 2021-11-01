
from airflow.sensors.filesystem import FileSensor
from airflow.utils.decorators import apply_defaults


class SmartFileSensor(FileSensor):
    poke_context_fields = ("filepath", "fs_conn_id")

    @apply_defaults
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def is_smart_sensor_compatible(self):
        return (
            not self.soft_fail
            and super().is_smart_sensor_compatible()
        )
