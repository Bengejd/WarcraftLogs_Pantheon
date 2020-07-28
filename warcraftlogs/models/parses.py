from warcraftlogs.models.base import BaseMeta

__all__ = ["Parse"]


class Parse(metaclass=BaseMeta):
    pk = ("id", "fightID")
    id = 'reportID'
    rank = 'rank'
    outOf = 'outOf'
    total = 'total'
    klass = 'class'
    spec = 'spec'
    guild = 'guild'
    duration = 'duration'
    startTime = 'startTime'
    itemlevel = 'itemLevel'
    patch = 'patch'
    reportID = 'reportID'
    fightID = 'fightID'
    difficulty = 'difficulty'
    size = 'size'
    estimated = 'estimated'
    encounterID = 'encounterID'
    encounterName = 'encounterName'
    percentile = 'percentile'

    @classmethod
    def _get_parse_from_dict(cls, data, default=None):
        return {
            e.id: e
            for e in [
                Parse.from_dict(i)
                for i in data.get(cls.attributes["parses"], [])
            ]
        }
