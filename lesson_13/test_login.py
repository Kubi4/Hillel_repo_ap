import unittest
from login import log_event

class TestLogEvent(unittest.TestCase):

    def test_log_event_success(self):
        with self.assertLogs("log_event", level="INFO") as cm:
            log_event("john", "success")
        self.assertEqual(len(cm.records), 1)
        self.assertIn("Login event - Username: john, Status: success", cm.output[0],)

    def test_log_event_expired(self):
        with self.assertLogs("log_event", level="WARNING") as cm:
            log_event("john", "expired")
        self.assertEqual(len(cm.records), 1)
        self.assertIn("Login event - Username: john, Status: expired",cm.output[0],)

    def test_log_event_failed(self):
        with self.assertLogs("log_event", level="ERROR") as cm:
            log_event("john", "failed")
        self.assertEqual(len(cm.records), 1)
        self.assertIn("Login event - Username: john, Status: failed",cm.output[0],)

if __name__ == "__main__":
    unittest.main()