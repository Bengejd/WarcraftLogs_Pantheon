from warcraftlogs.models.base import BaseMeta

__all__ = ["Report"]


class Report(metaclass=BaseMeta):
    pk = ("id", "name")
    id = "id"
    name = "name"
    owner = "owner"
    zone = "zone"
    startTime = "startTime"
    endTime = "endTime"

    @classmethod
    def _get_report_from_dict(cls, data, default=None):
        return {
            e.id: e
            for e in [
                Report.from_dict(i)
                for i in data.get(cls.attributes["report"], [])
            ]
        }