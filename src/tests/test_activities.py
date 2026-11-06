import unittest
from unittest.mock import patch

from src.backend.routers.activities import get_activities


class GetActivitiesTests(unittest.TestCase):
    @patch("src.backend.routers.activities.activities_collection")
    def test_filters_by_difficulty(self, activities_collection):
        activities_collection.find.return_value = []

        get_activities(difficulty="Intermediate")

        activities_collection.find.assert_called_once_with(
            {"difficulty": "Intermediate"}
        )

    @patch("src.backend.routers.activities.activities_collection")
    def test_all_difficulty_filter_matches_unspecified_activities(
        self, activities_collection
    ):
        activities_collection.find.return_value = []

        get_activities(day="Monday", difficulty="all")

        activities_collection.find.assert_called_once_with(
            {
                "schedule_details.days": {"$in": ["Monday"]},
                "$or": [
                    {"difficulty": {"$exists": False}},
                    {"difficulty": None},
                ],
            }
        )


if __name__ == "__main__":
    unittest.main()
