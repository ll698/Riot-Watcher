import sys

import pytest

if sys.version_info > (3, 0):
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

from riotwatcher._apis import ChampionMasteryApiV4


class TestChampionMasteryApiV4(object):
    def test_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "afas"
        encrypted_summoner_id = "15462"

        ret = mastery.by_summoner(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.by_summoner.__name__,
            region,
            "https://afas.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/15462",
            {},
        )

        assert ret is expected_return

    def test_summoner_by_champion(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "fsgs"
        encrypted_summoner_id = "53526"
        champion_id = 7

        ret = mastery.by_summoner_by_champion(
            region, encrypted_summoner_id, champion_id
        )

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.by_summoner_by_champion.__name__,
            region,
            "https://fsgs.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/53526/by-champion/7",
            {},
        )

        assert ret is expected_return

    def test_scored_by_summoner(self):
        mock_base_api = MagicMock()
        expected_return = object()
        mock_base_api.raw_request.return_value = expected_return

        mastery = ChampionMasteryApiV4(mock_base_api)
        region = "fsgs"
        encrypted_summoner_id = "6243"

        ret = mastery.scores_by_summoner(region, encrypted_summoner_id)

        mock_base_api.raw_request.assert_called_once_with(
            ChampionMasteryApiV4.__name__,
            mastery.scores_by_summoner.__name__,
            region,
            "https://fsgs.api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/6243",
            {},
        )

        assert ret is expected_return
