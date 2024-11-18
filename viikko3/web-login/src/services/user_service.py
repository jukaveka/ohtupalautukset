from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
from string import ascii_letters

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass



class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if user:
            raise UserInputError("Username already in use. Select another username")
        elif len(username) < 3 or not self.check_input_for_all_string_characters(username):
            raise UserInputError("Invalid username. User name be at least 3 characters long, and contain only letters within a-z")
        
        if password != password_confirmation:
            raise UserInputError("Invalid password. Password confirmation does not match the given password")
        
        if len(password) < 8 or self.check_input_for_all_string_characters(password):
            raise UserInputError("Invalid password. Password must be at least 8 characters long, and contain at least one number or special character")

    def check_input_for_all_string_characters(self, input):
        for character in input:
            if character not in ascii_letters:
                return False
            
        return True

user_service = UserService()
