# need to work on exception handling outside of the context of APIs.

class UserNotFoundError(Exception):
    code = 404
    description = {"error message": "The user ID specified was not found in the database. Please check and try again."}

class TweetNotFoundError(Exception):
    code = 404
    description = {"error message": "The tweet specified using the tweet ID was not found in the database. Please check and try again."}

class InvalidSortCriterionError(Exception):
    code = 400
    description = {"error message": "The sort criterion specified is invalid. If you wish to sort your results, please specify one of 'oldestToNewest', 'newestToOldest' or 'popularity'."}

class UnsuccessfulConnectionPostgreSQL(Exception):
    code = 400
    description = {"error message": "Unable to connect to PostgreSQL. Please try again."}

class NoParametersGivenError(Exception):
    code = 400
    description = {"error message": "No search parameters specified. Please specify one of username_for_user_info, user_id_for_tweets, username_tweets, user_id, tweet_id, keyword, hashtags or location."}

class TooManyParametersGivenError(Exception):
    code = 400
    description = {"error message": "Too many search parameters specified. Please specify only one of username_for_user_info, user_id_for_tweets, username_tweets, user_id, tweet_id, keyword, hashtags or location."}