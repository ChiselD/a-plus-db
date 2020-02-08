from .db_connection import DatabaseConnection
from typing import List, Dict, Union

"""
Saves A+ question/answer data in an SQL database
Data format:
[
	{
		'id': question_id,
		'test': test_number,
		'question': question_text,
		'answer_options': [optionA, optionB, optionC, optionD],
		'correct_answer': answer_text
	}
]
"""

# We define our own type here
Question = Dict[str, Union[str, int, List[str]]]


def create_table() -> None:
	with DatabaseConnection("data.db") as connection:
		cursor = connection.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS aplus(id integer primary key, test integer, question text, answer_options List, correct_answer text)")


def get_all_questions() -> List[Question]:
	with DatabaseConnection("data.db") as connection:
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM aplus")
		# cursor.fetchall() returns a list of tuples
		aplus = [{
			'id': row[0],
			'test': row[1],
			'question': row[2],
			'answer_options': row[3],
			'correct_answer': row[4]
			} for row in cursor.fetchall()]
	return aplus


