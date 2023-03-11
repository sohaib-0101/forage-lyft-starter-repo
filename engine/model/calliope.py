from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return bool(
            service_threshold_date < datetime.now().date()
            or self.engine_should_be_serviced()
        )
