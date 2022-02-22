from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from raterprojectapi.models import Game, Category



class GameTests(APITestCase):
    def setUp(self):
        url = "/register"

        player = {
            "gamertag": "Sherweezy025",
            "password": "me",
            "first_name": "sherwin",
            "last_name": "vargas",
            "username": "me@me.com",
        }
        
         # Initiate POST request and capture the response
        response = self.client.post(url, player, format='json')

        # Store the TOKEN from the response data
        self.token = Token.objects.get(pk=response.data['token'])
        
        # Use the TOKEN to authenticate the requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        #confirm 201 status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #create a category since no way to do it through urls
        game_category = Category()
        game_category.label = "Action"
        game_category.save()
        
        self.game = Game()
        self.game.createdby_id = 1
        self.game.title = "ello"
        self.game.description = "decent"
        self.game.designer = "jack"
        self.game.year_released = 2009
        self.game.num_of_players = 3
        self.game.est_time_to_play = 10
        self.game.age_recomendation = "10"
        
        self.game.save()
        self.game.categories.add(1)

    def test_create_game(self):
        url = "/games"
        
        thegame = {
            "title": "ello",
            "description": "decent",
            "designer": "jack",
            "year_released": 2009,
            "num_of_players": 3,
            "est_time_to_play": 10,
            "age_recomendation": "10",
            "categories": 1
        }
        # Initiate POST request and capture the response
        response = self.client.post(url, thegame, format='json')
        
        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Assert that the values are correct
        self.assertEqual(response.data["title"], thegame['title'])
        self.assertEqual(response.data["num_of_players"], thegame['num_of_players'])
        self.assertEqual(response.data["description"], thegame['description'])
        self.assertEqual(response.data["designer"], thegame['designer'])
        self.assertEqual(response.data["year_released"], thegame['year_released'])
        self.assertEqual(response.data["est_time_to_play"], thegame['est_time_to_play'])
        self.assertEqual(response.data["age_recomendation"], thegame['age_recomendation'])
        
    def test_get_game(self):
        url = f'/games/{self.game.id}'
        
        # Initiate GET request and capture the response
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["createdby"]["id"], self.game.createdby_id)
        self.assertEqual(response.data["title"], self.game.title)
        self.assertEqual(response.data["num_of_players"], self.game.num_of_players)
        self.assertEqual(response.data["description"], self.game.description)
        self.assertEqual(response.data["designer"], self.game.designer)
        self.assertEqual(response.data["year_released"], self.game.year_released)
        self.assertEqual(response.data["est_time_to_play"], self.game.est_time_to_play)
        self.assertEqual(response.data["age_recomendation"], self.game.age_recomendation)
        self.assertIsNotNone(response.data["categories"])
        
    def test_change_game(self):
        url = f'/games/{self.game.id}'
        
        newgame = {
            "title": "hello",
            "description": "decent",
            "designer": "jack",
            "year_released": 2009,
            "num_of_players": 3,
            "est_time_to_play": 10,
            "age_recomendation": "9"
        }
        
         # Initiate PUT request and capture the response
        response = self.client.put(url, newgame, format="json")

        # Assert that the response status code is 204 (NO CONTENT)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Initiate GET request and capture the response
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], newgame["title"])
        self.assertEqual(response.data["num_of_players"], newgame["num_of_players"])
        self.assertEqual(response.data["description"], newgame["description"])
        self.assertEqual(response.data["designer"], newgame["designer"])
        self.assertEqual(response.data["year_released"], newgame["year_released"])
        self.assertEqual(response.data["est_time_to_play"], newgame["est_time_to_play"])
        self.assertEqual(response.data["age_recomendation"], newgame["age_recomendation"])
    
    def test_get_games(self):
        url = f'/games'
        
        # Initiate GET request and capture the response
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data), 1 )

