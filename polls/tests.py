import datetime
from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client
from polls.models import Poll

def create_poll(question, days):
	"""
	Creates a poll with the given 'question' published the given number of
	'days' offset to now (negative for polls published in the past,
	positive for polls that have yet to be published)
	"""
	return Poll.objects.create(question=question,
		pub_date=timezone.now() _ datetime.timedelta(days=days))

class PollMethodTests(TestCase):

	def test_was_published_recently_with_future_poll(self):
		"""
		was published_recently() should reutrn False for polls whose
		pub_date is in the future
		"""
		future_poll = Poll(pub_date=timezone.now()+ datetime.timedelta(days=30))
		self.assertEqual(future_poll.was_published_recently(), False)
	def test_was_published_recently_with_old_poll(self):
		"""
		was_published_recently() should reutnr False for polls whose pub_date
		is older than 1 day
		"""
		old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
		self.assertEqual(old_poll.was_published_recently(), False)
		def test_was_published_recently_with_recent_poll(self):
			"""
			was_published_recently() should reutrn True for polls whose pub_date
			is within the last day
			"""
			recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
			self.assertEqual(recent_poll.was_published_recently(), True)

class PollViewTests(TestCase):
	def test_index_view_with_no_polls(self):
		"""
		if no polls exist, an appropriate message should be displayed
		"""
		response = self.client.get(reverse)
		self.assertEqual(response.status_code=200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_poll_list']), [])
	def test_index_view_with_a_past_poll(self):
		pass
	def test_index_view_with_a_future_poll(self):
		pass
	def test_index_view_with_future_poll_and_past_poll(self):
		pass
	def test_index_view_with_two_past_polls(self):
		pass


